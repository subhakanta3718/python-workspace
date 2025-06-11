import math

# Coordinates of the two points
x1, y1 = map(int,input("Enter x1 and y1 (separated by space): ").split())
x2, y2 = map(int,input("Enter x2 and y2 (separated by space): ").split())

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between the points is: {distance}")
