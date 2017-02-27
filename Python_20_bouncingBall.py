"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

def dropping(h,n):
    total = h
    bounce = h
    if n == 1:
        return {'total': total, 'bounce': bounce}
    for i in range (1,n):
        bounce = bounce / 2
        total = total + bounce * 2
    bounce /= 2
    return {'total': total, 'bounce': bounce}

h = 100
n = 10
D = dropping(h,n)
print("total is %f, the %dth time will bounce %f" % (D['total'], n, D['bounce']))
