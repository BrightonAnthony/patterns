n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print()
