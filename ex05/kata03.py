import sys
# Put this at the top of your kata03.py file
kata = "The right format"

def kata_do():
    print(f"{kata:->42}", end="")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        kata_do()
    elif sys.argv[1] == "new_string":
        print(f"Enter a string")
        kata = str(input())
        kata_do()
    else:
        print("Error: Too many arguments")