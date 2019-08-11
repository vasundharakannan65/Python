def gen():
    n=int(input("Enter the no. of elemnents:"))
    for i in range(0,n):
        if i%2==0:
            yield i
gen()
for value in gen():
    print(value)
