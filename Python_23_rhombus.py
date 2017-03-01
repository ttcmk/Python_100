"""
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""
s = ''
for i in range(1,5):
    for j in range(4-i):
        s += ' '
    for k in range(2*i-1):
        s += '*'
    s += '\n'

for i in range(1,4):
    for j in range(i):
        s += ' '
    for k in range(7-2*i):
        s += '*'
    s += '\n'

print(s)
