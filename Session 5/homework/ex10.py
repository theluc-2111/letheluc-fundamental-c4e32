def get_even_list(l):
    ds = []
    for i in range(len(l)):
        if l[i]%2 == 0:
            ds.append(l[i])
    return ds
even_list = get_even_list([1, 2, 5, 9, -10, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")