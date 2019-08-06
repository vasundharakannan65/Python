n1=int(input("Enter the num:"))
n2=int(input("Enter the number:"))
n2=n2+1
for i in range(n1,n2):
    if i%7==0 and i%5==0:
        print(i)
