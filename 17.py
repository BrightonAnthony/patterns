n = int(input("Enter number of lines"))
for i in range(0,n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(ord("A"),ord("A")+i+1):
        print(chr(k),end=" ")

    for k in range(ord("A")+i-1,ord("A")-1,-1):
        print(chr(k),end=" ")
    print("")


# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(0,2*i+1):
#         print(chr(ord("A")+k),end=" ")
#     print("")