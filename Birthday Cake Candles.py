def birthdayCakeCandles(candles:list):
    max_of_list_elements = max(candles)
    count = candles.count(max_of_list_elements)
    return count


print(birthdayCakeCandles([1,50,3,4,5,50]))


