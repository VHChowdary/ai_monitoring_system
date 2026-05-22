# db_logger.py - Saves results to a CSV file (acts as our database)

import csv
import os
from datetime import datetime

LOG_CSV = "logs/price_log.csv"

# Column headers for our CSV "database"
HEADERS = ["timestamp", "coin", "price_usd", "change_24h", "threshold", "status"]

def init_db():
    # Create the CSV file with headers if it doesn't exist yet
    if not os.path.exists(LOG_CSV):
        with open(LOG_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
        print("  Database (CSV) created successfully!")
    else:
        print("  Database (CSV) already exists, appending...")

def log_results(results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_CSV, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)

        for result in results:
            row = {
                "timestamp" : timestamp,
                "coin"      : result["coin"],
                "price_usd" : result["price_usd"],
                "change_24h": result["change_24h"],
                "threshold" : result["threshold"],
                "status"    : result["status"]
            }
            writer.writerow(row)

    alerts = [r for r in results if r["status"] == "ALERT"]
    print(f"  Logged {len(results)} records | "
          f"{len(alerts)} alert(s) detected")