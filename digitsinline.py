import re
n=str(input("Enter the no. of elemnents:"))
ans=re.sub(r'\D',"",n)
print("Digits in the sentence are:",ans)
lst=list(ans)
print(lst)
