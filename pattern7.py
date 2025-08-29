n=int(input("Enter The Number : "))

for i in range(n):
    for j in range(n-i-1):
        print("_",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
