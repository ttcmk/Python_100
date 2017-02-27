"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)
"""

def adding(n,init):
    l = [init]
    tmp = init
    summ = 0
    s = str(init)
    for i in range(1,n):
        init = init * 10 + tmp
        l += [init]
        s += ' ' + ' + ' + str(init)
    for number in l:
        summ += number
    return s + ' ' + ' = ' + str(summ)

str = adding(5,2)
print(str)
