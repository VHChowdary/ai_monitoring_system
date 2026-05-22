# config.py - All settings in one place

# API we are monitoring (Crypto prices - no API key needed, 100% free)
API_URL = "https://api.coingecko.com/api/v3/simple/price"
API_PARAMS = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

# Validation rules - flag alert if price change exceeds these %
THRESHOLDS = {
    "bitcoin":  5.0,   # flag if BTC moves more than 5% in 24hr
    "ethereum": 7.0,   # flag if ETH moves more than 7%
    "solana":   10.0   # flag if SOL moves more than 10%
}

# Database settings (we'll set these up later)
DB_HOST     = "localhost"
DB_USER     = "root"
DB_PASSWORD = ""       # you'll fill this from .env
DB_NAME     = "ai_monitoring"

# Report settings
LOG_FILE    = "logs/monitor.log"
REPORT_FILE = "reports/summary.txt"