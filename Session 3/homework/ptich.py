# n = int(input("Nhập N:"))
# while not 0 < n < 1000000:
#     n = int(input("Nhập lại N trong khoảng từ 0 đến 1000000:"))

# a = n
# tich = []
# while a != 1:
#     for i in range(2,n): 
#         if a % i == 0:
#             tich.append(i)
#             a = a/i
#             break
# print(n,"=",end=" ")
# print(*tich,sep="*")

n = int(input('Nhập số cần tính: '))
so_chia = 2
ls = []
while n != 1:
    if n%so_chia == 0:
        n = n/so_chia
        ls.append(so_chia)
    else:
        so_chia += 1
print(ls)