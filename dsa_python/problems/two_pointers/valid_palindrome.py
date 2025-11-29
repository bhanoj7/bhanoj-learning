def isPalindrome(s):
    start = 0
    end = len(s) - 1
    s = s.lower()
    while start < end:
        if s[start].isalnum() and s[end].isalnum():
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        else:
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1
    return True
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))