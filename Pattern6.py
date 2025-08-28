n=int(input("Enter the number:"))

for i in range(1,n+1):
    print("*",end="")
    for j in range(1,6-i):#range(n+1-i)
            print("_",end=" " )
    print("*",end="")
    print()