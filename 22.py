n = int(input("Enter the number"))
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        top = i
        bottom = 2*n-2-i
        left = j
        right = 2*n-2-j
        s = min(min(top,bottom),min(left,right))
        print(n-s,end=" ")
    print("")


# only works for 3
# n = int(input("Enter the number"))
# for i in range(0,2*n-1):
#     for j in range(0,2*n-1):
#         top = i
#         bottom = 2*n-2-i
#         left = j
#         right = 2*n-2-j
#         s = max(max(top,bottom),max(left,right))
#         print(s-1,end=" ")
#     print("")