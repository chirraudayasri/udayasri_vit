def count_multiples(numbers):
    # Initialize a dictionary to store the counts
    counts = {i: 0 for i in range(1, 10)}
    
    # Iterate through the range 1 to 9
    for i in range(1, 10):
        # Count multiples of i in the list
        counts[i] = sum(1 for num in numbers if num % i == 0)
    
    return counts

# Example input
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Get the result
result = count_multiples(input_list)

# Print the output
print(result)
