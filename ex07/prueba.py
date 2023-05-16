import string
import sys

def filterwords(s, n):
    words = [w.translate(str.maketrans("", "", string.punctuation)) for w in s.split()]
    long_words = [w for w in words if len(w) > n]
    print(long_words)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid argument type.\nUsage: python3 program.py <string> <integer>")
    # If arguments are 2 (program.py and "text", do text_analizer)
    else:
        s = sys.argv[1]
        n = int(sys.argv[2])
        filterwords(s, n)