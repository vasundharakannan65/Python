#Create a tuple with numbers and print 1 item
tuple1=('1','2','3','4','5')
print("tuple1[0]:",tuple1[0])
#Convert tuple into string
str1=''.join(tuple1)
print(str1)
#Print 4th element and last 4th element of tuple
print("tuple1[4]:",tuple1[4])
print("tuple1[-4]:",tuple1[-4])
#Repeated items of a tuple
tuple2=(1,2,3,4,3,5)
lst=list(tuple2)
print(lst)
count=0
n=int(input("Enter the number to be checked:"))
for i in lst:
    if i==n:
        count+=1
print(count)
#Add an item in a tuple
tuple1=tuple1+('9',)
print(tuple1)
#Remove a item "3"
tuple1=tuple1[:2]+tuple1[3:]
print(tuple1)
#Length of the tuple
print("the length of the tuple1 is",len(tuple1))
#Conversion of tuple into dictionary
tuple3 = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuple3))
#List of tuples replace last value
lst1=[(1,2,3),(4,5,6),(7,8,9)]
print([i[:-1]+(100,)for i in lst1])




