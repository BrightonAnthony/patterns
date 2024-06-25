n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(ord("A")+n-i-1,ord("A")+n):
        print(chr(j),end=" ")
    print("")