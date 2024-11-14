#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h.
#  Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

speed = int(input('Enter vehicle speed: '))
correct_speed = 40 <= speed <= 140
print(f'Speed is valid: {correct_speed}')