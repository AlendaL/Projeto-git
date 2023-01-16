
secret = 5

guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret:
        print("yheaaa")
    elif guess < secret :
        print("its bigger")
    elif guess > secret:
        print("its less")
    elif guess > guess_limit or guess < guess_count: 
        print("you need to put and coherent number")


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

