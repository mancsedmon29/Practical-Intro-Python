# Define the sequence of letters
sequence = "AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG"

# Four nested for loops to print the sequence
for i in range(0, 10):
    print(sequence[i], end="")
for j in range(10, 18):
    print(sequence[j], end="")
for k in range(18, 25):
    print(sequence[k], end="")
for l in range(25, len(sequence)):
    print(sequence[l], end="")