a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if a>b and a>c: # Logical op. "and" used to print only if both conditions are true
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
else:
    print("c is greater") 
