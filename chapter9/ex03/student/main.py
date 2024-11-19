import random


try:
    print(random.randinteger(5, 15))  # This is an error: incorrect method name
except AttributeError:
    print("Double check the attributes in your code and try again.")
