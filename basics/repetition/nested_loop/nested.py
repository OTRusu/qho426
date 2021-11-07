sequence = str(input('Please enter a sequence: '))
marker = str(input('Please enter a marker: '))
l1=[]
for i, charachter in enumerate(sequence):
  if charachter==marker:
    l1.append(i)
print(l1)
print(l1[2]-l1[0]-1-1) 
#example for string : abaaaabab wich will return how many a are between fir b aparicion and the third occurence of b excluding the b in the middle