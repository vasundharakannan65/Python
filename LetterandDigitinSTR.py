n=str(input("SENTENCE:"))
l=d=0
for i in n:
    if i.isdigit():
        d+=1
    elif i.isalpha():
            l+=1
    else:
        print()
print("LETTERS:",l)
print("DIGITS:",d)
