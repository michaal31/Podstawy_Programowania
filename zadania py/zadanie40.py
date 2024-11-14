###
# A program that prints your height both in cm and in feet and inches.
#
cm = 183
feet = cm // 30.40
inches = (cm-30.40*feet) / 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, I am {feet} and {inches:.2f} inches')