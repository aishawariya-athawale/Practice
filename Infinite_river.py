'''Infinite River'''
num  = int(input("Enter a number: "))
while True:
    for j in range(0, num):
        print(" "*j, end="")
        print("*"*num)
    for j in range(1,num+1):
        print(" "*(num-j+1),end="")
        print("*"*num)