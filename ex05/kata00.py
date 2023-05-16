import sys

kata = (19,42,21)

def kata_do():

    s = str(kata[0])
    for i in range(1, len(kata)):
        s = s  + ', ' + str(kata[i])
    print(f"There are {len(kata)} numbers : {s}")
    return

if __name__ == "__main__":
    if len(sys.argv) == 1:
        if len(kata) == 0:
            print("Error: The tuple is empty.")
        else:
            kata_do()
    else:
        print("Error: Too many arguments")