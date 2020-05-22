# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def sing_dig(x): # used to count letters of single digit numers
    tot = 0
    if x in [1, 2, 6]:
            tot += 3
    elif x in [3, 4, 5, 9]:
            tot += 4
    elif x in [7,8]:
            tot += 5
    return tot
def dub_dig(x): # used to count letters of double digit numbers
    total = 0
    if int(str(x)[0]) == 1:
        total += 4
    elif int(str(x)[0]) in [2, 3, 4, 8, 9]:
        total += 6
    elif int(str(x)[0]) in [5, 6]:
        total += 5
    elif int(str(x)[0]) in [7]:
        total += 7
    if len(str(x)) == 2:
        total += sing_dig(int(str(x)[1]))
    elif len(str(x)) == 1:
        total += sing_dig(x)
    return total
def trip_dig(x): #used to count letters of triple digit numbers
    total = 0
    if int(str(x)[0]) != 0:
        total += 7
        if x in [1, 2, 6]:
            total += 3
        elif x in [3, 4, 5, 9]:
            total += 4
        elif x in [7, 8]:
            total += 5
    total += dub_dig(int(str(x)[1:]))
    return total

def range_sum(num1, num2):
    total = -1  # starts the initial count, accounting for numbers ten, eleven and twelve which are exceptions to the rule, mean range must exceed 13 for count to be accurate
    for x in range(num1,num2):
        if len(str(x)) == 1: #determines length of number and counts digits using appropriate function
            total += sing_dig(x)
        elif len(str(x)) == 2:
            total += dub_dig(x)
        elif len(str(x)) == 3:
            total += trip_dig(x)
    return total
print(range_sum(1,1000))
