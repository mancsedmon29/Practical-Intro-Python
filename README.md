# A Practical Introduction to Python Programming by Brian Heinold

## Chapter 1: Getting Started

### First Program

```
temp = eval(input("Enter temperature in Celsius: "))
print(f"In Fahrenheit: {9/5 * temp + 32}")
```

After running:

```
Enter temperature in Celsius: 20
In Fahrenheit: 68.0
```

### Second Program

```
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

print("The average of the numbers you entered is:", (num1 + num2) / 2)
```

After running:

```
Enter first number: 5
Enter second number: 5
The average of the numbers you entered is: 5.0
```

Python will insert a space between each of the arguments of the print function. There is an optional argument called `sep`, short for separator, that you can use to change that space to something else.

```
print("The value of 3 + 4 is ", 3 + 4, ".")
print("The value of 3 + 4 is ", 3 + 4, ".", sep="")
```

Output:

```
The value of 3 + 4 is  7 .
The value of 3 + 4 is 7.
```

`end` The print function will automatically advance to the next line.

Scenario without `end`.

```
print("On the first line")
print("On the second line")
```

Output:

```
On the first line
On the second line
```

If with `end`.

```
print("On the first line", end='')
print("On the second line")
```

Output:

```
On the first lineOn the second line
```

### Variables

One of the major purposes of a variable is to remember a value from one part of a program so that it can be used in another part of the program.

```
temp = eval(input('Enter a temperature in Celsius: '))
print('In Fahrenheit, that is', 9/5*temp+32)
```
In the case above, the variable temp stores the value
that the user enters so that we can do a calculation with it in the next line.

Output:

```
Enter a temperature in Celsius: 31
In Fahrenheit, that is 87.80000000000001
```

Another example of temperature with condition:

```
temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9 / 5 * temp + 32
if f_temp > 212:
    print("That temperature is above the boiling point.")
if f_temp < 32: 
    print("The temperature is below the freezing point.")
```

Output:

```
Enter a temperature in Celsius: 220
That temperature is above the boiling point.
```

### Variable names

There are just a couple of rules to follow when naming your variables.
- Variable names can contain letters, numbers, and the underscore.
- Variable names *cannot* contain spaces.
- Variable names *cannot* start with a number.
- Case matters—for instance, `temp` and `Temp` are different.

### Exercise

1. Print a box like the one below.
```
*******************
*******************
*******************
*******************
```

Code: 

```
row = 4
cols = 19

for i in range(row):
    for j in range(cols):
        print("*", end="")
    print()
```

2. Print a box like the one below.

```
*******************
*                 *
*                 *
*******************
```

Code: 

```
rows = 4
cols = 19

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

3. Print a triangle like the one below.
```
*
**
***
****
```

Code:

```
rows = 4

for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()
```

4. Write a program that computes and prints the result of 512 − 282 / 47 * 48 + 5. It is roughly 0.1017.

Code:

```
result = (512 - 282) / (47 * 48 + 5)
print("Result:", round(result, 4))
```

5. Ask the user to enter a number. Print out the square of the number, but use the sep optional argument to print it out in a full sentence that ends in a period. Sample output is shown below.

```
Enter a number: 5
The square of 5 is 25.
```

Code: 

```
from math import *

number = float(input("Enter a number: "))

square = number ** 2

print("The square of", floor(number), "is", floor(square), end=".\n")
```

6. Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below.

```
Enter a number: 7 
7---14---21---28---35
```

Code: 

```
x = int(input("Enter a number: "))
print(x, x*2, x*3, x*4, x*5, sep="---")
```

7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.

Code: 

```
weight_kg = float(input("Enter the weight in kilograms: "))

weight_pounds = weight_kg * 2.2

print(f"The weight in pounds is: {weight_pounds}" )
```

8. Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called `total` and `average` that hold the sum and average of the three numbers and print out the values of `total` and `average`.

Code: 

```
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

total = num1 + num2 + num3

average = total / 3

print("Total:", total)
print("Average:", average)
```

9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included.

Code: 
```
meal_price = float(input("Enter the price of the meal: $"))

tip_percent = float(input("Enter the tip percentage you want to leave (as a percentage): "))

tip_amount = meal_price * (tip_percent / 100)

total_bill = meal_price + tip_amount

print("Tip amount: $", format(tip_amount, ".2f"), sep="")
print("Total bill (with tip): $", format(total_bill, ".2f"), sep="")
```
