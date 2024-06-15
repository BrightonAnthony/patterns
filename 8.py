n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range((2*n-1)-2*i,0,-1):
        print("*",end=" ")
    print()