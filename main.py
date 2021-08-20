import requests

TICKER_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol='

def get_latest_crypto_price(crypto):
    response = requests.get(TICKER_API_URL + crypto)
    response_json = response.json()
    price = float(response_json["price"])
    return price


# crytpto = "BTCUsDT"
# get_latest_crypto_price(crytpto.upper())

