if __name__ == '__main__':
    
    student_list = []   # öğrenci listesi oluşturuldu.
    result_list = []    # öğrenci score sonuçları
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])   # Bir listeye gelen öğrencilerin ad ve skorlarını ekler.

    student_list.sort()  # liste içerisindeki isimlere göre alfabetik sırayla dizer.

    for i in student_list:  # Sadece skorları tutmak ve en düşük ikinci skoru bulmak için result list içerisine skorları kaydediyoruz.
        result_list.append(i[1])

    result_list = list(set(result_list)) # unique list
    result_list.sort()                   # sort list   
    

    for i in range(0,len(student_list)):
        if(result_list[1] == student_list[i][1]):
            print(student_list[i][0])

            

    
    
    
    