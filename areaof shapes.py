import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius * radius

# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

while True:
    print("\nMenu:")
    print("1. Calculate the area of a rectangle")
    print("2. Calculate the area of a circle")
    print("3. Calculate the area of a triangle")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
    except ValueError:
        print("Invalid choice. Please enter a valid choice (1/2/3/4).")
        continue

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print("Area of the rectangle:", area)

    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print("Area of the circle:", area)

    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print("Area of the triangle:", area)

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid choice (1/2/3/4).")
