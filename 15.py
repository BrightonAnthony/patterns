n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(ord("A"),ord("A")+n-i):
        print(chr(j),end=" ")
    print()