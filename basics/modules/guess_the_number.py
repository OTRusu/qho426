import random as rnd
x = int(input('Please enter the minimum value:'))
y = int(input('Please enter the maximum value:'))
z = rnd.randrange(x, y, 1)
print('I am thinking of a number between {} and {}. Can you guess what it is?' .format(x, y))
a = int(input('Please enter a number in the range of minimum and maximum'))
while z in range(x, y):
  if a < z :
    print('Your guess is too low!')
    print('Try again!')
    a = int(input('Please enter a number in the range of minimum and maximum: '))
  elif a > z:
    print('Your guess is too high!')
    print('Try again!')
    a = int(input('Please enter a number in the range of minimum and maximum:'))
  elif a == z:
    print('Congratulations!You guessed my number!')
    break