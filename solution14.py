height = int(input("Enter the height of the diamond: "))

# Upper triangle
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))

# Lower triangle
for i in range(height - 1, 0, -1):
    print(" " * (height - i) + "*" * (2 * i - 1))
