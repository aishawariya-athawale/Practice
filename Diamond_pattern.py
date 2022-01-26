'''Diamond Pattern'''
num  = int(input("Enter a number: "))

for j in range(1, num+1):
    print(" "*(num-j),end=" ")
    print("* "*(j))
for j in range(1, num+1):
    print(" "*j,end=" ")
    print("* "*(num-j))