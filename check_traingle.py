def check_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"

# Get inputs from the user
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check the type of triangle
triangle_type = check_triangle_type(a, b, c)

# Print the result
print("The triangle is:", triangle_type)
