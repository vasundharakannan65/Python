tup=(1,2,3,4,5,6,7,8,9,10)
#since we cannot append on a tuple ,we convert them to list
lst=list(tup)
list1=[]
#generating even numbers
for i in lst:
    if i%2==0:
        list1.append(i)
tuple1=tuple(list1)
print(tuple1)
        

