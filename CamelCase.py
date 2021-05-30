from re import findall

word = "oneTwoThereFourFiveFour"

def camelcase(s):
    checkpoint1 = 0
    stringlist = []
    for i in range(0,len(s)):
        if(s[i].isupper() == True):
            stringlist.append(s[checkpoint1:i])
            checkpoint1 = i   
    if(checkpoint1 < len(s)):
            stringlist.append(s[checkpoint1:len(s)])
    return len(stringlist)

camelcase(word)