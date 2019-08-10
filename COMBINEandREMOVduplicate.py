a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
c=a+b
print(c)
lst=[]
for i in c:
    if i not in lst:
        lst.append(i)
print(lst)
