# persion = [["Nguyễn Văn A",21,"Hà Nội"],["Lê Văn B",23,"Phú Thọ"],["Trần Ngọc C",22,"Nghệ An"]]
# print(persion[2][1])

# person = {'name':"abc",'tuoi':21}
# # if 'a'in person:
# #     print(person['a'])
# print(person.get('a','khong co'))

# dic = {'mouse':'con chuột','keyboard':'bàn phím','monitor':'màn hình'}
# while True:
#     tra_cuu = input('nhập từ cần tra cứu: ')
#     tra_cuu = tra_cuu.lower()
#     # if tra_cuu == "":
#     #     break
#     if len(tra_cuu)==0:
#         break
#     if tra_cuu in dic:
#         print('Nghĩa của từ là:',dic[tra_cuu])
#     else:
#         print('Từ này không có trong từ điển')
# for k,v in dic.items():
#         print(k,":",v)


# person = [{'sdt':['0123456789','12351263461237'],'name':'luc','age':21,'address':'hà nội'},
# {'sdt':['12345'],'name':'tran thi hue','age':22,'address':'hà tĩnh'}]
# # first = person[0]
# number = first['sdt']
# second_phone = number[1]
# print(second_phone)

# sdt = '12345'
# for p in person:
#     if sdt in p['sdt']:
#         print(p['name'].split(' ')[-1])
letter_counts = {}
data = input("Enter a sentence: ")  # ask user to enter a sentence

for letter in data:
    if letter != " ":
        letter = letter.lower()     # transform all letters to the same case
        letter_counts[letter] = letter_counts.get(letter,0)+1 
        # count the number of each letter in the sentence

# sort the letters in alphabetical order. 
letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)