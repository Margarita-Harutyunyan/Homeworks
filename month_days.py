#Program to find how many days there are in a month

def month_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30 
    while month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
