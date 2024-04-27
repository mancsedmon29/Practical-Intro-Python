# Ask the user for the size of the giant letter A
size = int(input("Enter the size of the giant letter A: "))

# Upper part of the letter A
for i in range(size):
    if i == 0:
        print(" " * (size - i - 1) + "*")
    elif i == size // 2:
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (size - i - 1) + "*" + " " * (2 * i - 1) + "*")