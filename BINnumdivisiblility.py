binary = input("Enter number in Binary Format: ");
if binary == 'x':
    exit();
else:
    decimal = int(binary, 2);
    print(binary,"in Decimal =",decimal);
if decimal%5==0:
    print("It is divible by 5")
else:
    print("It is not divisible by 5")
