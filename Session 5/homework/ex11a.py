def is_inside(toa_do,info_hinh):
    # toa_do = [x,y]
    # info_hinh = [a,b,ngang,doc]
    if info_hinh[0] <= toa_do[0] <= info_hinh[0] + info_hinh[2] and info_hinh[1] <= toa_do[1] <= info_hinh[1] + info_hinh[3]:
        return True
    else:
        return False
x = int(input('Nhập toạ độ trục x của điểm cần kiểm tra: '))
y = int(input('Nhập toạ độ trục y của điểm cần kiểm tra: '))
a = int(input('Nhập toạ độ trục x của hình: '))
b = int(input('Nhập toạ độ trục y của hình: '))
ngang = int(input('Nhập độ dài bề ngang: '))
doc = int(input('Nhập độ dài bề dọc: '))
print(is_inside([x,y],[a,b,ngang,doc]))