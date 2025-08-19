import math

def math_operations(num: float) -> dict:
    """Perform square root, natural log, and sine on the given number."""
    if num <= 0:
        raise ValueError("Number must be positive for sqrt and log operations.")

    return {
        "Square Root": math.sqrt(num),
        "Natural Logarithm": math.log(num),
        "Sine (radians)": math.sin(num)
    }


if __name__ == "__main__":
    try:
        number = float(input("Enter a number: "))
        results = math_operations(number)

        print(f"\nResults for number {number}:")
        for operation, value in results.items():
            print(f"{operation}: {value:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Invalid input. Please enter a valid number.")
