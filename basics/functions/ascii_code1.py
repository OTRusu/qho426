print('Program Started!\n')
x = input('Please enter a standard character: ')
for i in x:
  if len(x) < 2:
    y = ord(x)
    print('The ASCII code for {} is {}.'.format(x,y))
  else:
    print('You have entered more than one charachter.')
print('Program Ended!\n')