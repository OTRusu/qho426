string = str(input('Please enter a sequence:'))
marker = str(input('Please enter the character for the marker:'))
marker1 = -1
marker2 = -1
for position in range(0, len(string), 1):
    charachter = string[position]
    if (charachter == marker):
        if (marker1 == -1):
            marker1 = position
        else:
            marker2 = position
print(f"The distance between the markers is {marker2 - marker1 - 1}.")