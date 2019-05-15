# so_nguyen_to = []
# for num in range(2,101):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#     if prime:
#        so_nguyen_to.append(num)
# print('danh sach so nguyen to: ',so_nguyen_to)

list_prime = []

n = int(input("Nhap N:"))
a = n
i = 2

while a != 1:  
    if a % i == 0:
        list_prime.append(i)
        a = a/i
    else:
        i += 1

   
print(n,"=",end=" ")
print(*list_prime,sep="*")