from collections import Counter
def is_anagram(s,t):
    return Counter(s) == Counter(t)
def valid_anagram(s,t):
    flag = True
    if len(s) != len(t):
        flag = False
    else:
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(letter) != t.count(letter):
                flag = False
                break
    return flag

if __name__ == "__main__":
    s="anagram"
    t="nagaram"
    print(is_anagram(s,t))
    print(valid_anagram(s,t))