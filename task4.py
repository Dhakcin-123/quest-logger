num = int(input("Enter an integer: "))

for i in range(1,num+1):
    if i%2 == 0:
        print(f"{i} : even")
    else:
        print(f"{i} : odd")