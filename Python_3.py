"""
一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
Within 0 ~ 10000
"""

import math

for i in range(100001):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))

    if (x ** 2 == (i + 100)) and (y ** 2 == (i + 268)):
        print(i)
