n=int(input("ENTER THE NUMBER:"))

for i in range(n):
    for j in range(i):
        if(j%2==0):
            continue
        print(j,end="*")
    print()

