geom = [[5.5, 8.0], [4.5, 7.5], 9.5]

area_of_triangle = 0.0     # use this variable to keep the area of triangle
area_of_rectangle = 0.0    # use this variable to keep the area of rectangle    
area_of_circle = 0.0       # # use this variable to keep the area of circle

triangle = geom[0]
rectangle = geom[1]
circle = geom[2]

b,h = triangle
area_of_triangle = 0.5 * b * h

l,b = rectangle
area_of_rectangle = l * b

r = circle
area_of_circle = 3.14 * r * r
print(area_of_triangle, area_of_rectangle, area_of_circle)