odd_lst=[]
lst=[]
n=int(input("Enter number of elements : ")) 
for i in range(0, n): 
	ele = int(input()) 
	lst.append(ele) 	
print(lst) 
odd_list = [i for i in lst if (int(i) % 2 != 0)]
print(odd_list)
