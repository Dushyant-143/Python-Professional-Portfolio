def factorial(n: int) -> int:
    """Calculate factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = factorial(number)
        print(f"Factorial of {number} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Invalid input. Please enter a valid integer.")
