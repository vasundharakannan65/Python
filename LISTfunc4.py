a=[12,24,35,70,88,120,55]
b=[]
for i in a:
    if i%5==0: 
        a.remove(i)
    elif i%7==0:
        a.remove(i)
    else:
        b.append(i)
print(b)
