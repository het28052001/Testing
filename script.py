import sys

def add_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)

    try:
        number1 = float(sys.argv[1])
        number2 = float(sys.argv[2])
    except ValueError:
        print("Please provide two valid numbers.")
        sys.exit(1)

    result = add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}.")