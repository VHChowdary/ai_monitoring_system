# reporter.py - Reads the CSV log and prints a summary report

import csv
import os
from datetime import datetime
from tabulate import tabulate
from db_logger import LOG_CSV
from config import REPORT_FILE

def generate_report():
    print("\n" + "="*55)
    print("         AI MONITORING SYSTEM - SUMMARY REPORT")
    print("="*55)

    # Check if any data exists yet
    if not os.path.exists(LOG_CSV):
        print("  No data logged yet. Run the monitor first!")
        return

    # Read all rows from CSV
    rows = []
    with open(LOG_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        print("  CSV exists but has no data yet.")
        return

    # Basic stats
    total     = len(rows)
    alerts    = [r for r in rows if r["status"] == "ALERT"]
    oks       = [r for r in rows if r["status"] == "OK"]
    last_time = rows[-1]["timestamp"]

    print(f"\n  Total checks logged : {total}")
    print(f"  OK records          : {len(oks)}")
    print(f"  ALERTS raised       : {len(alerts)}")
    print(f"  Last checked        : {last_time}")

    # Show last 10 records as a table
    print("\n--- LATEST RECORDS ---")
    last_10 = rows[-10:]
    table_data = [
        [r["timestamp"], r["coin"].upper(),
         f"${float(r['price_usd']):,.2f}",
         f"{float(r['change_24h']):+.2f}%",
         r["status"]]
        for r in last_10
    ]
    print(tabulate(table_data,
                   headers=["Time", "Coin", "Price", "24h Change", "Status"],
                   tablefmt="rounded_outline"))

    # Show alerts separately if any
    if alerts:
        print("\n--- 🚨 ALERTS RAISED ---")
        alert_data = [
            [r["timestamp"], r["coin"].upper(),
             f"${float(r['price_usd']):,.2f}",
             f"{float(r['change_24h']):+.2f}%"]
            for r in alerts
        ]
        print(tabulate(alert_data,
                       headers=["Time", "Coin", "Price", "24h Change"],
                       tablefmt="rounded_outline"))

    # Save report to file
    with open(REPORT_FILE, "w") as f:
        f.write(f"Report generated: {datetime.now()}\n")
        f.write(f"Total checks: {total} | OKs: {len(oks)} | Alerts: {len(alerts)}\n")

    print(f"\n  Report saved to → {REPORT_FILE}")
    print("="*55 + "\n")