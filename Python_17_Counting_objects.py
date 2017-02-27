"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
isalpha()
isspace()
isdigit()
""" 

def Counting(s):
    l = list(s)
    number = 0
    letter = 0
    space = 0
    other = 0
    for i in l:
        if i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            number += 1
        else:
            other += 1
    print("number ---> %d, space ---> %d, letter ---> %d, others ---> %d" % (number,space,letter,other))

str = input("Enter a string: ")
Counting(str)
