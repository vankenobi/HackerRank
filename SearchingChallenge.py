# That is coderspace problem

text = "H3ello9-9113"

def searchingChallenge(text:str):
    sumOfNumbers = 0 
    sumOfCharacters = 0
    for i in text:
        if(i.isnumeric()):
            sumOfNumbers += int(i)
        else:
            sumOfCharacters += 1
    return round(sumOfNumbers / sumOfCharacters)        

a = searchingChallenge(text)
print(a)

