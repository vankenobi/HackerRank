contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
def luckBalance(k, contests):
    change = []
    for i in contests:
        change.append(i[0])
    change = sorted(change)
    print(change)
    for i in range(k-1):
        change.pop(0) 
    print(sum(change))

luckBalance(2,contests)