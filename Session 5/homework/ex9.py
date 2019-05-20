def get_even_list(l):
    ds = []
    for i in range(len(l)):
        if l[i]%2 == 0:
            ds.append(l[i])
    print(ds)
a = [1,2,3,4,5]
get_even_list(a)
