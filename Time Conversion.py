def timeConversion(s:str):
    hour = s.split(":")

    if hour[2][2:] == "PM":
        if int(hour[0]) > 12:
            result = ":".join(map(str,hour)) 
        else:
            convertion = int(hour[0]) % 12 + 12
            hour[0] = convertion
            hour[2] = hour[2][0:2]
            result = ":".join(map(str,hour))

    elif hour[2][2:] == "AM":
        convertion = str(int(hour[0]) % 12) 
        if len(convertion) == 1:
            convertion = "0" + convertion
        hour[0] = convertion
        hour[2] = hour[2][0:2]
        result = ":".join(map(str,hour))

    return result
       
   

print(timeConversion("06:40:03AM")) # For example