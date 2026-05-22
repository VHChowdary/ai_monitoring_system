# monitor.py - The main file. Runs everything together.

import time
import schedule
from fetcher   import fetch_prices
from validator import validate_prices
from db_logger import init_db, log_results
from reporter  import generate_report

def run_monitor():
    print("\n🔄 Starting monitoring cycle...")

    # Step 1 - Fetch live data from API
    data = fetch_prices()

    if data is None:
        print("  Skipping cycle - no data received.")
        return

    # Step 2 - Validate the data
    results = validate_prices(data)

    # Step 3 - Log results to CSV
    log_results(results)

    # Step 4 - Generate report
    generate_report()

def main():
    print("="*55)
    print("   🚀 AI MONITORING SYSTEM - STARTING UP")
    print("="*55)

    # Setup database (CSV file)
    init_db()

    # Run once immediately
    run_monitor()

    # Then run every 60 seconds automatically
    schedule.every(60).seconds.do(run_monitor)

    print("\n⏰ Scheduler active - checking every 60 seconds")
    print("   Press Ctrl+C to stop\n")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()