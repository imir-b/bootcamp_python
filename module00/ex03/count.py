import sys
import string

def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    
    if text is None:
        text = input("Please provide a string to analyze.\n")

    printcount = 0
    uppercount = 0
    lowercount = 0
    punctcount = 0
    spacecount = 0

    for char in text:
        if char.isprintable():
            printcount += 1
        if char.isupper():
            uppercount += 1
        if char.islower():
            lowercount += 1
        if char in string.punctuation:
            punctcount += 1
        if char.isspace():
            spacecount += 1
    print("This text contains", int(printcount), "printables character(s):")
    print("-", int(uppercount), "upper letter (s)")
    print("-", int(lowercount), "lower letter(s)")
    print("-", int(punctcount), "ponctuation mark(s)")
    print("-", int(spacecount), "space(s)")


if __name__ == "__main__":
    if len(sys.argv) > 2 :
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if len(sys.argv) < 2 :
        text_analyzer()
    else :
        text_analyzer(sys.argv[1])
