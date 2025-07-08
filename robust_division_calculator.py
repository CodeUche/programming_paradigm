def safe_divide(numerator, denominator):
    # Return division
    try:

        # Convert input to float
        num = float(numerator)
        den = float(denominator)
        
        # handle division by zero
        if den == 0:
            return "Error: Not divisible by zero."
        
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numbers only."