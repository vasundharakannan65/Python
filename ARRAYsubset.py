a = [1 ,2 ,3 ,4 ,5 ,6 ,7] 
b = [3,4,5,6,7,1] 
print ("Original list : " + str(a)) 
print ("Original sub list : " + str(b)) 
flag = 0
if(set(b).issubset(set(a))): 
	flag = 1
if (flag) : 
	print ("Yes") 
else : 
	print ("No") 

	
