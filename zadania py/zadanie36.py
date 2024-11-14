#In many games, the numbers one and six on dice have special meaning.
#Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6.
import random
dice_roll = random.randint(1,6)
special_number = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')