x = int(input(' How many cables should i remove: '))
print('I wil remove %d cables' %(x))
y = int(input('How many cables should I avoid: '))
print('I will avoid %d cables' %(y))
avoid = 0
removed = 0
while removed < x:
  while avoid < y:
    avoid +=1
    print('Avoiding... %d' %(avoid))
    print('...Done! %d live cable avoided!' %avoid)
  removed +=1
  print('I removed %d cable(s).' %removed)
print('I removed in total %d cables.' %(removed))
print('All live cables have been avoided.')