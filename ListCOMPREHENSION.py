lst=[1,2,3,4,5,6,7,8,9]
odd_lst_sq=[]
odd=[]
for i in lst:
    if i%2==0:
       print()
    else:
        odd.append(i)
        n=i**2
        odd_lst_sq.append(n)
print(odd)
print(odd_lst_sq)
