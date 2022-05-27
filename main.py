#Weight converting#

weight = float(input("Weight: "))
unit = input(str("units[L(lbs)/K(kg)]"))
if unit.upper() == "L":
    weigh = 0.45*weight
    print(f"{weigh} kilograms")
elif unit.upper() == "K":
    weigh = 2.20*weight
    print(f"{weigh} pounds")
else:
    print("didn't catch that")
