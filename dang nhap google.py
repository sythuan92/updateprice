import pygsheets
from main import *
import requests
from datetime import datetime

TICKER_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol='

#ngay cap nhat
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

gc = pygsheets.authorize('code_secret_client_727886963174-amadjmq92p8ahi4iefctmmnb5p8u7sc9.apps.googleusercontent.com.json')
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
    print(abc)
    print(cell_cap_nhat_gia)
    if abc != "NONE":
        price = get_latest_crypto_price(abc)
        print(price)
        ws1.update_value(cell_cap_nhat_gia, price)
    else:
        pass
#
#
# import pygsheets
# from main import *
# import threading
# from time import sleep
# from datetime import datetime
# #ngay cap nhat
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# #soluong
# thread_count =5
# #dang nhap gooogle
# gc = pygsheets.authorize('code_secret_client_727886963174-amadjmq92p8ahi4iefctmmnb5p8u7sc9.apps.googleusercontent.com.json')
# sh = gc.open('Giá Crypto ')
# ws1 =sh.sheet1
# #khai bao bien
# row_number =2
# col_number =9
# col_gia=10
# crytpto =0
# price=0
# macry=[]
# cellgiacry=[]
# giacry=[]
# giacry2 =[1]
# #cap nhat thoi gian cap nhat
# ws1.update_value("J1", current_time)
# #chia luong
# def chia_mang(thread_step):
#     for i in range(thread_step, len(macry),thread_count):
#         if macry[i] != "NONE":
#             price = get_latest_crypto_price(macry[i])
#             # print(macry[i])
#             # print(cellgiacry[i])
#             # print(price)
#             # print(price)
#             global giacry
#             giacry.append(price)
#             print(cellgiacry[i])
#             print(giacry[i])
#             # ws1.update_value(cellgiacry[i], giacry[i])
#             # sleep(1)
#         else:
#             pass
#
# #khai bao phan tu
# for i in range(1,ws1.rows):
#     # cell_chua_ma= "%s%s" % (i_row, col_number)
#     crytpto  =ws1.cell((row_number,col_number)).value
#     cell_cap_nhat_gia = "%s%s" % ("J", row_number)
#     row_number = row_number + 1
#     abc= crytpto.upper()
#     macry.append(abc)
#     cellgiacry.append(cell_cap_nhat_gia)
# # print(macry)
# # print(cellgiacry)
#
# #chia luong
# for i in range(thread_count):
#     new_thread = threading.Thread(target=chia_mang, args=(i,))
#     new_thread.start()
#
# # print(cellgiacry)
# # print(giacry2)
#
#
# # for i in range(2,ws1.rows):
# #     print(cellgiacry[i])
# #     print(giacry[i])
# #     # ws1.update_value(cellgiacry[i], giacry[i])
