'''Concentric number square'''
num = int(input("enter a num:"))
k = 2*num-1

for i in range(0, (k//2)+1):
    for j in range(0, i):
        print(j+1 ,end= " " )
    for j in range(0, k-2*i):
        print(i+1, end=" ")
    m = i
    for j in range(1, i+1):
        print(m ,end= " ")
        m-=1
    print()

for i in range((k//2)-1,-1,-1):
    for j in range(0, i):
        print(j+1 ,end= " " )
    for j in range(0, k-2*i):
        print(i+1, end=" ")
    m= i
    for j in range(1, i+1):
        print(m ,end= " ")
        m-=1
    print()