import string
import sys

def filterwords(s, n):
    """
    This program is a word filter, you must indicate any text to filter and the lengh of word.
    """
    words = [w.translate(s.maketrans("","",string.punctuation)) for w in s.split()]
    long_words = [w for w in words if len(w) > n]
    if len(long_words) == 0:
        print("No words under this condition.")
        return
    print(long_words)



if __name__ == "__main__":
    if len(sys.argv) == 3:
        s = sys.argv[1]
        n = sys.argv[2]         
        if n.isdigit() or not s.isdigit:
            filterwords(s, int(n))
        else:
            print("ERROR")
    elif len(sys.argv) == 1:
        print("ERROR")
    else:
        print("ERROR")