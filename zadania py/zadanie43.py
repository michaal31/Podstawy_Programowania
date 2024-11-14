###
# A program that convert a decimal number to binary or hexadecimal value
#
decimal = int(input('Enter number: '))
binary = bin(decimal)
hexadecimal = hex(decimal)
print(f'Binary number: {binary}')
print(f'Hexadecimal number: {hexadecimal}')