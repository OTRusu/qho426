x = str(input('How many degrees ar outside?(-1/0)'))
print(x)
y = str(input('Is it snowing?(yes/no)'))
print(y)
if x == ('-1') and y == ('yes'):
  print('Have a cup of tea and stay inside.')
elif x ==(0) or y ==('yes'):
  print('Put a jacket on.') 
else:
  print('Have a nice walk outside')