import oandapyV20
import oandapyV20.endpoints.pricing as pricing
import time

ACCOUNT_ID = "your_account_id"
ACCESS_TOKEN = "your_access_token"
INSTRUMENT = "EUR_USD"

client = oandapyV20.API(access_token=ACCESS_TOKEN, environment="practice")

def get_price():
    params = {"instruments": INSTRUMENT}
    r = pricing.PricingInfo(accountID=ACCOUNT_ID, params=params)
    client.request
(r)
    price = float(r.response["prices"][0]["bids"][0]["price"])
    return price

print("Bot started...")
while True:
    price = get_price()
    print("Price:", price)
    time.sleep(10)
