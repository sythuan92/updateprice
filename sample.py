# filename='userpass.xlsx'
# col_name_acc = "A"
# col_name_pass = "B"
# col_name_status = "C"
# tong = 10
#
# for i_row in range(10,66):
#     cell_name_acc = "%s%s" % (col_name_acc, i_row)
#     cell_name_pass = "%s%s" % (col_name_pass, i_row)
#     cell_name_status = "%s%s" % (col_name_status, i_row)
#
#     account = get_value_excel(filename, cell_name_acc)
#     password = get_value_excel(filename, cell_name_pass)
#     status =get_value_excel(filename,cell_name_status)
#     print('current account', account)
#     print('current password', password)

# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Gio hien tai =", current_time)

from datetime import timezone
from datetime import datetime
import pytz

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

localDatetime = utcmoment.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))

print(localDatetime.strftime("%H:%M:%S"))