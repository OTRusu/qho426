x = str(input('What type of cover does the book have?(soft/hard)'))
if x == 'soft':
  y = str(input('Is the book perfect-bound?(yes/no)'))
  if y == 'yes':
    print('Soft cover, perfect bound books are very popular!')
  else:
    print('Soft covers with coils or stitches are great for short books')
else:
  print('Books with hard covers can be more expensive!')