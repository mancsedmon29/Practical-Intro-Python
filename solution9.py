def fibonacci(n):
    fibonacci_sequence = [1, 1] 

    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  
        fibonacci_sequence.append(next_number) 

    return fibonacci_sequence

n = int(input("How many Fibonacci numbers do you want to print? "))

print("Fibonacci sequence:")
for number in fibonacci(n):
    print(number, end=", ")
