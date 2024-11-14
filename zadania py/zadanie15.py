###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
cuboid_volume = (a*b*c) 
cuboid_surface_area = 2*(a*b+a*c+b*c)
print(f"Cuboid volume is {cuboid_volume}")
print(f"Cuboid surface area = {cuboid_surface_area}")