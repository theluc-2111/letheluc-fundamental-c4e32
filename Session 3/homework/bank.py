r = 6.5
Future_cash = cash = 21000000
for i in range(1,10):
    Future_cash = Future_cash*(1+r/100)
print("Sau 9 năm, số tiền tại ngân hàng là: ",Future_cash,"đồng")

nam = 0
while True:
    cash = cash*(1+r/100)
    nam += 1
    if cash >= 1200000000:
        break
print("Cần gửi tối thiểu",nam,"năm để mua nhà\nCụ thể, số tiền tại thời điểm ấy là: ",cash,"đồng")