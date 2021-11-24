def cross_bridge(x):
  x = int(input('Please enter the number of steps: '))
  for steps in range(x):
    print('Crossed step.')
  if steps>5:
    print('The bridge is collapsing!')
  else:
    print('we must keep going')
cross_bridge('x')