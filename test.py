import decimal

Input = '00111001'

def binaryToDecimal(userInput):
    i = 0
    total = 0
    userInput = userInput[::-1]
    for s in userInput:
        num = int(s)
        total += num * 2**i
        print(total, num, i, sep = ' ')
        i+=1
    print(total)

binaryToDecimal(Input)

def decimal_to_binary(userInput):
    pass