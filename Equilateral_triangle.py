'''Equilateral triangle'''
num  = int(input("Enter a number: "))
for i in range(0, num):
    for j in range(0, num-1):
        print(end=" ")
    num-=1
    for j in range(0, i+1):
        print("*", end=" ")
    print("\n")