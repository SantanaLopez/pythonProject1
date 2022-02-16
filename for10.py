decimal = 0
print('Enter a number: ')
binary = input()
print('You entered: ' + str(binary))
for i in binary:
    decimal = decimal * 2 + int(i)
print(decimal)