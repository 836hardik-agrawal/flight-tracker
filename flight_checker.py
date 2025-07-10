import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FLIGHTAPI_KEY")

def get_flight_price(origin, destination, departure_date):
    # Basic roundtrip or oneway request
    
    
    # if not return_date:
    resp = requests.get(f"https://api.flightapi.io/onewaytrip/{API_KEY}/{origin}/{destination}/{departure_date}/1/0/0/Economy/INR")
    
    if resp.status_code != 200:
        print("API Error:", resp.text)
        return None

    data = resp.json()

    try:
        # length = len(data["itineraries"])
        price = float('inf')
        for i in data["itineraries"]:
            if(price > i["cheapest_price"]["amount"]):
                price = i["cheapest_price"]["amount"]

        # price = data["itineraries"][0]["cheapest_price"]["amount"]
        print(price)
        return price
       
    except (KeyError, IndexError):
        return None
 