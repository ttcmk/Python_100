"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return 1
    else: return 0


while(True):
    year = int(input("Enter Year: "))
    month = int(input("Enter Month: "))
    if month not in range(1,13):
        print("please enter a valid month (1 ~ 12)")
        continue
    day = int(input("Enter day: "))
    if month in [1,3,5,7,8,10,12]:
        if day > 31:
            print("please enter a valid day (1 ~ 31)")
            continue
    elif month in [4,6,9,11]:
        if day > 30:
            print("please enter a valid day (1 ~ 30)")
            continue
    else:
        if is_leap_year(year) == 1:
            if day > 29:
                print("please enter a valid day (1 ~ 29)")
                continue
        else:
            if day > 28:
                print("please enter a valid day (1 ~ 28)")
                continue
    break



raw_year = [0,31,59,90,120,151,181,212,243,273,304,334]
leap_year = [0,31]
leap_year += [i+1 for i in raw_year if i >31]

number = 0
if is_leap_year(year):
    number = day + leap_year[month-1]
    print("This day is the %dth day of %d" % (number,year))
else:
    number = day + raw_year[month-1]
    print("This day is the %dth day of %d" % (number,year))
