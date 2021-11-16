print('Program Started!\n')
x = int(input('Please enter an ASCII code: '))
x = abs(x)
if (x >= 32 and x <= 126):
  y = chr(x)
  print('The ASCII code for {} is {}.'.format(x,y))
else:
  print('You have entered a value witch is not in range.')
print('Program Ended!\n')