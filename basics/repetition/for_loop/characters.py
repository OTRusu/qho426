x = str(input("What strange markings do you see? "))
print('\n Identifying...\n')
for i in range(0, len(x), 1):
    print('Index %d:' %i, x[i])
print('\n Done! \n')