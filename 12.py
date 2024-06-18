n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(1,i+2):
        print(f"{j}",end=" ")
    for k in range(0,2*int(n-i-1)):
        print(" ",end=" ")
    for l in range(i+1,0,-1):
        print(f"{l}",end=" ")
    print()