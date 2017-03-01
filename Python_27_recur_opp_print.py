"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""

def opp_print(L):
    n = len(L)
    if n == 1:
        print(L[n-1])
    else:
        l = L[:-1]
        p = L[-1]
        print(p)
        opp_print(l)


L = 'acdfsfe'
#L = [1,2,3,4,5]
opp_print(L)
