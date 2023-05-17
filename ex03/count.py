import sys
import string


# Define a function to check the text provided as a param.
def text_analyzer(str1=None):
    """
    This program count the characters given and counts by type.
    """
    # Repeat the input promt until a non-empty string is provided

    while True:
        while str1 is None or str1.strip() == "":
            str1 = input("Please enter a string: \n>>>> ")
        try:
            int(str1)
            print("Error: Argument must be a string.")
            str1 = input("Please enter a string: \n>>>> ")
        except ValueError:
            break

    # Declare empty counters 
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    # Sums characters 
    for char in str1:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punct_count += 1

    # Print results.
    print("The text contains", len(str1), "characters")
    print("Upper-case characters :", upper_count)
    print("Lower-case characters :", lower_count)
    print("Punctuation characters : ", punct_count)
    print("Spaces :", space_count)

if __name__ == "__main__":
    # If arguments are more than one, print error.
    if len(sys.argv) > 2:
        print("Error: Too many arguments")
    # If arguments are 2 (program.py and "text", do text_analizer)
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    # If any text is provided, the program will ask you for it
    else:
        str1 = None
        while str1 is None or str1.strip() == "":
            str1 = input("Please enter a string: \n>>>   ")
        text_analyzer(str1)

