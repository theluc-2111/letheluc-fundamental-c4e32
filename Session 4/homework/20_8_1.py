alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string = input('Mời bạn nhập chuỗi: ')
string = string.lower()
dem_ky_tu = {}
for i in range(len(alphabet)):
    if string.count(alphabet[i]) != 0:
        dem_ky_tu[alphabet[i]] = string.count(alphabet[i])
for k,l in dem_ky_tu.items():
    print(k," ",l)