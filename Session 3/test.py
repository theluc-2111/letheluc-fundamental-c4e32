# for i in range(10):
#     print(i)
# print(i)

# tong = 0
# i = 1
# while tong < 2:
#     tong = tong + 1/i
#     i += 1
#     if tong >= 2:
#         break
#     print(tong)

# while False:
#     print('hi')

# n = 0
# while n < 10:
#     print("hi",n)
#     n += 1

# dem = 0
# while True:
#     print("hi",dem)
#     dem += 1
#     if dem >=3:
#         break
#     print('abc')
# print('end')
    
# dem = 0
# loop = True
# while loop:
#     print("hi",dem)
#     dem += 1
#     if dem >=3:
#         loop = False
#     print('abc')
# print('end')    

# for v in range(40):
#     if v>=4:
#         break
#     print('hi',v)

# password = input('Nhập pass: ')
# while len(password) <8:
#     print('Mời nhập lại: ',end ="")
#     password = input()

# while True:
#     pw = input('nhập pass: ')
#     if len(pw)>8:
#         break

# r = 6.5
# PV = 21000000
# for i in range(1,10):
#     PV = PV*(1+r/100)
# print(PV)

# r = 6.5
# PV = 21000000
# nam = 0
# while True:
#     PV = PV*(1+r/100)
#     nam += 1
#     if PV >= 1200000000:
#         break
# print(nam,PV)

n = int(input('nhập số phần tử: '))
ds = []
for i in range(n):
    so = input('nhập số thứ '+str(i)+': ')
    so = int(so)
    ds.append(so)
print('dãy số vừa nhập là: ')
print(ds)

# tong_so_chan = 0
# so_phan_tu_chan = 0
ds_chan = []
for v in ds:
    if v%2 == 0:
        # print(v)
        ds_chan.append(v)
print('các phần tử chẵn là: ',ds_chan)
        # tong_so_chan = tong_so_chan + v
        # so_phan_tu_chan += 1
# print('trung binh cong cac phan tu chan: ',tong_so_chan/so_phan_tu_chan)
print('tbc: ',sum(ds_chan)/len(ds_chan))
