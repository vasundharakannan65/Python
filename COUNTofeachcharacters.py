str1=str(input("Enter the string:"))
string=list(str1)
print(string)
for i in string:
    print("Count of %s is %d"%(i,string.count(i)))
