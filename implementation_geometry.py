from geometry.rectangle import info as rectangle_info, calculate_rectangle_area
from geometry.triangle import calculate_triangle_area, info as triangle_info

a = 10
b = 20

print(f'\n{triangle_info()}')
print(f'the triangle area of base: {a} and height: {b} is {calculate_triangle_area(a, b)}')

print(f'\n{rectangle_info()}')
print(f'the rectangle area of length: {a} and width: {b} is {calculate_rectangle_area(a, b)}')
