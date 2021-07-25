num = int(input("Enter number: "))
if num==0:
    print("0 is neither prime nor composite.")
elif num==1:
    print("1 is a unitary number.")
elif (num%(num//2)) == 0:
    print("This is not a prime number.")
else:
    print("This is a prime number.")
