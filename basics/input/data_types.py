name = str(input('What is your name human?'))
age = int(input('"How old are you (in years)?"'))
height = float(input('How tall are you (in meters)?'))
weight = float(input('How much do you weigh (in kilograms)?'))
x = height**2
bmpi = weight / x
rounded = format(bmpi, '.2f')
print(name, 'you are', age, 'years old and your bmpi is', rounded)