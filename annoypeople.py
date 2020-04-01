import string
s = input("Enter your string: ")

s = s.lower()

numbers = dict(zip([str(x) for x in range(10)],
               "zero, one, two, three, four, five, six, seven, eight, nine".split(", ")))

retstr = ""
for char in s:
    if char in string.punctuation+' \n':
        retstr += ":space: "
    elif char in string.digits:
        retstr += ":{}: ".format(numbers[char])
    else:
        #retstr += ":{}{}:".format(char, char)
        retstr += ":regional_indicator_{}: ".format(char)
        
print(retstr)
