"""
将一个数组逆序输出。
"""

#easiest:
L = [1,2,3,4,5]
print(L[::-1])

#manual:
L = [1,2,3,4,5,6]
leng = len(L)
for i in range(int(leng/2)):
    tmp = L[i]
    L[i] = L[leng - 1 - i]
    L[leng - 1 - i] = tmp

print(L)
