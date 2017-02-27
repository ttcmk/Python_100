"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

L = [1,2,3,4]

for i in L:
    for j in L:
        for p in L:
            if (i != j) and (i != p) and (j != p):
                print(i,j,p);
