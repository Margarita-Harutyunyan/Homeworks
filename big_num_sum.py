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

#find the sum of two numbers and return in list form
def bigsum():
    n = input('Enter 1st number: ')
    m = input('Enter 2nd number: ')
    lst1 = bignumber(n)
    lst2 = bignumber(m)
    lst = []
    while len(lst1) > 0 and len(lst2) > 0:              
        sum = int(lst1[-1]) + int(lst2[-1])
        lst.append(str(sum))
        lst1 = lst1[:-1]
        lst2 = lst2[:-1]
    while len(lst1) > 0:                    
        lst.append(lst1[-1])
        lst1 = lst1[:-1]
    while len(lst2) > 0:
        lst.append(lst2[-1])
        lst2 = lst2[:-1]
    for k in range(len(lst) - 1):
        if len(lst[k]) == 4:
            lst[k + 1] = str(int(lst[k + 1]) + 1)
            lst[k] = str(int(lst[k]) - 1000)
    lst = lst[::-1]
    string = ''.join(l for l in lst)
    return bignumber(string)
print(bigsum())
