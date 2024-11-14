#nter phone number: 543097329
#Phone number: 543-097-329

###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
phone1 = phone[:3] + '-' + phone[3:6] + '-' + phone[6:9]
print("Numer telefonu:", phone1)