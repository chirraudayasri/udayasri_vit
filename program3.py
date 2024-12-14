def generate_series(a):
    # Determine the number of odd numbers to generate
    n = a if a % 2 != 0 else a - 1
    
    # Generate the first n odd numbers
    series = [2 * i + 1 for i in range(n)]
    return series

# Input from the user
a = int(input("Enter a number: "))
output = generate_series(a)

# Print the output as a comma-separated string
print(", ".join(map(str, output)))
