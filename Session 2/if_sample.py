nam_sinh = int(input('nhap nam sinh: '))
tuoi = 2019 - nam_sinh + 1
print('baby') if tuoi <= 13 else print('teenager') if tuoi <= 18 else print('adult')