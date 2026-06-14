#!/usr/bin/env python3
"""
🏆 FIFA World Cup 2026 Telegram Bot — Multi-User Edition
- যে কেউ /start দিলে সে অটো রেজিস্টার হয়ে সব অ্যালার্ট পাবে
- /stop দিলে আনসাবস্ক্রাইব হবে
- প্রতিদিন সকাল ৮টায় দৈনিক সূচি
- ম্যাচের ১ ঘন্টা আগে রিমাইন্ডার
- ম্যাচ শুরুর মুহূর্তে কিক-অফ অ্যালার্ট
"""

import os
import json
import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from schedule_data import MATCHES

# ─── কনফিগারেশন ───────────────────────────────────────────────
BOT_TOKEN    = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
USERS_FILE   = Path("subscribers.json")   # রেজিস্টার্ড ইউজার সেভ হবে এখানে

BD_TZ  = pytz.timezone("Asia/Dhaka")
UTC_TZ = pytz.utc

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── সাবস্ক্রাইবার ম্যানেজমেন্ট ──────────────────────────────

def load_subscribers() -> set[int]:
    """ফাইল থেকে সাবস্ক্রাইবার লিস্ট লোড করো"""
    if USERS_FILE.exists():
        try:
            return set(json.loads(USERS_FILE.read_text()))
        except Exception:
            return set()
    return set()

def save_subscribers(subs: set[int]):
    """সাবস্ক্রাইবার লিস্ট ফাইলে সেভ করো"""
    USERS_FILE.write_text(json.dumps(list(subs)))

# মেমোরিতে রাখো (বট চলার সময়)
subscribers: set[int] = load_subscribers()

# ─── ডুপ্লিকেট প্রতিরোধ ──────────────────────────────────────
_sent_alerts: set[str] = set()

# ─── হেল্পার ──────────────────────────────────────────────────

def utc_to_bd(utc_dt: datetime) -> datetime:
    if utc_dt.tzinfo is None:
        utc_dt = UTC_TZ.localize(utc_dt)
    return utc_dt.astimezone(BD_TZ)

def get_matches_for_date(date: datetime) -> list[dict]:
    target = date.strftime("%Y-%m-%d")
    result = []
    for m in MATCHES:
        bd_dt = utc_to_bd(datetime.strptime(m["utc"], "%Y-%m-%d %H:%M"))
        if bd_dt.strftime("%Y-%m-%d") == target:
            result.append({**m, "bd_dt": bd_dt})
    return sorted(result, key=lambda x: x["bd_dt"])

async def broadcast(bot, text: str):
    """সব সাবস্ক্রাইবারকে মেসেজ পাঠাও"""
    dead = set()
    for uid in list(subscribers):
        try:
            await bot.send_message(chat_id=uid, text=text, parse_mode="HTML")
            await asyncio.sleep(0.05)   # Telegram rate limit
        except Exception as e:
            err = str(e).lower()
            # ব্লক করলে বা চ্যাট না থাকলে লিস্ট থেকে বাদ দাও
            if "blocked" in err or "not found" in err or "deactivated" in err:
                dead.add(uid)
                logger.info(f"Removed inactive user: {uid}")
    if dead:
        subscribers.difference_update(dead)
        save_subscribers(subscribers)

# ─── মেসেজ ফরম্যাট ────────────────────────────────────────────

def format_daily_schedule(matches: list[dict], label: str) -> str:
    if not matches:
        return f"📅 <b>{label}</b>\n\nকোনো ম্যাচ নেই।"
    lines = [f"🏆 <b>FIFA বিশ্বকাপ ২০২৬ — {label}</b>\n"]
    for m in matches:
        t = m["bd_dt"].strftime("%I:%M %p")
        lines.append(
            f"⚽ <b>{m['home']} 🆚 {m['away']}</b>\n"
            f"   🕐 {t} (বাংলাদেশ সময়)\n"
            f"   🏟️ {m['venue']}\n"
            f"   📌 {m['stage']}\n"
        )
    lines.append("🔔 ম্যাচের ১ ঘন্টা আগে রিমাইন্ডার + শুরুতে 🚨 কিক-অফ অ্যালার্ট পাবেন!")
    return "\n".join(lines)

def format_reminder(m: dict, bd_dt: datetime) -> str:
    t = bd_dt.strftime("%I:%M %p")
    return (
        f"⏰ <b>ম্যাচ শুরু হতে ১ ঘন্টা বাকি!</b>\n\n"
        f"⚽ <b>{m['home']} 🆚 {m['away']}</b>\n"
        f"🕐 {t} (বাংলাদেশ সময়)\n"
        f"🏟️ {m['venue']}\n"
        f"📌 {m['stage']}\n\n"
        f"📺 প্রস্তুত হয়ে যান! গো গো গো! 🎉"
    )

def format_kickoff(m: dict, bd_dt: datetime) -> str:
    t = bd_dt.strftime("%I:%M %p")
    return (
        f"🚨🔴 <b>ম্যাচ এখনই শুরু হচ্ছে!</b> 🔴🚨\n\n"
        f"⚽ <b>{m['home']} 🆚 {m['away']}</b>\n"
        f"🕐 {t} (বাংলাদেশ সময়)\n"
        f"🏟️ {m['venue']}\n"
        f"📌 {m['stage']}\n\n"
        f"🎙️ বল গড়াচ্ছে — এখনই চ্যানেল খুলুন! 🏆🔥"
    )

# ─── কমান্ড হ্যান্ডলার ────────────────────────────────────────

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid  = update.effective_user.id
    name = update.effective_user.first_name or "বন্ধু"

    if uid not in subscribers:
        subscribers.add(uid)
        save_subscribers(subscribers)
        greeting = f"✅ <b>স্বাগতম, {name}!</b> আপনি সফলভাবে সাবস্ক্রাইব করেছেন!\n\n"
    else:
        greeting = f"👋 <b>আবার স্বাগতম, {name}!</b> আপনি আগে থেকেই সাবস্ক্রাইব করা আছেন।\n\n"

    text = (
        greeting +
        "আপনি পাবেন:\n"
        "✅ প্রতিদিন সকাল ৮টায় দৈনিক ম্যাচ সূচি\n"
        "✅ প্রতিটি ম্যাচের ১ ঘন্টা আগে রিমাইন্ডার\n"
        "✅ ম্যাচ শুরুর মুহূর্তে 🚨 কিক-অফ অ্যালার্ট\n\n"
        "<b>কমান্ড:</b>\n"
        "/today — আজকের ম্যাচ\n"
        "/tomorrow — আগামীকালের ম্যাচ\n"
        "/schedule — সম্পূর্ণ সূচি\n"
        "/stop — আনসাবস্ক্রাইব\n"
        "/stats — মোট সাবস্ক্রাইবার সংখ্যা"
    )
    await update.message.reply_html(text)
    logger.info(f"User subscribed: {uid} ({name}) | Total: {len(subscribers)}")

async def cmd_stop(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid  = update.effective_user.id
    name = update.effective_user.first_name or "বন্ধু"
    if uid in subscribers:
        subscribers.discard(uid)
        save_subscribers(subscribers)
        await update.message.reply_html(
            f"😢 <b>{name}</b>, আপনি আনসাবস্ক্রাইব করেছেন।\n"
            "আবার অ্যালার্ট পেতে /start দিন।"
        )
    else:
        await update.message.reply_html("আপনি এখনো সাবস্ক্রাইব করেননি। /start দিন।")

async def cmd_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        f"📊 <b>বট পরিসংখ্যান</b>\n\n"
        f"👥 মোট সাবস্ক্রাইবার: <b>{len(subscribers)} জন</b>"
    )

async def cmd_today(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    now = datetime.now(BD_TZ)
    matches = get_matches_for_date(now)
    await update.message.reply_html(
        format_daily_schedule(matches, f"আজ ({now.strftime('%d %B %Y')})")
    )

async def cmd_tomorrow(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    tom = datetime.now(BD_TZ) + timedelta(days=1)
    matches = get_matches_for_date(tom)
    await update.message.reply_html(
        format_daily_schedule(matches, f"আগামীকাল ({tom.strftime('%d %B %Y')})")
    )

async def cmd_schedule(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📋 <b>সম্পূর্ণ সূচি পাঠানো হচ্ছে…</b>")
    days: dict[str, list] = {}
    for m in MATCHES:
        bd_dt = utc_to_bd(datetime.strptime(m["utc"], "%Y-%m-%d %H:%M"))
        days.setdefault(bd_dt.strftime("%Y-%m-%d"), []).append({**m, "bd_dt": bd_dt})
    for key in sorted(days.keys()):
        ms = sorted(days[key], key=lambda x: x["bd_dt"])
        label = ms[0]["bd_dt"].strftime("%d %B %Y")
        await update.message.reply_html(format_daily_schedule(ms, label))
        await asyncio.sleep(0.4)

async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, ctx)

# ─── শিডিউল্ড জব ─────────────────────────────────────────────

async def job_daily_morning(ctx: ContextTypes.DEFAULT_TYPE):
    now = datetime.now(BD_TZ)
    matches = get_matches_for_date(now)
    text = format_daily_schedule(matches, f"আজ ({now.strftime('%d %B %Y')})")
    await broadcast(ctx.bot, text)
    logger.info(f"Daily schedule sent to {len(subscribers)} users.")

async def job_check_reminders(ctx: ContextTypes.DEFAULT_TYPE):
    if not subscribers:
        return
    now_utc = datetime.now(UTC_TZ).replace(second=0, microsecond=0)
    for m in MATCHES:
        utc_dt = UTC_TZ.localize(datetime.strptime(m["utc"], "%Y-%m-%d %H:%M"))
        diff   = (utc_dt - now_utc).total_seconds()

        # ১ ঘন্টা আগে রিমাইন্ডার
        if 59 * 60 <= diff <= 61 * 60:
            key = f"reminder:{m['utc']}"
            if key not in _sent_alerts:
                _sent_alerts.add(key)
                bd_dt = utc_to_bd(utc_dt)
                await broadcast(ctx.bot, format_reminder(m, bd_dt))
                logger.info(f"Reminder → {len(subscribers)} users: {m['home']} vs {m['away']}")

        # কিক-অফ অ্যালার্ট
        elif -60 <= diff <= 60:
            key = f"kickoff:{m['utc']}"
            if key not in _sent_alerts:
                _sent_alerts.add(key)
                bd_dt = utc_to_bd(utc_dt)
                await broadcast(ctx.bot, format_kickoff(m, bd_dt))
                logger.info(f"Kick-off → {len(subscribers)} users: {m['home']} vs {m['away']}")

# ─── মেইন ────────────────────────────────────────────────────

def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ TELEGRAM_BOT_TOKEN environment variable সেট করুন!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",    cmd_start))
    app.add_handler(CommandHandler("stop",     cmd_stop))
    app.add_handler(CommandHandler("stats",    cmd_stats))
    app.add_handler(CommandHandler("today",    cmd_today))
    app.add_handler(CommandHandler("tomorrow", cmd_tomorrow))
    app.add_handler(CommandHandler("schedule", cmd_schedule))
    app.add_handler(CommandHandler("help",     cmd_help))

    jq = app.job_queue

    # প্রতিদিন সকাল ৮:০০ AM BD (= UTC 02:00)
    import datetime as dt
    morning = dt.time(hour=2, minute=0, tzinfo=UTC_TZ)
    jq.run_daily(job_daily_morning, time=morning)

    # প্রতি মিনিটে রিমাইন্ডার চেক
    jq.run_repeating(job_check_reminders, interval=60, first=10)

    logger.info(f"🏆 FIFA 2026 Bot চালু! লোড হয়েছে {len(subscribers)} সাবস্ক্রাইবার।")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
