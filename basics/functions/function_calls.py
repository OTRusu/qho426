def run():
  x=input('Please enter a word: ')
  a=input('Please chose an action (Display_Box / Display_Lower / Display_Upper / Display_Mirrored/ Display_Repeat)? ')
  z=int(input('Please enter how many times to display the word: '))
  if a == 'Display_Box':
    Display_Box(x)
  elif a == 'Display_Lower':
    Display_Lower(x)
  elif a == 'Display_Upper':
    Display_Upper(x)
  elif a == 'Display_Mirrored':
    Display_Mirrored(x)
  elif a == 'Display_Repeat':
    Display_Repeat(z, x)

def Display_Box(x):
  ascii = []
  for i in x:
    ascii.append(ord(i))
  print(ascii)


def Display_Lower(x):
  print(x.lower())

def Display_Upper(x):
  print(x.upper())

def Display_Mirrored(x):
  print(x[::-1])

def Display_Repeat(z, x):
  for n in range(z):
    if n%2 == 0:
      Display_Lower(x)
    else:
      Display_Upper(x)
run()
