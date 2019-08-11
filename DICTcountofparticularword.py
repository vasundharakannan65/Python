#dict count of particular word
ss = input().split()
dict = {i:ss.count(i) for i in ss} 
dict = sorted(dict.items())                                              
for i in dict:
    print("%s:%d"%(i[0],i[1]))
