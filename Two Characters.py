# 'beabeefeab'
# 'babfab'
# 'babab'



def alternate(s):
    count_of_elements = []
    counts = []
    s = list(s) # converted to list
    unique_list= set(s) # converted to unique list and attached to unique_list variable
    
    for i in unique_list:
        counts.append(s.count(i))
        count_of_elements.append(str(s.count(i))+str(i))
   
    max_value = max(counts)
    min_value = min(counts)
    print(counts)
    for i in count_of_elements:
        if(int(i[0]) ==  max_value):
            for k in range(max_value):
                s.pop(s.index(str(i[1])))

        if(int(i[0]) ==  min_value):
            for k in range(min_value):
                s.pop(s.index(str(i[1])))    
    
    return len(s)

print(alternate("asdcbsdcagfsdbgdfanfghbsfdab"))