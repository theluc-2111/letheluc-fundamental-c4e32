import requests
import bs4
import pyexcel
data = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html = data.content.decode()
soup = bs4.BeautifulSoup(html,"html.parser")
Chi_tieu = list(soup.find('div',{'id':'divTableHeader'}).find_all('td',{'class':['b_r_c','h_t','h_t_tt']}))
Du_lieu = list(soup.find_all('tr',{'class':['r_item','r_item_a']}))
bctc = []
a = 1
hang={}
while a<=5:
    if a == 1:
        hang['Cột 1'] = 'Chỉ tiêu'
        a += 1
    else:
        hang['Cột '+str(a)] = Chi_tieu[a-1].text.strip()
        a += 1
        if a > 5:
            bctc.append(hang)
            break
for i in Du_lieu:
    du_lieu={}    
    info_hang = i.find_all('td',{'class':'b_r_c'})
    b=1
    while b<=5:
        du_lieu['Cột '+str(b)] = info_hang[b-1].text.strip()
        b+=1
        if b>5:
            bctc.append(du_lieu)
            break
pyexcel.save_as(records=bctc, dest_file_name="BCTC_Vinamilk.xlsx")