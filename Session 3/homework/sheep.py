sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Luc and these are my ship sizes: ")
print(sizes)
print("Now my biggest sheep has size",max(sizes),"let's shear it")
sizes[sizes.index(max(sizes))] = 8
print("After shearing, here is my flock")
print(sizes)
for j in range(4):
    print("MONTH",j+1)  
    for i in range(len(sizes)):
        sizes[i] = sizes[i] + 50
    print("1 month has passed, now here is my flock")
    print(sizes)  
    print("My flock has size in total:",sum(sizes))
    print("i would get",sum(sizes),"* 2$ =",sum(sizes)*2,"$") 
    print("Now my biggest sheep has size",max(sizes),"let's shear it")
    sizes[sizes.index(max(sizes))] = 8
    print("After shearing, here is my flock")
    print(sizes)
    print()
    print()
