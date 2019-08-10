a=[12,24,35,70,88,120,155]
lst=[]
for i in a:
    if a[0]==i or a[4]==i or a[5]==i :
        lst.append(i)
print(lst)
del lst
