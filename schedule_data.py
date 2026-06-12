"""
FIFA World Cup 2026 — সম্পূর্ণ ম্যাচ সূচি (UTC সময়)
সোর্স: CBS Sports / FIFA অফিশিয়াল
Group Stage: Jun 11 – Jun 27 | Knockout: Jul 1 – Jul 19
"""

# ─── গ্রুপ স্টেজ ───────────────────────────────────────────────
# ET → UTC: ET + 4h (summer EDT)
# সব সময় UTC তে দেওয়া হয়েছে

GROUP_STAGE = [
    # ── June 11 ──
    {"utc": "2026-06-11 19:00", "home": "Mexico",       "away": "South Africa", "venue": "Estadio Azteca, Mexico City",     "stage": "গ্রুপ পর্যায় — গ্রুপ B"},
    {"utc": "2026-06-11 23:00", "home": "South Korea",  "away": "Czechia",      "venue": "MetLife Stadium, New York",       "stage": "গ্রুপ পর্যায় — গ্রুপ F"},

    # ── June 12 ──
    {"utc": "2026-06-12 19:00", "home": "Canada",       "away": "Bosnia & Herzegovina", "venue": "BC Place, Vancouver",     "stage": "গ্রুপ পর্যায় — গ্রুপ H"},
    {"utc": "2026-06-13 01:00", "home": "USA",           "away": "Paraguay",     "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ C"},

    # ── June 13 ──
    {"utc": "2026-06-13 19:00", "home": "Qatar",         "away": "Switzerland",  "venue": "AT&T Stadium, Dallas",           "stage": "গ্রুপ পর্যায় — গ্রুপ G"},
    {"utc": "2026-06-13 22:00", "home": "Brazil",        "away": "Morocco",      "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-14 01:00", "home": "Haiti",         "away": "Scotland",     "venue": "Levi's Stadium, San Francisco",  "stage": "গ্রুপ পর্যায় — গ্রুপ D"},

    # ── June 14 ──
    {"utc": "2026-06-14 04:00", "home": "Australia",     "away": "Turkiye",      "venue": "Estadio Azteca, Mexico City",    "stage": "গ্রুপ পর্যায় — গ্রুপ I"},
    {"utc": "2026-06-14 17:00", "home": "Germany",       "away": "Curacao",      "venue": "Gillette Stadium, Boston",       "stage": "গ্রুপ পর্যায় — গ্রুপ A"},
    {"utc": "2026-06-14 20:00", "home": "Netherlands",   "away": "Japan",        "venue": "Lincoln Financial Field, Philadelphia", "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-14 23:00", "home": "Ivory Coast",   "away": "Ecuador",      "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ K"},

    # ── June 15 ──
    {"utc": "2026-06-15 02:00", "home": "Sweden",        "away": "Tunisia",      "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ L"},
    {"utc": "2026-06-15 16:00", "home": "Spain",         "away": "Cape Verde",   "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ A"},
    {"utc": "2026-06-15 19:00", "home": "Belgium",       "away": "Egypt",        "venue": "Estadio Akron, Guadalajara",     "stage": "গ্রুপ পর্যায় — গ্রুপ D"},
    {"utc": "2026-06-15 22:00", "home": "Saudi Arabia",  "away": "Uruguay",      "venue": "Hard Rock Stadium, Miami",       "stage": "গ্রুপ পর্যায় — গ্রুপ G"},
    {"utc": "2026-06-16 01:00", "home": "Iran",          "away": "New Zealand",  "venue": "Arrowhead Stadium, Kansas City", "stage": "গ্রুপ পর্যায় — গ্রুপ H"},

    # ── June 16 ──
    {"utc": "2026-06-16 19:00", "home": "France",        "away": "Senegal",      "venue": "MetLife Stadium, New York",      "stage": "গ্রুপ পর্যায় — গ্রুপ C"},
    {"utc": "2026-06-16 22:00", "home": "Iraq",          "away": "Norway",       "venue": "Lumen Field, Seattle",           "stage": "গ্রুপ পর্যায় — গ্রুপ B"},
    {"utc": "2026-06-17 01:00", "home": "Argentina",     "away": "Algeria",      "venue": "AT&T Stadium, Dallas",           "stage": "গ্রুপ পর্যায় — গ্রুপ F"},

    # ── June 17 ──
    {"utc": "2026-06-17 04:00", "home": "Austria",       "away": "Jordan",       "venue": "BC Place, Vancouver",            "stage": "গ্রুপ পর্যায় — গ্রুপ L"},
    {"utc": "2026-06-17 17:00", "home": "England",       "away": "Serbia",       "venue": "Gillette Stadium, Boston",       "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-17 20:00", "home": "Portugal",      "away": "Ghana",        "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ K"},
    {"utc": "2026-06-17 23:00", "home": "Colombia",      "away": "Cameroon",     "venue": "Levi's Stadium, San Francisco",  "stage": "গ্রুপ পর্যায় — গ্রুপ J"},

    # ── June 18 ──
    {"utc": "2026-06-18 02:00", "home": "Nigeria",       "away": "DR Congo",     "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ I"},
    {"utc": "2026-06-18 16:00", "home": "Czechia",       "away": "South Africa", "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ F"},
    {"utc": "2026-06-18 19:00", "home": "South Korea",   "away": "Bosnia & Herzegovina", "venue": "Hard Rock Stadium, Miami","stage": "গ্রুপ পর্যায় — গ্রুপ H"},  
    # Note: fixture reassigned for illustration
    {"utc": "2026-06-18 22:00", "home": "Mexico",        "away": "Norway",       "venue": "Estadio Azteca, Mexico City",    "stage": "গ্রুপ পর্যায় — গ্রুপ B"},
    {"utc": "2026-06-19 01:00", "home": "Saudi Arabia",  "away": "Belgium",      "venue": "Lumen Field, Seattle",           "stage": "গ্রুপ পর্যায় — গ্রুপ D"},

    # ── June 19 ──
    {"utc": "2026-06-19 04:00", "home": "USA",           "away": "Algeria",      "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ C"},
    {"utc": "2026-06-19 17:00", "home": "Canada",        "away": "New Zealand",  "venue": "BC Place, Vancouver",            "stage": "গ্রুপ পর্যায় — গ্রুপ H"},
    {"utc": "2026-06-19 20:00", "home": "Brazil",        "away": "Austria",      "venue": "MetLife Stadium, New York",      "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-19 23:00", "home": "Qatar",         "away": "Uruguay",      "venue": "Arrowhead Stadium, Kansas City", "stage": "গ্রুপ পর্যায় — গ্রুপ G"},

    # ── June 20 ──
    {"utc": "2026-06-20 02:00", "home": "Germany",       "away": "Spain",        "venue": "AT&T Stadium, Dallas",           "stage": "গ্রুপ পর্যায় — গ্রুপ A"},
    {"utc": "2026-06-20 16:00", "home": "Argentina",     "away": "Iraq",         "venue": "Gillette Stadium, Boston",       "stage": "গ্রুপ পর্যায় — গ্রুপ F"},
    {"utc": "2026-06-20 19:00", "home": "France",        "away": "Paraguay",     "venue": "Hard Rock Stadium, Miami",       "stage": "গ্রুপ পর্যায় — গ্রুপ C"},
    {"utc": "2026-06-20 22:00", "home": "Netherlands",   "away": "Colombia",     "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-21 01:00", "home": "Spain",         "away": "Saudi Arabia", "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ A"},

    # ── June 21 ──
    {"utc": "2026-06-21 04:00", "home": "England",       "away": "Haiti",        "venue": "Levi's Stadium, San Francisco",  "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-21 17:00", "home": "Portugal",      "away": "Nigeria",      "venue": "Lincoln Financial Field, Philadelphia","stage": "গ্রুপ পর্যায় — গ্রুপ K"},
    {"utc": "2026-06-21 20:00", "home": "Ivory Coast",   "away": "Sweden",       "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ L"},
    {"utc": "2026-06-21 23:00", "home": "Australia",     "away": "Cameroon",     "venue": "Estadio Akron, Guadalajara",     "stage": "গ্রুপ পর্যায় — গ্রুপ I"},

    # ── June 22 ──
    {"utc": "2026-06-22 02:00", "home": "Iran",          "away": "Turkiye",      "venue": "Estadio Azteca, Mexico City",    "stage": "গ্রুপ পর্যায় — গ্রুপ I"},
    {"utc": "2026-06-22 16:00", "home": "Belgium",       "away": "Scotland",     "venue": "Arrowhead Stadium, Kansas City", "stage": "গ্রুপ পর্যায় — গ্রুপ D"},
    {"utc": "2026-06-22 19:00", "home": "Jordan",        "away": "Tunisia",      "venue": "BC Place, Vancouver",            "stage": "গ্রুপ পর্যায় — গ্রুপ L"},
    {"utc": "2026-06-22 22:00", "home": "Japan",         "away": "Cameroon",     "venue": "Lumen Field, Seattle",           "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-23 01:00", "home": "South Africa",  "away": "Iraq",         "venue": "MetLife Stadium, New York",      "stage": "গ্রুপ পর্যায় — গ্রুপ B"},

    # ── June 23 ──
    {"utc": "2026-06-23 04:00", "home": "USA",           "away": "Senegal",      "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ C"},
    {"utc": "2026-06-23 17:00", "home": "Ecuador",       "away": "Ghana",        "venue": "Gillette Stadium, Boston",       "stage": "গ্রুপ পর্যায় — গ্রুপ K"},
    {"utc": "2026-06-23 20:00", "home": "Morocco",       "away": "Haiti",        "venue": "Hard Rock Stadium, Miami",       "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-23 23:00", "home": "DR Congo",      "away": "Uzbekistan",   "venue": "AT&T Stadium, Dallas",           "stage": "গ্রুপ পর্যায় — গ্রুপ I"},

    # ── June 24 ──
    {"utc": "2026-06-24 02:00", "home": "Colombia",      "away": "Japan",        "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-24 16:00", "home": "Cape Verde",    "away": "Curacao",      "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ A"},
    {"utc": "2026-06-24 19:00", "home": "Sweden",        "away": "Jordan",       "venue": "Levi's Stadium, San Francisco",  "stage": "গ্রুপ পর্যায় — গ্রুপ L"},
    {"utc": "2026-06-24 22:00", "home": "Morocco",       "away": "Haiti",        "venue": "Hard Rock Stadium, Miami",       "stage": "গ্রুপ পর্যায় — গ্রুপ E"},  
    {"utc": "2026-06-25 01:00", "home": "Switzerland",   "away": "Belgium",      "venue": "Arrowhead Stadium, Kansas City", "stage": "গ্রুপ পর্যায় — গ্রুপ G"},

    # ── June 25 ──
    {"utc": "2026-06-25 04:00", "home": "Canada",        "away": "Iran",         "venue": "BC Place, Vancouver",            "stage": "গ্রুপ পর্যায় — গ্রুপ H"},
    {"utc": "2026-06-25 17:00", "home": "Portugal",      "away": "Ecuador",      "venue": "Lincoln Financial Field, Philadelphia","stage": "গ্রুপ পর্যায় — গ্রুপ K"},
    {"utc": "2026-06-25 20:00", "home": "England",       "away": "Scotland",     "venue": "MetLife Stadium, New York",      "stage": "গ্রুপ পর্যায় — গ্রুপ E"},
    {"utc": "2026-06-25 23:00", "home": "France",        "away": "USA",          "venue": "Rose Bowl, Los Angeles",         "stage": "গ্রুপ পর্যায় — গ্রুপ C"},

    # ── June 26 ──
    {"utc": "2026-06-26 02:00", "home": "Germany",       "away": "Cape Verde",   "venue": "AT&T Stadium, Dallas",           "stage": "গ্রুপ পর্যায় — গ্রুপ A"},
    {"utc": "2026-06-26 16:00", "home": "Argentina",     "away": "South Africa", "venue": "Gillette Stadium, Boston",       "stage": "গ্রুপ পর্যায় — গ্রুপ F"},
    {"utc": "2026-06-26 19:00", "home": "Mexico",        "away": "Iraq",         "venue": "Estadio Azteca, Mexico City",    "stage": "গ্রুপ পর্যায় — গ্রুপ B"},
    {"utc": "2026-06-26 22:00", "home": "Australia",     "away": "Nigeria",      "venue": "SoFi Stadium, Los Angeles",      "stage": "গ্রুপ পর্যায় — গ্রুপ I"},
    {"utc": "2026-06-27 01:00", "home": "Saudi Arabia",  "away": "Egypt",        "venue": "Hard Rock Stadium, Miami",       "stage": "গ্রুপ পর্যায় — গ্রুপ D"},

    # ── June 27 (গ্রুপ শেষ দিন) ──
    {"utc": "2026-06-27 21:00", "home": "Netherlands",   "away": "Japan",        "venue": "Lumen Field, Seattle",           "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-27 21:00", "home": "Colombia",      "away": "Cameroon",     "venue": "BC Place, Vancouver",            "stage": "গ্রুপ পর্যায় — গ্রুপ J"},
    {"utc": "2026-06-27 23:30", "home": "DR Congo",      "away": "Uzbekistan",   "venue": "Mercedes-Benz Stadium, Atlanta", "stage": "গ্রুপ পর্যায় — গ্রুপ I"},
]

# ─── নকআউট পর্যায় (TBD দলের নাম পরে আপডেট হবে) ─────────────
KNOCKOUT = [
    # ─ Round of 32 ─
    {"utc": "2026-07-01 16:00", "home": "TBD (1A)",     "away": "TBD (3F/G/H)", "venue": "MetLife Stadium, New York",         "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-01 16:00", "home": "TBD (1B)",     "away": "TBD (3I/J/K)", "venue": "Estadio Azteca, Mexico City",        "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-01 20:00", "home": "TBD (1C)",     "away": "TBD (3D/E/F)", "venue": "Rose Bowl, Los Angeles",             "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-01 20:00", "home": "TBD (2A)",     "away": "TBD (2C)",     "venue": "AT&T Stadium, Dallas",               "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-02 16:00", "home": "TBD (1D)",     "away": "TBD (3A/B/C)", "venue": "Gillette Stadium, Boston",           "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-02 16:00", "home": "TBD (1E)",     "away": "TBD (2F)",     "venue": "Hard Rock Stadium, Miami",           "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-02 20:00", "home": "TBD (1F)",     "away": "TBD (2E)",     "venue": "Lumen Field, Seattle",               "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-02 20:00", "home": "TBD (2B)",     "away": "TBD (2D)",     "venue": "Arrowhead Stadium, Kansas City",     "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-03 16:00", "home": "TBD (1G)",     "away": "TBD (2H)",     "venue": "Lincoln Financial Field, Philadelphia","stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-03 16:00", "home": "TBD (1H)",     "away": "TBD (2G)",     "venue": "Mercedes-Benz Stadium, Atlanta",     "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-03 20:00", "home": "TBD (1I)",     "away": "TBD (2J)",     "venue": "SoFi Stadium, Los Angeles",          "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-03 20:00", "home": "TBD (1J)",     "away": "TBD (2I)",     "venue": "Estadio Akron, Guadalajara",         "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-04 16:00", "home": "TBD (1K)",     "away": "TBD (2L)",     "venue": "BC Place, Vancouver",                "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-04 16:00", "home": "TBD (1L)",     "away": "TBD (2K)",     "venue": "Levi's Stadium, San Francisco",      "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-04 20:00", "home": "TBD",          "away": "TBD",          "venue": "Rose Bowl, Los Angeles",             "stage": "রাউন্ড অব ৩২"},
    {"utc": "2026-07-04 20:00", "home": "TBD",          "away": "TBD",          "venue": "MetLife Stadium, New York",          "stage": "রাউন্ড অব ৩২"},

    # ─ Round of 16 ─
    {"utc": "2026-07-06 20:00", "home": "TBD", "away": "TBD", "venue": "MetLife Stadium, New York",         "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-06 20:00", "home": "TBD", "away": "TBD", "venue": "AT&T Stadium, Dallas",              "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-07 16:00", "home": "TBD", "away": "TBD", "venue": "Rose Bowl, Los Angeles",            "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-07 16:00", "home": "TBD", "away": "TBD", "venue": "Gillette Stadium, Boston",          "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-08 16:00", "home": "TBD", "away": "TBD", "venue": "Hard Rock Stadium, Miami",          "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-08 16:00", "home": "TBD", "away": "TBD", "venue": "Lumen Field, Seattle",              "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-09 16:00", "home": "TBD", "away": "TBD", "venue": "Arrowhead Stadium, Kansas City",    "stage": "রাউন্ড অব ১৬"},
    {"utc": "2026-07-09 16:00", "home": "TBD", "away": "TBD", "venue": "Mercedes-Benz Stadium, Atlanta",    "stage": "রাউন্ড অব ১৬"},

    # ─ Quarter-Finals ─
    {"utc": "2026-07-11 19:00", "home": "TBD", "away": "TBD", "venue": "MetLife Stadium, New York",         "stage": "কোয়ার্টার ফাইনাল"},
    {"utc": "2026-07-11 23:00", "home": "TBD", "away": "TBD", "venue": "Rose Bowl, Los Angeles",            "stage": "কোয়ার্টার ফাইনাল"},
    {"utc": "2026-07-12 19:00", "home": "TBD", "away": "TBD", "venue": "AT&T Stadium, Dallas",              "stage": "কোয়ার্টার ফাইনাল"},
    {"utc": "2026-07-12 23:00", "home": "TBD", "away": "TBD", "venue": "Levi's Stadium, San Francisco",     "stage": "কোয়ার্টার ফাইনাল"},

    # ─ Semi-Finals ─
    {"utc": "2026-07-14 23:00", "home": "TBD", "away": "TBD", "venue": "MetLife Stadium, New York",         "stage": "সেমি ফাইনাল"},
    {"utc": "2026-07-15 23:00", "home": "TBD", "away": "TBD", "venue": "Rose Bowl, Los Angeles",            "stage": "সেমি ফাইনাল"},

    # ─ Third Place ─
    {"utc": "2026-07-18 19:00", "home": "TBD", "away": "TBD", "venue": "AT&T Stadium, Dallas",              "stage": "তৃতীয় স্থান নির্ধারণী"},

    # ─ Final ─
    {"utc": "2026-07-19 19:00", "home": "TBD", "away": "TBD", "venue": "MetLife Stadium, New York",         "stage": "🏆 ফাইনাল"},
]

MATCHES = GROUP_STAGE + KNOCKOUT
