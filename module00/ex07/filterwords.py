import sys

def filter_words(text, n):
    words = text.split()
    filtered_words = [word for word in words if len(word) > n]
    return " ".join(filtered_words)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} '<text>' <n>")
        sys.exit(1)
    else:
        text = sys.argv[1]
        try:
            n = int(sys.argv[2])
            result = filter_words(text, n)
            print(result)
        except ValueError:
            print("Error: n must be an integer.")

if __name__ == "__main__":
    main()