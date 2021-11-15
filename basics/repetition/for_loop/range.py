x = int(input('What level of brightness is required? '))
print('\n Adjusting brightness...\n')
for i in range(2, x+1, 2):
  print("Beep's brightness level:", i*'*')
  print("Bop's brightness level:", i*'*')
print('\nAdjustments complete!')