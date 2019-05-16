bang_diem = [{'Tên':'Lê Văn A','Tuổi':'21','Địa chỉ':'Hà Nội','Toán':7,'Lý':8,'Hoá':9,'SDT':['0123456789','2323232331']},
{'Tên':'Trần Ngọc B','Tuổi':'22','Địa chỉ':'Hà Nam','Toán':6,'Lý':8,'Hoá':7,'SDT':['6271873361']},
{'Tên':'Nguyễn Đức C','Tuổi':'20','Địa chỉ':'Bắc Giang','Toán':10,'Lý':8,'Hoá':9,'SDT':['512873361']},
{'Tên':'Đặng Văn D','Tuổi':'21','Địa chỉ':'Bắc Ninh','Toán':9,'Lý':7,'Hoá':8,'SDT':['067834219','515123361']},
{'Tên':'Phạm Công E','Tuổi':'22','Địa chỉ':'Hà Tĩnh','Toán':10,'Lý':9,'Hoá':8,'SDT':['0124534219','86923361']}]

# tính điểm trung bình 3 môn:
for p in bang_diem:
    print(p['Tên'],'có điểm trung bình 3 môn là:',(p['Toán']+p['Lý']+p['Hoá'])/3)

# tìm sinh viên có điểm môn Toán cao nhất:
max_toan = 0
ten = []
for k in bang_diem:
    if k['Toán'] >= max_toan:
        if k['Toán'] > max_toan:
            ten.clear()
        max_toan = k['Toán']
        ten.append(k['Tên'])
print(*ten,sep=", ",end=" ")
print('đạt số điểm môn Toán cao nhất là:',max_toan) 

# Tìm sinh viên theo số điện thoại
sdt = input('Nhập số điện thoại cần tìm: ')
Ten = []
for i in bang_diem:
    if sdt in i['SDT']:
        Ten.append(i['Tên'])
if len(Ten) != 0:
    print('Số điện thoại này của sinh viên:',*Ten)
else:
    print('Không có sinh viên nào dùng số điện thoại này')