# def say_hi():
#     print('hi')
# say_hi()
# say_hi()


# def add_two_number(a,b):
#     # a = int(input('nhap so thu nhat: '))
#     # b = int(input('nhap so thu hai: '))
#     print('Tong hai so la:',a+b)
#     return a+b
# a = 50
# b = 7
# c = 10
# tong1 = add_two_number(a,b)
# tong2 = add_two_number(tong1,c)
# print('Tong 3 so:',tong2)


# def abs_of_number(a):
#     if a>0:
#         return a
#         print('tri tuyet doi la:',a)
#     else:
#         return -a
#         print('tri tuy doi la:',a)
#     print('tri tuy doi la:',a)    
# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)


def evaluate(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
# x = evaluate(1,3,'-')
# print('x có giá trị là:',x)
def eval_expression(s):
    a = int(s[0])
    b = int(s[2])
    c = s[1]
    return evaluate(a,b,c)
while True:
    s = input('nhap bieu thuc:')
    print(eval_expression(s))

# n = 9
# cach 1
# uoc = []
# for v in range(2,n):
#     if n%v == 0:
#         uoc.append(v)
# if len(uoc) == 0:
#     print('đây là số nguyên tố')
# else:
#     print('đây không phải là số nguyên tố')

# cach 2 
# la_so_nguyen_to = True
# for v in range (2,n):
#     if n%v == 0:
#         la_so_nguyen_to = False
# if la_so_nguyen_to:
#     print('đây là số nguyên tố')
# else:
#     print('không phải số nguyên tố')        

# ds = []
# def la_so_nguyen_to(m):
#     for v in range(2,m):
#         if m%v == 0:
#             return False
#     return True
# # if la_so_nguyen_to(113):  
# #     print('đây là số nguyên tố')
# # else:
# #     print('đây không phải số nguyên tố') 
# for k in range(2,10000):
#     if la_so_nguyen_to(k):
#         ds.append(k)
# print(ds)