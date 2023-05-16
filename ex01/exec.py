import sys

def reverse_swap(string):
    """
    Esta función toma una cadena como argumento, invierte la cadena y cambia el caso de cada letra.
    Devuelve la cadena invertida y con el caso cambiado.
    """
    reversed_string = string[::-1]
    swapped_string = reversed_string.swapcase()
    return swapped_string

# Get the command-line arguments
args = sys.argv[1:]
if len(args) == 0:
    print("Usage: python3 program.py [string] ** No params provided **")
else:
    # Merge the arguments into a single string
    string = " ".join(args)
    # Reverse and swap the case of the string
    result = reverse_swap(string)
    # Print the result
    print(result)