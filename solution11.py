width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)  
    else:
        print("*", " " * (width - 2), "*", sep="")  