###
#A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference
# of the tree entered from the keyboard, calculates and prints the value True if the tree can be cut down, or print the value False otherwise. 

circumference = int(input('Enter tree  circumferences in cm: '))
can_be_cut = circumference >= 150
print(f'Tree can be cut down: {can_be_cut}') # tree 1 and 3 can be cut down