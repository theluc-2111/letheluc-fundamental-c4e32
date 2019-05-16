goi_cau_hoi = [{'question':'If x = 8, then what is the value of 4*(x+3)?','choice':{1:35,2:36,3:40,4:44},'answer':4},
{'question':'Estimate this answer (exact calculation not needed)\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?',
'choice':{1:'About 55',2:'About 65',3:'About 75',4:'About 85'},'answer':2}]
so_cau_dung = 0
for i in range(len(goi_cau_hoi)):
    bo_cau_hoi = goi_cau_hoi[i]
    phuong_an = bo_cau_hoi['choice']
    print(bo_cau_hoi['question'])
    for k,l in phuong_an.items():
        print(k,'.',l)
    your_choice = int(input('Your choice: '))
    if your_choice == bo_cau_hoi['answer']:
        print('Bingo')
        so_cau_dung += 1
    else:
        print(':(')
print('You correctly answer',so_cau_dung,'out of',len(goi_cau_hoi),'questions')