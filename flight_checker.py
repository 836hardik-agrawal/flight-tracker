import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FLIGHTAPI_KEY")

def get_flight_price(origin, destination, departure_date):
    # Basic roundtrip or oneway request
    base_url = f"https://api.flightapi.io/roundtrip/{API_KEY}/{origin}/{destination}/{departure_date}/1/0/0/Economy/USD"
    
    # if not return_date:
    resp = requests.get(f"https://api.flightapi.io/onewaytrip/{API_KEY}/{origin}/{destination}/{departure_date}/1/0/0/Economy/INR")
    # resp = requests.get('https://api.flightapi.io/onewaytrip/686d1ebf4e30db35ef995e50/BLR/DEL/2025-10-20/1/0/0/Economy/INR')
    # print (resp.json())
    
    # resp = requests.get('https://api.flightapi.io/onewaytrip/686d1ebf4e30db35ef995e50/BLR/DEL/2025-10-20/1/0/0/Economy/INR')
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
    
# if __name__ == "__main__":

#     # resp = requests.get('https://api.flightapi.io/onewaytrip/686d1ebf4e30db35ef995e50/BLR/DEL/2025-10-20/1/0/0/Economy/INR')
#     # print (resp.json())
    
#     resp = requests.get(f"https://api.flightapi.io/onewaytrip/{API_KEY}/BLR/DEL/2025-10-20/1/0/0/Economy/INR")
#     if resp.status_code != 200:
#         print("API Error:", resp.text)
#         # return None

#     data = resp.json()
#     # print(data)

#     try:
#         length = len(data["itineraries"])
#         price = float('inf')
#         for i in data["itineraries"]:
#             if(price > i["cheapest_price"]["amount"]):
#                 price = i["cheapest_price"]["amount"]

#         # price = data["itineraries"][0]["cheapest_price"]["amount"]
#         print(price)
#     except (KeyError, IndexError):
#         print(None)
#         # return None
#     # get_flight_price()


