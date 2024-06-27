n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,2*(n-i-1)):
        print(" ",end=" ")   
    for j in range(0,i+1):
        print("*",end=" ")
    print("")

for i in range(0,n):
    for j in range(i+1,n):
        print("*",end=" ")   
    for j in range(0,2*(i+1)):
        print(" ",end=" ")   
    for j in range(i+1,n):
        print("*",end=" ")
    print("")