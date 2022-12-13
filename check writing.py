

def numberclump(digits, i):
    if digits[i] !=0:
        if digits[i-1] != 1 and digits[i-1] != 0:
            print(words.get(digits[i]), "hundred", tens.get(digits[i-1]), words.get(digits[i-2]), end = '')

        elif digits[i-1] == 1 and digits[i-2] == 0:
            print(words.get(digits[2]), "hundred and ten", end = '')

        elif digits[i-1] == 1 and digits[i-2] == 1:
            print(words.get(digits[2]), "hundred and eleven", end = '')

        elif digits[i-1] == 1 and digits[i-2] == 2:
            print(words.get(digits[2]), "hundred and twelve", end = '')

        elif digits[i-1] == 1 and digits[i-2] == 3:
            print(words.get(digits[i]), "hundred and thirteen", end = '')

        elif digits[i-1] == 1:
            print(words.get(digits[i]), "hundred", words.get(digits[i-2]) + tens.get(digits[i-1]),end = '')

    elif digits[i-1] !=0:
        if digits[i-1] != 1 and digits[i-1] != 0:
            print(tens.get(digits[i-1]), words.get(digits[i-2]), end = '')
        elif digits[i-1] == 1 and digits[i-2]==0:
            print("ten", end = '')
        elif digits[i-1] == 1 and digits[i-2]==1:
            print("eleven", end = '')
        elif digits[i-1] == 1 and digits[i-2]==2:
            print("twelve", end = '')
        elif digits[i-1] == 1 and digits[i-2]==3:
            print("thirteen", end = '')

        elif digits[i-1] == 1:
            print(words.get(digits[i-2])+tens.get(digits[i-1]), end = '')
    else:
        print(words.get(digits[i-2]), end = '')
words = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
    }

tens = {
    1:"teen",
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"nintey"
    }

def numbercrunch(num):
    amount = int(num)

    digits = []
    i = 1
    while amount>=1:
        digits.append(amount%10)
        num -= (amount%10) * i
        amount = amount//10
        i*=10

    num = round(num,2)
    num = num * 100

    if len(digits)%3 == 2:
        digits.append(0)

    elif len(digits)%3 == 1:
        digits.append(0)
        digits.append(0)

    if len(digits)>6:
        numberclump(digits, 8)
        print("million, ", end = '')

    if len(digits)>3:
        numberclump(digits, 5)
        print(" thousand, ", end = '')

    numberclump(digits,2)
    print(" dollars and", int(num),"/ 100")

doExit = False
print("Welcome to the Auto Check Writing Program")
while doExit == False:
    num = float(input("Please enter dollar amount for check, 0 to quit:"))
    if num !=0:
        numbercrunch(num)
    else:
        doExit = True

print("goodbye!")
