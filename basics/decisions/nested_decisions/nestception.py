x = str(input('Where should I look?(in the bedroom/under the bed/ in the bathroom /in the bathtube/in the lab)'))
if x == 'in the bedroom':
  y = str(input('Where in the bedroom should I look?(under the bed)'))
  if y == 'under the bed':
    print('Found some shoes but no battery')
  else:
    print('Found some mess but no battery.')
elif x == 'in the bathroom':
  y = str(input('Where in the bathroom should I look?in the bathtub)'))
  if y =='in the bathtub':
    print('Found a rubber duck but no battery')
  else:
    print('Found a wet surface but no battery.')
elif x == 'in the lab':
  y = str(input('Where in the lab should I look?(on the table)'))
  if y =='on the table':
    print('Yes! I found my battery!')
  else:
    print('Found some tools but no battery.')
else:
  print('I do not know where that is but I will keep looking.')