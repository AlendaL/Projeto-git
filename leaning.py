
secret = 5

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('guess between 0 and 9: '))
    guess_count += 1
    if guess < 0 or guess > 9:
        print("Invalid input dotplease enter a number between 0 and 9")
        continue
    if guess == secret:
        print("yheaaa")
        break
    elif guess < secret :
        print("its bigger")
    elif guess > secret:
        print("its less")
   


# i = 1

# while i <= 100:
#     print("*" * i)
#     i += 1
# print("done")


# wheight = int(input("wheight: "))

# unit = input("(L)bs (K)bs: ")

# if unit.upper() == "L":
#     converted = wheight * 0.45   
#     print(f"you are {converted} kilograms")
# else: 
#     converted = wheight / 0.45
#     print(f"you are {converted} pounds")

