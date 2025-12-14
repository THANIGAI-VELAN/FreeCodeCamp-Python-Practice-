def number_pattern(n):
    # Check if n is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if n is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Generate the pattern using a for loop
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " "
    
    # Remove the trailing space
    return result.rstrip()
