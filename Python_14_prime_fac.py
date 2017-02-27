"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""

def prime_factorization(n):
    s = str(n) + ' = '
    if n == 1:
        return s + ' 1 '
    while n != 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = int(n / i)
                if n == 1:
                    return s + ' '+ str(i) + ' '
                else:
                    s += ' ' + str(i) + ' *'
                    break

n = int(input("Enter a number: "))
s = prime_factorization(n)
print(s)
