###
# A program that, based on the person's age entered from the keyboard
# prints True if the preson is exempt from paying taxes
# and prints False oterwise
#
age = int(input('Enter age: '))
no_tax = age < 27
print(f'Excemption from paying taxes: {no_tax}')