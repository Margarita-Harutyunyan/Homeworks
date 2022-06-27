#Program to find median
def get_median(data):
    n = len(data)
    if  n % 2 == 0:
        return data[n//2] + data[(n//2 - 1)]
    else:
        return data[n//2]
