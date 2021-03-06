''' in case data1 has the fewest elements or they have equal elements '''

def map3(func, data1, data2, data3):
  res = [None] * len(data1)
  for i in range(len(data1)):
    res[i] = func(data1[i], data2[i], data3[i])
  return res
 
def sum(a, b, c)
  return a + b + c

lst1 = [1, 2, 3]
lst2 = [0, 1, 2]
lst3 = [3, 2, 1, 4]

map3(sum, lst1, lst2, lst3)


