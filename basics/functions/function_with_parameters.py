def climb_ladder(steps_remaining, steps_crossed):
  steps_remaining = int(input('Please enter the number of steps remaining: '))
  steps_crossed =int(input('Please enter the number of steps crossed: '))
  if steps_remaining > steps_crossed:
    print('Still some way to go!')
  else:
    print('We are almost there!')
climb_ladder('steps_remaining', 'steps_crossed')