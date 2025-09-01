# escape sequences in python
# /"
# /'
# //
# /n

# print("hello world")
# x = 1
# name = "ghislain"
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[0:3])

# first = "byimbo"
# second = "ghislain"

# full_name = first + " " + second
# full_name = f"{first} {second}"
# print(full_name)


# printing type of variables

# print(type("hello"))
# print(type(2))
# print(type(True))
# print(type(1.43))

# type casting

# a = str(10)
# b = str("abc")
# c = str(3.5)
# d = int("3")
# e = int(3.5)
# f = int(3.5)
# g = float(1)
# h = float("32")
# i = float("12.4")

# print([a, b, c, d, e, f, g, h, i])

# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game

# customer_name = "ghislain"
# number_of_passes = 3
# token_per_pass = 30
# price_per_pass = 15.00
# tokens_per_game = 3
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
# total_tokens = number_of_passes * token_per_pass
# total_cost = number_of_passes * price_per_pass
# games_available = total_tokens // tokens_per_game
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available
# print("==== Arcade Day Pass Tracker ====")
# print("customer name: ", customer_name)
# print("Passes bought", number_of_passes)
# print("total token: $", total_tokens)
# print("Games available", games_available)


# working with user input

# name = input("what is your name?: ")
# age = input("How old are you?: ")
# print("Hello " + name + "! you're now " + age + " years old");

# name = input("what is your name?: ")
# # named = name.upper()
# kilometers = input("Enter the kilometers: ")
# miles = int(kilometers) / 1.609

# # print("Hello "+ named +" you're now "+ str(kilometers)+'km, which is '+ str(miles)+' miles');
# print(f'Heloo {name[0].upper()} you\'re now {kilometers} far away, which is {round(miles,1)}miles')

# msg = "welcome to Python 101: strings"
# msg1 = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
# print(msg1.title())
# print([msg[18],msg[:8],msg[25:29],msg[7:11],msg[13],msg[12],msg[2],msg[1],msg[-5]])
# print(msg1[::-1].title())

# # Create variables:

# # an integer for your age
# age = 24
# # a float for your height
# height = 1.79
# # a string for your school name
# school = "Rwanda Coding Academy"
# # a boolean for whether you like Python (True/False)
# likes_python = True
# # Print them all with their data types using type().
# print(type(age));
# print(type(height));
# print(type(school));
# print(type(likes_python));
# # Convert:

# # num1 = "50" (string) → cast it to an integer and add 20
# num1 = "50"
# result = int(num1) + 20
# print(result)
# # num2 = 45.67 (float) → cast it to integer
# num2 = 45.67
# print(int(num2))
# # num3 = 90 (integer) → cast it to string and join it inside: "My score is ___"
# num3 = 90
# print("My score is " + str(num3))




























