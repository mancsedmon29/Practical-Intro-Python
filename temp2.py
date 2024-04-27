temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9 / 5 * temp + 32
if f_temp > 212:
    print("That temperature is above the boiling point.")
elif f_temp < 32: 
    print("The temperature is below the freezing point.")