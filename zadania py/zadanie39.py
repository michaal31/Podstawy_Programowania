###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
C = int(input('Enter temperature in Celsius: '))
# 0 celsius = 273.15 kelvin
K = 273.15 + C  
# (C*9/5)+32=F
F = C * 1.8 + 32  # 9/5 after divide is 1.8
print(f'Temperature in Kelvin: {K}')
print(f'Temperature in Fahrenheit: {F}')
