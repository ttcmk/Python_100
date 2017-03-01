"""
利用递归方法求5!
"""

def recur_factorial(n):
    total = 0
    if n == 1:
        total = 1
    else:
        total = n * recur_factorial(n-1)
    return total

print(recur_factorial(5))
