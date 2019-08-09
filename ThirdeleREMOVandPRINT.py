list1=[0,1,2,3,4,5]
len_list1=len(list1)
for i in list1:
    if len_list1>0:
            try:
                while (list1[i]==list1[2]):
                   print(list1.pop(i))
                   print(list1)
            except IndexError:
                    print("INDEX ERROR:Index out of range")
print(list1.pop(1))
print(list1.pop(0))
