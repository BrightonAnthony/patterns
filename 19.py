n = int(input("Enter number of lines"))
#1 AND 2
for i in range(0,n):
    for j in range(i,n):
        print("*",end=" ")   
    for j in range(0,2*i):
        print(" ",end=" ")   
    for j in range(i,n):
        print("*",end=" ")
    print("")

#3 AND 4
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,2*(n-i-1)):
        print(" ",end=" ")   
    for j in range(0,i+1):
        print("*",end=" ")
    print("")