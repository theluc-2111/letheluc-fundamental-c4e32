import json
import requests
import bs4

# Lấy html từ trang vne
data = requests.get('https://vnexpress.net/') 
html = data.content.decode()

# Tạo đối tượng soup để xử lý dữ liệu dạng html
soup = bs4.BeautifulSoup(html, "html.parser")
# Liệt kê các danh sách bài viết, là các thẻ article có thuộc 
# tính class = 'list_news', xem html để rõ hơn
ds_bai_viet = soup.find_all('article', {"class": "list_news"})

ket_qua = [] # Tạo list để chứa các bài viết
for v in ds_bai_viet:
    bai_viet = {} # Từng bài viết là các dic
    bai_viet['tieu_de'] = v.h4.text # lấy tiêu đề từng bài viết
    bai_viet['anh'] = v.div.a.img.attrs['src'] # lấy src của ảnh 
    ket_qua.append(bai_viet) # Thêm vào list

# Lưu list ket_qua ra file theo định dạng json
with open('result.json', 'wt', encoding='utf-8') as f: 
    f.write(json.dumps(ket_qua, ensure_ascii=False))

# In ra màn hình chỉ các tiêu đề các bài viết
for v in ket_qua:
    print(v['tieu_de'].strip())