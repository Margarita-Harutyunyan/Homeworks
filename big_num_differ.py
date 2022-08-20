#make a list from a number
def bignumber(n):
    lst = []
    rev = n[::-1]
    while len(rev) % 3 !=0:
        rev += '0'
    rev = rev[::-1]
    i = 3
    while len(rev) > 0:
        lst.append(rev[:i])
        rev = rev[i:]
    return lst

#find the difference between two numbers and return in list form
def bigdiffer():
    n = input('Enter 1st number: ')
    m = input('Enter 2nd number: ')
    if int(n) > int(m):
        lst1 = bignumber(n)
        lst2 = bignumber(m)
    else:
        lst1 = bignumber(m)
        lst2 = bignumber(n)
    lst = []
    while len(lst1) > 0 and len(lst2) > 0:  
            if lst1[-1] >= lst2[-1]:
                differ = int(lst1[-1]) - int(lst2[-1])
            if lst1[-1] < lst2[-1]:
                differ = 1000 + int(lst1[-1]) - int(lst2[-1])
                lst1[-2] = str(int(lst1[-2]) - 1) 
            lst.append(str(differ))
            lst1 = lst1[:-1]
            lst2 = lst2[:-1]
    while len(lst1) > 0:                    
        lst.append(lst1[-1])
        lst1 = lst1[:-1]
    while len(lst2) > 0:
        lst.append(lst2[-1])
        lst2 = lst2[:-1]
    lst = lst[::-1]
    string = ''.join(l for l in lst)
    res = bignumber(string)
    if int(n) > int(m):
        return res
    else:
        res[0] = '-' + res[0]
        return res
print(bigdiffer())
