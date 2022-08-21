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

def bignummultiple():
    n = input('Enter 1st number: ')
    m = input('Enter 2nd number: ')
    if n[0] == '-':
        nn = n[1:]
        lst1 = bignumber(nn)
    else:
        lst1 = bignumber(n)
    if m[0] == '-':
        mm = m[1:]
        lst2 = bignumber(mm)
    else:
        lst2 = bignumber(m)
    lst = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            for k in range(len(lst2[j])):
                mult = int(lst2[j][k]) * int(lst1[i])
                lst.append(str(mult))
    zero = 10 ** (len(lst) - 1)
    sum = 0
    for num in range(len(lst)):
        lst[num] = str(int(lst[num]) * zero)
        zero //= 10
        sum += int(lst[num])
    sum = str(sum)
    res = bignumber(sum)
    if '-' in m and '-' not in n:
        res[0] = '-' + res[0]
    if '-' in n and '-' not in m:
        res[0] = '-' + res[0]       
    return res
print(bignummultiple())
                
