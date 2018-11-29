import math
import decimal


'''Doc Comment'''

'''
To Do:

Treat everything as a string
write methods to convert every base to binary
write method to convert binary to desired output

'''



#decimal to any base
numInput = input("number: ")
base = input("base: ")
printSecond = False

dec = decimal.Decimal(numInput)
#e = abs(dec.as_tuple().exponent)
intPart = int(dec)
d = dec - intPart


lFirst = []
lSecond = []

# Dict for hex numbers > 9
def hexConvert(x):
    return {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }.get(x, x)

# Divide by base for integer part
i = intPart
while (i!=0): #works for whole numbers
    r = i // base
    m = i % base

    lFirst.append(hexConvert(m))
    print(i, '/', base, '=', r, 'R', m, sep=' ')
    i = r
print()

# Multiply by base for decimal part
if d != 0:
    print('decimal')
    print()
    i = d
    printSecond = True
    count = 0
    while (i!=0 and count <= 10):
        r = i * base 
        n = int(r)
        decPart = r - n
        i = decPart

        lSecond.append(hexConvert(n))

        print(i, '*', base, '=', r, 'R', n, sep=' ')
        count+=1

# reverse whole number list as the order of the remainders is backwards when dividing
lFirst = lFirst[::-1] 


for value in lFirst:
    print(value, end='')

if printSecond:
    print('.', end = '')
    for value in lSecond:
        print(value, end='')

print()
