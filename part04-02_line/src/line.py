def line(length, word):
    if len(word) == 0:
        print("*" * length)
    else:
        print(word[0] * length)

if __name__ == "__main__":
    line(5, "x")