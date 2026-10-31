x = int(input("Enter first angle: "))
y = int(input("Enter second angle: "))
z = int(input("Enter third angle: "))
total = x + y + z
if x > 0 and y > 0 and z > 0 and total == 180:
    print(f"The triangle with angles {x} , {y} , {z} is valid.")
else:
    print(f"The triangle with angles {x} , {y} , {z} is not valid.")