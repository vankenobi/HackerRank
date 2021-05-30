def is_leap(year):
    leap = False
    if(year%400 == 0):
        leap = True    
    else:
        leap = False
    return leap

print(is_leap(1992))