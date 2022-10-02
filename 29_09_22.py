i = 0
string = ''
while i < 5:
    n = input('Enter a number: ')
    string += n + '+'
    i += 1
string = string[:-1]
print(string)
