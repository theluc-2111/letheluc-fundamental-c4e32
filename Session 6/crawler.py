html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<title>Trang web của tôi</title>

<body>
<h1>Chào mừng đến với Techkids</h1>
<p id='data'>Xin chào</p>
<p>python</p>
<p>c#</p>
<p>java</p>

<div>
    <div data="tin_tuc" style="border-style: solid;">
        <a href='http://google.com'>Tự động hóa xét nghiệm, giảm chờ đợi cho người bệnh</a>
        <img src="https://icdn.dantri.com.vn/thumb_w/640/2019/04/09/y-te-2-1554803305875.png">
        <div>
            <p>Bệnh viện Chợ Rẫy vừa đưa hệ thống xét nghiệm tự động hóa hoàn toàn thứ 2 </p>
        </div>
    </div>
    <div data="tin_tuc" style="border-style: solid;">
        <a href='http://google.com'>Bất ngờ với những lợi ích sức khỏe khi ăn ớt</a>
        <img src="https://icdn.dantri.com.vn/thumb_w/640/2019/04/09/ot-1554816529826.jpg"/>
        <div>
            <p>Có rất nhiều lý do tốt để thêm ớt vào chế độ ăn và con số này tiếp tục tăng lên </p>
        </div>
    </div>
</div>

</body>

</html>
"""
 
import bs4
   
soup = bs4.BeautifulSoup(html,"html.parser")
  
print(soup.title.string)
print(soup.body.p)
print(soup.body.find_all('p')[-1])
for v in soup.find_all('p'):
    print(v.string)
print(list(soup.body.children))
for v in soup.body.children:
    print(v)
print(len(list(soup.body.children)))
print(list(soup.body.div.children))
bai_viet = list(soup.body.find_all('div',{'data':'tin_tuc'}))
for v in bai_viet:
    print(v.a.string)
    print(v.img.attrs['src'])
    print(v.div.string)

for v in soup.body.div.find('div'):
    print(v)
the_p = soup.body.p
print(the_p.attrs['id'])