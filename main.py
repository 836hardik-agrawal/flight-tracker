from flight_checker import get_flight_price
from notifier import send_telegram_notification

def main():
    origin = "BLR"
    destination = "DEL"
    departure_date = "2025-10-17"
    return_date = None  # Or "2025-09-25" for roundtrip
    target_price = 9500  # INR or USD based on your request

    price = get_flight_price(origin, destination, departure_date)

    if price:
        print(f"Flight Price: ₹{price}")
        if price < target_price:
            message = f"✈️ *Price Alert!* Flight from {origin} to {destination} on {departure_date} is now ₹{price}!"
            send_telegram_notification(message)
    else:
        print("Could not fetch price. API error or no data.")

if __name__ == "__main__":
    from datetime import datetime
    with open("log_from_scheduler.txt", "a") as f:
        f.write(f"Task ran at {datetime.now()}\n")
    main()
