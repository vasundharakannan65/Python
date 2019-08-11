n=int(input("Enter the num to be divided:"))
try:
    print(n/0)
except ZeroDivisionError:
    raise 
else:
    print("Error is raised and it cant be divided")




