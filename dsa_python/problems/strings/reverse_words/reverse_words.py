def reverse_words(s):
    return " ".join(reversed(s.split()))
if __name__ == "__main__":
    s = "Namaskaram Anna"
    print(reverse_words(s))