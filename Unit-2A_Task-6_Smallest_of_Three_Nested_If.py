x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x <= y:
    if x <= z:
        smallest = x
    else:
        smallest = z
else:
    if y <= z:
        smallest = y
    else:
        smallest = z
print(f"The smallest number is {smallest}.")
