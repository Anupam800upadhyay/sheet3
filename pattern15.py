n=int(input("Enter the number: "))

x=1
y=1
while x<=n:
    y=1
    while y<=x:
        print("*",end="")
        y=y+1
    print()
    x=x+1
x=n-1
y=1
while x>=1:
    y=x
    while y>=1:
        print("*",end="")
        y=y-1
    print()
    x=x-1