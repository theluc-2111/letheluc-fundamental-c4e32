prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock = {"apple": 0,"banana": 6,"pear": 15,"orange": 32}
# match price, stock:
for k in prices:
    print(k)
    print("price:",prices[k])
    print("stock:",stock[k])
# sum money:
total = 0
for i in prices:
    total = total + prices[i] * stock [i]
print('Tổng số tiền thu được là:',total)
