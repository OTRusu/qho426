x = int(input(' How many bars should be charged? '))
print('I will charge %d bars' %(x))
charge = 0
while charge < x:
  charge +=1
  print('Charging:...')
  print('|' * charge)
print('The battery is fully charged.')