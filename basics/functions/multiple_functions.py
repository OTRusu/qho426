def display_ladder(steps):
  for steps in range(steps):
    print('| |')
    print('***')
  print('| |')
def create_ladder():
  steps = int(input('How many steps remaind? '))
  display_ladder(steps)
create_ladder()