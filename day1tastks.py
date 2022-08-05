#1. The sum of the numbers in file
def filesum(file):
    openfile = open(file, "r")
    readfile = openfile.read()
    splitfile = readfile.split()
    sum = 0
    for num in splitfile:
        sum += int(num)
    return sum


#2. Capitalize the first letters and move to another file
def fileupper(file, anotherfile):
    openfile = open(file,"r")
    readfile = openfile.read()
    newfile = readfile.title()
    another = open(anotherfile, "x")
    another.write(newfile)
     
#3. The number of repititions of all the numbers in a list
def numcount(lst):
    numfreq = [lst.count(num) for num in lst]
    print(dict(zip(lst, numfreq)))

#4. The number of symbols in a file
def symbolcount(file):
    openfile = open(file, "r")
    readfile = openfile.read()
    return len(readfile)


#5. Remove every third symbol in a string
def removethird(string):
    lst = list(string)
    del lst[2::3]
    return "".join(lst)

#6. The number of repititions of all the words in a file
def file_word_count(file):
    openfile = open(file, "r")
    readfile = openfile.read()
    splitfile = readfile.split()
    wordfreq = [splitfile.count(word) for word in splitfile]
    return dict(zip(splitfile, wordfreq))

#7. Count the squares of the list values and save in a sorted list
def listsqr(lst):
    newlst = [None] * len(lst)
    for i in range(len(lst)):
        newlst[i] = lst[i] ** 2
    return sorted(newlst)

#8. The sum of the digits of a number
def digitsum(number):
    sum = 0
    strnum = str(number)
    for digit in strnum:
        sum += int(digit)
    return sum

#9. The difference between the product and the sum of the digits in a number
def digitdiffer(number):
    sum = 0
    product = 1
    strnum = str(number)
    for digit in strnum:
        sum += int(digit)
        product *= int(digit)
    return product - sum

#10. The number of odd numbers in a range
def oddcount(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    return count
    

