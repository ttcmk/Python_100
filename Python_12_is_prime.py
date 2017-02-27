"""
判断输入是否为素数
"""

import math
def is_primeNmuber(n):
    flag = 0
    if(n == 2):
        print("2 is a prime number")
        return
    if(n == 1):
        print("1 is a prime number")
        return
    sqr = int(math.sqrt(n))
    for i in range(2,sqr+1):
        if n % i == 0:
            print("%d is not a prime number" % n)
            flag = 1
            break
    if flag == 0:
        print("%d is a prime number" % n)

number = int(input("Enter a positive number: "))
is_primeNmuber(number)
