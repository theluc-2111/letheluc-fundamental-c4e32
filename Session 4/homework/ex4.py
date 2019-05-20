goi_cau_hoi = [{'question':'If x = 8, then what is the value of 4*(x+3)?','choice':{1:35,2:36,3:40,4:44},'answer':4},
{'question':'Estimate this answer (exact calculation not needed)\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?',
'choice':{1:'About 55',2:'About 65',3:'About 75',4:'About 85'},'answer':4},
{'question':'1000+1000=?','choice':{1:200,2:2500,3:2000,4:1400},'answer':3}]
so_cau_dung = 0
for i in range(len(goi_cau_hoi)):
    bo_cau_hoi = goi_cau_hoi[i]
    phuong_an = bo_cau_hoi['choice']
    print('Question',i+1,":",bo_cau_hoi['question'])
    for k,l in phuong_an.items():
        print(k,'.',l)
    your_choice = int(input('Your choice: '))
    if your_choice == bo_cau_hoi['answer']:
        print("Bingo. That's great!")
        so_cau_dung += 1
    else:
        print("You're wrong.The answer of this question is",phuong_an[bo_cau_hoi['answer']],
        '=> so the right choice must be:',bo_cau_hoi['answer'])
print("It's finished. You correctly answer",so_cau_dung,'out of',len(goi_cau_hoi),'questions')