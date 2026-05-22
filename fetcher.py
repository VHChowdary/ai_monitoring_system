# fetcher.py - Calls the live API and returns data

import requests
from datetime import datetime
from config import API_URL, API_PARAMS, LOG_FILE

def fetch_prices():
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Fetching live prices...")

    try:
        response = requests.get(API_URL, params=API_PARAMS, timeout=10)
        response.raise_for_status()  # crash loudly if API returns an error

        data = response.json()
        print("  Data fetched successfully!")
        return data

    except requests.exceptions.ConnectionError:
        print("  ERROR: No internet connection.")
        return None

    except requests.exceptions.Timeout:
        print("  ERROR: API took too long to respond.")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"  ERROR: API returned error - {e}")
        return None