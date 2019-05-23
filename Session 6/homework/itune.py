import requests
import bs4
import pyexcel
data = requests.get('https://www.apple.com/itunes/charts/songs/')
html = data.content.decode()
soup = bs4.BeautifulSoup(html,"html.parser")
bxh_100 = list(soup.body.find_all('div',{'class':'section-content'})[-1].ul.find_all('li'))
dsach_bai_hat = []
for i in bxh_100:
    bai_hat = {}
    position = i.strong.text
    bai_hat['Rank'] = position[:len(position)-1]
    bai_hat['Song'] = i.h3.a.text
    bai_hat['Singer'] = i.h4.a.text
    dsach_bai_hat.append(bai_hat)
pyexcel.save_as(records=dsach_bai_hat, dest_file_name="Top_100.xlsx")