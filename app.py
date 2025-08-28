# escape sequences in python
# /"
# /'
# //
# /n

print("hello world")
x = 1
name = "ghislain"
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[0:3])

first = "byimbo"
second = "ghislain"

# full_name = first + " " + second
full_name = f"{first} {second}"
print(full_name)


# printing type of variables

print(type("hello"))
print(type(2))
print(type(True))
print(type(1.43))

# type casting

a = str(10)
b = str("abc")
c = str(3.5)
d = int("3")
e = int(3.5)
f = int(3.5)
g = float(1)
h = float("32")
i = float("12.4")

print([a, b, c, d, e, f, g, h, i]);

# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game

customer_name = "ghislain"
number_of_passes = 3
token_per_pass = 30
price_per_pass =15.00
tokens_per_game = 3
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
total_tokens = number_of_passes * token_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_per_game
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available
print("==== Arcade Day Pass Tracker ====")
print("customer name: ", customer_name)
print("Passes bought", number_of_passes)
print("total token: $",total_tokens)
