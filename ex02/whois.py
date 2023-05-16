import sys

# Define a function to check if a number is odd, even, or zero
def whois(number):
    if number == 0:
        return "This number is Zero."
    elif number % 2 == 0:
        return "This number is Even."
    else:
        return "This number is Odd."


# Check if there are any arguments
if len(sys.argv) == 1:
    print("Usage: python3 program.py [number] ** No params provided")
# Check if there are too many arguments
elif len(sys.argv) > 2:
    print("Error. too many arguments.")
else:
    try:
        number = int(sys.argv[1])

        result = whois(number)
        print(result)
    except (ValueError, IndexError):
        print("Error: Argument must be an integer")