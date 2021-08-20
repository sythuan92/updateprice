import pygsheets
from main import *
import requests
from datetime import datetime
import pytz

TICKER_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol='

#ngay cap nhat theo gio vn
utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
localDatetime = utcmoment.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
current_time = localDatetime.strftime("%H:%M:%S")
#ngay cap nhat

gc = pygsheets.authorize('code_secret_client_461521253547-k09ajmh69d56po66h27h884i8tvddfsj.apps.googleusercontent.com.json')
sh = gc.open('Giá Crypto ')
ws1 =sh.sheet1
row_number =2
col_number =9
col_gia=10
crytpto =0
price=0
ws1.update_value("J1", current_time)

def get_latest_crypto_price(crypto):
    response = requests.get(TICKER_API_URL + crypto)
    response_json = response.json()
    price = float(response_json["price"])
    return price

for i in range(1,ws1.rows):
    # cell_chua_ma= "%s%s" % (i_row, col_number)
    crytpto  =ws1.cell((row_number,col_number)).value
    cell_cap_nhat_gia = "%s%s" % ("J", row_number)
    row_number = row_number + 1
    abc= crytpto.upper()
    if abc != "NONE":
        price = get_latest_crypto_price(abc)
        ws1.update_value(cell_cap_nhat_gia, price)
    else:
        pass
