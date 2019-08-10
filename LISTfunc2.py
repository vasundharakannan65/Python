def func():
    l=list()
    for x in range(1,21):
        l.append(x**2)
    print(l)
    print(l[:5])#To print first 5 elements
    print(l[-5:])#To print last 5 elements
    print(l[5:])#To print elements except first 5
func()
