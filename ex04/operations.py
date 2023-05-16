import sys

def do_op(str1=None, str2=None):
    """
    This program do math operations with 2 arguments
    """
    while str1 is None or str2 is None or str1.strip() == "" or str2.strip() == "":
        str1 = input("Write first number:  ")
    while str2 is None or str2.strip() == "":    
        str2 = input("Write second number:  ")

    if not str1.lstrip('-').isdigit() or not str2.lstrip('-').isdigit():
        print("Usage: python3 my_program.py [numer1] [number2]")
        print("Error: arguments must be two numbers")
        return ValueError
    num1 = int(str1)
    num2 = int(str2)

    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)
    if num2 == 0:
        print("Quotient: ERROR (division by zero)")
    else:
        print("Quotient:", num1 / num2)
    if num2 == 0:
        print("Remainder : ERROR (modulo by zero)")
    else:
        print("Remainder:", num1 % num2)

if __name__ == "__main__":
    if len(sys.argv) > 3:
            print("error: Too many arguments")
    elif len(sys.argv) == 3:
            do_op(sys.argv[1], sys.argv[2])
    elif len(sys.argv) < 3:
        str1 = None
        str2 = None
        while str1 is None or str1.strip() == "":
            str1 = input("Please provide a number as first parameter:  ")
        while str2 is None or str2.strip() == "":
            str2 = input("Please provide a number as second parameter:  ")
        do_op(str1, str2)