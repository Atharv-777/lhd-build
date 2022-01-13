def getNumArr(text):
    numArr = []
    for letter in text.replace(" ", ""):
        numArr.append(ord(letter) - 65)
    return numArr

def getCipherText(key):
    res = []
    key = "NCBTZQARXDHAKHDJKKSHBUEOAHAPDHDHFDJFDFDJFBSJDBSFJSFB"
    textArr = getNumArr(text.upper())
    keyArr = getNumArr(key)
    getCipherText = ""
    for i in range(len(textArr)):
        addition = textArr[i] + keyArr[i]
        if(addition > 26):
            addition -= 26
        res.append(addition)

    for num in res:
        getCipherText += chr(num + 65)
    return getCipherText


text = input("Enter your text : ")
print(getCipherText(text))
