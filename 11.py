n = int(input("Enter number of lines"))
for i in range(0,n):
    if (i % 2 == 0): s = 1
    else : s = 0
    for j in range(0,i+1):
        print(f"{s}",end=" ")
        s = 1-s
    print()