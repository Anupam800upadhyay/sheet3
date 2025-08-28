n=int(input("Enter the number:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1) or (j==n):
            print("*",end="")
        else:
            print("_",end=" " )
    print()

# Pattern4.py

# rows = 5
# for i in range(rows):
#     print("#", end=" ")
#     print("*", end=" ")
    
#     if i == 0 or i == rows - 1:
#         print(" " * 7, end="")  # 7 spaces to match the middle width
#     else:
#         print("- " * 3, end="")  # 3 dashes with spaces
    
#     print("*")  # End with a star