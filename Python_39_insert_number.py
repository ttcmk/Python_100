"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
"""

L = [1,3,5,7,9]
l = []
input = int(input("Enter a number: "))

if input > L[-1]:
    L.append(input)
    print(L)
else:
    for i in range(len(L)):
        if (input > L[i]) and (input <= L[i+1]):
            l.append(L[i])
            l.append(input)
        else:
            l.append(L[i])
    print(l)
