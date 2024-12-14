def generate_series(a):
    if a <= 0:
        return []  
    # Return an empty list for invalid input

    series = [2 * i + 1 for i in range(a)]
    return series
    #Here we are taking as odd interger

# Example usage:
try:
    # Take input from the user
    result = generate_series(a)
    print(", ".join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter an integer.")
