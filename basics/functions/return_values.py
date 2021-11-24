def sum_weights(beep_weight, bop_weight):
  total_weight = bop_weight + beep_weight
  return total_weight

def calc_avg_weight(bop_weight, beep_weight):
  avg_weight = (bop_weight + beep_weight)/2
  return avg_weight

def run():
  beep_weight=float(input('Please enter Beep weight:'))
  bop_weight=float(input('Please enter Beep weight:'))
  x=input('What would you like to calculate (sum or average)? ')

  if (x == 'sum'):
    y = sum_weights(beep_weight, bop_weight)
    print('Total weight is {:.2f}.'.format(y))
  elif (x == 'average'):
    y= calc_avg_weight(beep_weight, bop_weight)
    print('Average weight is {:.2f}.'.format(y))
run()