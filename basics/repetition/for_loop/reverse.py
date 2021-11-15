x = str(input("What phrase do you see? "))
print('\n Reversing...\n')
for i in range(len(x)-1, -1, -1):
  print(x[i], end='')