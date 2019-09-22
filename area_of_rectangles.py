# Write a program that asks for the length and width of two rectangles. The program should tell the user
# which rectangle has the greater area or if they are the same.

# Gather the first rectangles measurements.
rect1_length = float(input('Enter the first rectangles length: '))
rect1_width = float(input('Enter the first rectangles width: '))

# Gather teh second rectangles measurements.
rect2_length = float(input('Enter the second rectangles length: '))
rect2_width = float(input('Enter the second rectangles width: '))

# Preform the calculations for both rectangles.
rect1_area = rect1_length * rect1_width
rect2_area = rect2_length * rect2_width

# Proceed through the if - elif statements to find which rectangle has the larger area.
if rect1_area == rect2_area:
    print(f'The two rectangles have the same area!')
elif rect1_area > rect2_area:
    print(f'The first rectangles area, {rect1_area}, is larger'
          f' than the second rectangles area, {rect2_area}.')
else:
    print(f'The second rectangles area, {rect2_area}, is larger'
          f' than the first rectangles area, {rect1_area}.')
