# validator.py - Checks if the data looks normal or suspicious

from config import THRESHOLDS

def validate_prices(data):
    print("\n  Running validation checks...")

    results = []

    for coin, values in data.items():
        price      = values.get("usd", 0)
        change_24h = values.get("usd_24h_change", 0)
        threshold  = THRESHOLDS.get(coin, 5.0)

        if abs(change_24h) >= threshold:
            status = "ALERT"
        else:
            status = "OK"

        result = {
            "coin"      : coin,
            "price_usd" : price,
            "change_24h": round(change_24h, 2),
            "threshold" : threshold,
            "status"    : status
        }

        results.append(result)

        flag = "ALERT" if status == "ALERT" else "OK"
        print(f"  [{flag}]  {coin.upper()}")

    return results