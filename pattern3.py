n=int(input("ENTER THE NUMBER:"))
for i in range(1,n):
    for j in range(1,7-i):
        print("*",end='')
    print()