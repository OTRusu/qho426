x = int(input('Please enter first number. '))
y = int(input('Please enter second number. '))
z = int(input('Please enter third number. '))
l1=[x,y,z]
print(l1)
odd, even =0,0
for n in l1:
  print(n)
  if n%2==0:
    even +=1
  else:
    odd +=1
print('There were {0} even and {1} odd numbers.'.format(even, odd))