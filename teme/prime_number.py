def prime_number():
  x = int(input('Please eneter a number bigger by number 1: '))
  if x > 1:
    for i in range(2, x):
      if (x%i)==0:
        print(x,"is not a prime number")
        break
    else:
      print(x,"is a prime number")
  if x == 1:
    print(x,"is not a prime number")
prime_number()