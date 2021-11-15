x = int(input(' How many numbers should I sum up? '))
i = 0
total = 0
while i < x:
  i +=1
  z = int(input('Please enter number %d of %d:  ' %(i,x)))
  total = total + z
  print('The answer is: ', total)