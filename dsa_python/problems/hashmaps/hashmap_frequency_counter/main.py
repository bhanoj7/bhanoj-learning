from collections import Counter

def count_frequency(arr):
    return Counter(arr)

if __name__ == "__main__":
    print(count_frequency(["apple", "banana", "apple", "orange", "banana", "apple"]))
