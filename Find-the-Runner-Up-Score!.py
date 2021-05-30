from os import read
from typing import List, Set


if __name__ == "__main__":

    n = int(input())  
    arr = map(int, input().split())

    unique_list = list(set(arr))     # set metodu ile unique bir liste oluştur.
    sorted_list = unique_list.sort() # sort metodu ile unique_list'i sırala

    print(unique_list[len(unique_list)-2]) # en büyük ikinci sayıyı yazdır.
        
        