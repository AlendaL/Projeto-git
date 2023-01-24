numbers = [5,2,5,2,2]

# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

for x_count in numbers: 
    print('x' * x_count)

# # why this code changes the started to True after putting the same command?

# started = False
# command = ""
# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("car started already")
#         else:
#             started = True
#             print("car started")
#     elif command == "stop":
#         if not started:
#             print("car stopped already")
#         else:
#             started = False
#             print("car stopped.")
#     elif command == "help":
#         print('''
#         Start - To start the car
#         stop - to stop the car 
#         quit - to quit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("sorry I don't understand that")


# it was made by chatgpt
# while True:
#     command = input("Ask for help: ")
#     if command == "help":
#         print("start, stop, quit")
#     elif command == "start":
#         print("car started")
#     elif command == "stop":
#         print("car stopped")
#     elif command == "quit":
#         print("game quit")
#         break
#     else:
#         print("Invalid command. Please enter a valid command.")


# secret = 5

# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('guess between 0 and 9: '))
#     guess_count += 1
#     if guess < 0 or guess > 9:
#         print("Invalid input dotplease enter a number between 0 and 9")
#         continue
#     if guess == secret:
#         print("yheaaa")
#         break
#     elif guess < secret :
#         print("its bigger")
#     elif guess > secret:
#         print("its less")
   


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

