choice = {1:35,2:36,3:40,4:44}
answer = 4
print('If x = 8, then what is the value of 4(x+3)')
for k,i in choice.items():
    print(k,'. ',i)
your_choice = int(input('Your choice: '))
if your_choice == answer:
    print('hura')
else:
    print(':(')

