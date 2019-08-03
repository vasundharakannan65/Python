a=int(input("NUM:"))
b=int(input("NUM:"))
c=int(input("NUM:"))
sum=a+b+c
def func(a,b,c):
    if a==b==c:
        return sum*3
    else:
        return 'NOT EQUAL'
print(func(a,b,c))
