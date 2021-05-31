if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # sözlük içerisindeki istenene ada sahip kişinin skorlarını topla ve skor adedine böl çıkan ondalıklı 
    # sonucun noktadan sonraki iki basamağına kadar al ve ekrana yazdır.
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]),".2f"))
