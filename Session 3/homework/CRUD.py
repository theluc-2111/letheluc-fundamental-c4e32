Item = ['T-Shirt','Sweater']
while True:
    request = input('Welcome to our shop, what do you want (C, R, U, D)? : ')
    request = request.upper()
    if request == 'R':
        print('Our items: ',Item)
    elif request == 'C':
        new_item = input('Enter new item: ')
        Item.append(new_item)
        print('Our items: ',Item)
    elif request == 'U':
        update = int(input('Update position?: '))
        new_item = input('Enter new item: ')
        Item[update - 1] = new_item
        print('Our items: ',Item)
    elif request == 'D':
        del_pos = int(input('Delete position?: '))
        Item.pop(del_pos - 1)
        print('Our items: ',Item)
    else:
        print('Unknow request, please try again: ')