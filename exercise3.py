def map2(func, data1, data2):
  res = [None] * len(data1)
  for i in range(len(data1)):
    res[i] = func(data1[i], data2[i])
  return res
   
base = [10, 20, 30, 40, 50 ,60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

map2(pow, base, exp)



