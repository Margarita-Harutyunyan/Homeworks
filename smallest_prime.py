#Program to check if a number is prime

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False

#Program to find the smallest prime number after n

def smallest_prime(n):
    m = n + 1
    if is_prime(m):
        return m 
    else:
        m = m + 1
    return m
