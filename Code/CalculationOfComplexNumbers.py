
operators = ['+','-']

def additionComplexNumber(operationsWert):
    reelValue = 0
    imagValue = 0

    for i in range(0, len(operationsWert)):
        if operationsWert[i].find('i') == -1 and operationsWert[i] not in operators:
            reelValue += int(operationsWert[i])
        if operationsWert[i].find('i') != -1 and operationsWert[i] not in operators:
            imagValue += int(operationsWert[i].replace('i', ''))
            print(imagValue)
    return  str(reelValue) + "+" + str(imagValue) + 'i'

def substractionComplexNumbers(a, b):
    return  a - b

def multiplicationComplexNumber(a, b):
    return  a * b

def divisionComplexNumber(a,b):
    return a/b

x =  "2+5i+4"
operationsWert = []
def checkEntryValue(x, operationsWert_, operators_):
    val = ''
    checkValue = True
    for zeichen in x:
        if zeichen.isalpha() and zeichen != 'i':
            checkValue = False
        if zeichen in operators_:
            operationsWert_.append(val)
            operationsWert_.append(zeichen)
            val = ''
            continue
        if zeichen == ' ':
            continue
        val += zeichen
    operationsWert_.append(val)
    return checkValue

check = checkEntryValue(x, operationsWert, operators)
print(check)
print(operationsWert)
print(additionComplexNumber(operationsWert))