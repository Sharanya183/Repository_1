#If name<3 characters long, "name must contain at least 3 characters". If name>50 characters long, "name exceeds 50 characters". Otherwise, "Looks perfect!"#

name = input(str("Name: "))
if len(name) < 3:
    print("name must contain at least 3 characters")
elif len(name) > 50:
    print("name exceeds 50 characters")
else:
    print("Looks perfect!")
    