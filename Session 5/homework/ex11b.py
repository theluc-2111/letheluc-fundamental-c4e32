def is_inside(toa_do,info_hinh):
    if info_hinh[0] <= toa_do[0] <= info_hinh[0] + info_hinh[2] and info_hinh[1] <= toa_do[1] <= info_hinh[1] + info_hinh[3]:
        return True
    else:
        return False
inside = is_inside([200,150],[140, 60,100,200])
if inside == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")