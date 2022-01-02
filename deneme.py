def gradingStudents(grades):
    result = []
    for i in grades:
        if i >= 38 and 5-i % 5 <= 2:
            result.append(i+5-i%5)
        else:
            result.append(i)
            
    return result

result = gradingStudents([74,67,37,33])
print(result)

            