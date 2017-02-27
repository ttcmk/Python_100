"""
斐波那契数列（Fibonacci sequence）
"""

def fib(n):
    F = [0,1]
    # F += [(F(i-2) + F(i-1)) for i in range(2,10)]
    if(n == 1):
        F = [0]
    if(n > 2):
        for i in range(2,n+1):
            nextN = int(F[i-2]) + int(F[i-1])
            F += [nextN]
    print(F)


n = int(input("Please Enter a number: "))
fib(n)
