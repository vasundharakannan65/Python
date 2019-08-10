a=[12,24,35,24,88,120,155,88,120,155]
lst=[]
for i in a:
    if i not in lst and i!=24:
        lst.append(i)      
print(lst)
