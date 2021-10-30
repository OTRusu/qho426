# Ask user to enter their name
print("What is your name human?")
name = input()
print("It is nice to meet you human", name)
print('          ')
print('          ')
print('          ')

name = input("What is your name human? ")
print("Nice to meet you human ", name, ".")
print('          ')
print('          ')
print('          ')


name = input("What is your name human? ")
print("Nice to meet you {}.".format(name))
print('          ')
print('          ')
print('          ')

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))