# That is Coderspace problem
import itertools

def MathChallenge(num:int):
    numList = list(str(num))
    combinationOfNumList = list(itertools.permutations(numList,len(numList)))
    combinationOfNumList = list(int(''.join(i)) for i in combinationOfNumList)
    combinationOfNumList.sort()
    
    for i in combinationOfNumList:
        if(i > num):
            return i
    return -1   

print(MathChallenge(41352))

