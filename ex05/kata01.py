import sys

kata = {
    'Python': 'Guido van Rossum', 
    'Ruby': 'Yukihiro Matsumoto', 
    'PHP': 'Rasmus Lerdorf' 
}

def kata_do():
    s = ""
    for key, value in kata.items():
        s += f"\n{key} was created by {value}, " 
    print(f"There are {len(kata)} languages: {s[:-2]}")
    return

if __name__ == "__main__":
    if len(sys.argv) == 1:
            if len(kata) == 0:
                print("Error: The tuple is empty.")
            else:
                kata_do()
    elif len(sys.argv) > 1 and sys.argv[1] == "new_dictionary":
        kata = dict(x.split(":") for x in input("Enter the key-value pairs separated by commas: ").split(","))
        kata_do()
    else:
        print("Error: Too many arguments")
