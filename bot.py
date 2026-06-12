#!/usr/bin/env python3
"""
🏆 FIFA World Cup 2026 Telegram Bot
- প্রতিদিন সকালে দৈনিক ম্যাচ সূচি পাঠায়
- প্রতিটি ম্যাচের ১ ঘন্টা আগে রিমাইন্ডার পাঠায়
- ম্যাচ শুরুর মুহূর্তে কিক-অফ অ্যালার্ট পাঠায়
- /today, /tomorrow, /schedule কমান্ড সাপোর্ট করে
"""

import os
import asyncio
import logging
from datetime import datetime, timedelta, timezone
import pytz
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from schedule_data import MATCHES

# ─── কনফিগারেশন ───────────────────────────────────────────────
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID",   "YOUR_CHAT_ID_HERE")

# বাংলাদেশ সময় (UTC+6)
BD_TZ   = pytz.timezone("Asia/Dhaka")
UTC_TZ  = pytz.utc

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── হেল্পার ──────────────────────────────────────────────────

def utc_to_bd(utc_dt: datetime) -> datetime:
    """UTC datetime → Bangladesh datetime"""
    if utc_dt.tzinfo is None:
        utc_dt = UTC_TZ.localize(utc_dt)
    return utc_dt.astimezone(BD_TZ)

def get_matches_for_date(date: datetime) -> list[dict]:
    """নির্দিষ্ট তারিখের ম্যাচ (BD টাইমজোন অনুযায়ী)"""
    target = date.strftime("%Y-%m-%d")
    result = []
    for m in MATCHES:
        utc_dt = datetime.strptime(m["utc"], "%Y-%m-%d %H:%M")
        bd_dt  = utc_to_bd(utc_dt)
        if bd_dt.strftime("%Y-%m-%d") == target:
            result.append({**m, "bd_dt": bd_dt})
    return sorted(result, key=lambda x: x["bd_dt"])

def format_daily_schedule(matches: list[dict], label: str) -> str:
    if not matches:
        return f"📅 <b>{label}</b>\n\nকোনো ম্যাচ নেই।"

    lines = [f"🏆 <b>FIFA বিশ্বকাপ ২০২৬ — {label}</b>\n"]
    for m in matches:
        bd = m["bd_dt"]
        time_str = bd.strftime("%I:%M %p")
        lines.append(
            f"⚽ <b>{m['home']} 🆚 {m['away']}</b>\n"
            f"   🕐 {time_str} (বাংলাদেশ সময়)\n"
            f"   🏟️ {m['venue']}\n"
            f"   📌 {m['stage']}\n"
        )
    lines.append("🔔 প্রতিটি ম্যাচের ১ ঘন্টা আগে রিমাইন্ডার + শুরুর মুহূর্তে 🚨 কিক-অফ অ্যালার্ট পাবেন!")
    return "\n".join(lines)

def format_reminder(match: dict, bd_dt: datetime) -> str:
    time_str = bd_dt.strftime("%I:%M %p")
    return (
        f"⏰ <b>ম্যাচ শুরু হতে ১ ঘন্টা বাকি!</b>\n\n"
        f"⚽ <b>{match['home']} 🆚 {match['away']}</b>\n"
        f"🕐 আজ রাত/সকাল {time_str} (বাংলাদেশ সময়)\n"
        f"🏟️ {match['venue']}\n"
        f"📌 {match['stage']}\n\n"
        f"📺 প্রস্তুত হয়ে যান! গো গো গো! 🎉"
    )

def format_kickoff_alert(match: dict, bd_dt: datetime) -> str:
    time_str = bd_dt.strftime("%I:%M %p")
    return (
        f"🚨🔴 <b>ম্যাচ এখনই শুরু হচ্ছে!</b> 🔴🚨\n\n"
        f"⚽ <b>{match['home']} 🆚 {match['away']}</b>\n"
        f"🕐 {time_str} (বাংলাদেশ সময়)\n"
        f"🏟️ {match['venue']}\n"
        f"📌 {match['stage']}\n\n"
        f"🎙️ বল গড়াচ্ছে — এখনই চ্যানেল খুলুন! 🏆🔥"
    )

# ─── কমান্ড হ্যান্ডলার ────────────────────────────────────────

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏆 <b>FIFA বিশ্বকাপ ২০২৬ -এ স্বাগতম!</b>\n\n"
       
        "<b>কমান্ডসমূহ:</b>\n"
        "/today — আজকের ম্যাচ\n"
        "/tomorrow — আগামীকালের ম্যাচ\n"
        "/schedule — সম্পূর্ণ সূচি (গ্রুপ পর্যায়)\n"
        "/help — সাহায্য"
    )
    await update.message.reply_html(text)

async def cmd_today(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    now     = datetime.now(BD_TZ)
    matches = get_matches_for_date(now)
    label   = f"আজ ({now.strftime('%d %B %Y')})"
    await update.message.reply_html(format_daily_schedule(matches, label))

async def cmd_tomorrow(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    tom     = datetime.now(BD_TZ) + timedelta(days=1)
    matches = get_matches_for_date(tom)
    label   = f"আগামীকাল ({tom.strftime('%d %B %Y')})"
    await update.message.reply_html(format_daily_schedule(matches, label))

async def cmd_schedule(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        "📋 <b>সম্পূর্ণ সূচি পাঠানো হচ্ছে…</b>\n"
        "(গ্রুপ পর্যায় ১১ জুন – ২৭ জুন ২০২৬)"
    )
    # তারিখ অনুযায়ী গ্রুপ করে পাঠাই
    days: dict[str, list] = {}
    for m in MATCHES:
        utc_dt = datetime.strptime(m["utc"], "%Y-%m-%d %H:%M")
        bd_dt  = utc_to_bd(utc_dt)
        key    = bd_dt.strftime("%Y-%m-%d")
        days.setdefault(key, []).append({**m, "bd_dt": bd_dt})

    for day_key in sorted(days.keys()):
        ms    = sorted(days[day_key], key=lambda x: x["bd_dt"])
        dt    = ms[0]["bd_dt"]
        label = dt.strftime("%d %B %Y")
        await update.message.reply_html(format_daily_schedule(ms, label))
        await asyncio.sleep(0.4)   # flood guard

async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, ctx)

# ─── শিডিউল্ড জব ─────────────────────────────────────────────

async def job_daily_morning(ctx: ContextTypes.DEFAULT_TYPE):
    """প্রতিদিন সকাল ৮টায় আজকের ম্যাচ পাঠায়"""
    now     = datetime.now(BD_TZ)
    matches = get_matches_for_date(now)
    label   = f"আজ ({now.strftime('%d %B %Y')})"
    text    = format_daily_schedule(matches, label)
    await ctx.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="HTML")
    logger.info("Daily morning schedule sent.")

async def job_check_reminders(ctx: ContextTypes.DEFAULT_TYPE):
    """প্রতি মিনিটে চেক করে:
    - ম্যাচের ঠিক ৬০ মিনিট আগে → রিমাইন্ডার
    - ম্যাচ শুরুর মুহূর্তে (০ মিনিট) → কিক-অফ অ্যালার্ট
    """
    now_utc = datetime.now(UTC_TZ).replace(second=0, microsecond=0)
    for m in MATCHES:
        utc_dt = UTC_TZ.localize(datetime.strptime(m["utc"], "%Y-%m-%d %H:%M"))
        diff   = (utc_dt - now_utc).total_seconds()

        # ১ ঘন্টা আগে রিমাইন্ডার (৫৯–৬১ মিনিটের উইন্ডো)
        if 59 * 60 <= diff <= 61 * 60:
            bd_dt = utc_to_bd(utc_dt)
            text  = format_reminder(m, bd_dt)
            await ctx.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="HTML")
            logger.info(f"1-hour reminder sent: {m['home']} vs {m['away']}")

        # কিক-অফ অ্যালার্ট (০ থেকে +১ মিনিটের উইন্ডো)
        elif -60 <= diff <= 60:
            bd_dt = utc_to_bd(utc_dt)
            text  = format_kickoff_alert(m, bd_dt)
            await ctx.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="HTML")
            logger.info(f"Kick-off alert sent: {m['home']} vs {m['away']}")

# ─── মেইন ────────────────────────────────────────────────────

def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ TELEGRAM_BOT_TOKEN environment variable সেট করুন!")
        return
    if CHAT_ID == "YOUR_CHAT_ID_HERE":
        print("❌ TELEGRAM_CHAT_ID environment variable সেট করুন!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # কমান্ড
    app.add_handler(CommandHandler("start",    cmd_start))
    app.add_handler(CommandHandler("today",    cmd_today))
    app.add_handler(CommandHandler("tomorrow", cmd_tomorrow))
    app.add_handler(CommandHandler("schedule", cmd_schedule))
    app.add_handler(CommandHandler("help",     cmd_help))

    # জব কিউ
    jq = app.job_queue

    # প্রতিদিন সকাল ৮:০০ AM BD টাইম (= UTC 02:00)
    morning_time = datetime.now(BD_TZ).replace(hour=8, minute=0, second=0, microsecond=0)
    if morning_time < datetime.now(BD_TZ):
        morning_time += timedelta(days=1)
    jq.run_daily(job_daily_morning, time=morning_time.timetz())

    # প্রতি মিনিটে রিমাইন্ডার চেক
    jq.run_repeating(job_check_reminders, interval=60, first=10)

    logger.info("🏆 FIFA 2026 Bot চালু হয়েছে!")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
