n = int(input("Enter number of lines"))
s = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(f"{s}",end=" ")
        s = s+1
    print()