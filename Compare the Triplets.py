def compareTriples(a,b):
    Alice = 0
    Bob = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                Alice += 1
            elif a[i] < b[i]:
                Bob += 1
    
    return Alice,Bob
            
        
result = compareTriples([1,2,3],[5,1,6])
print(result)