wheight = int(input("wheight: "))

unit = input("(L)bs (K)bs: ")

if unit.isupper() == "L":
    converted = wheight * 0.45   
    print(f"you are {converted} kilograms")
elif unit.isupper() == "K":
    converted = wheight / 0.45
    print(f"you are {converted} pounds")
else:
    print("Invalid input. Please enter only uppercase L or K.")
