def example(lives):
#lives = int(input('Please enter the number of lives: '))

  for live in range(lives):
    print('***')
    energy = int(input('Please enter the energy level: '))
    shield = int(input('Please enter the shield level: '))
    while energy > 5:
      if shield > 90:
        print('You rock')
        break
      
      elif shield > 70:
        print('You are ok')
        break

      else: 
        print('Take care')
        break
    print('Go to recharge your energy')

example(3)

example(5)
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