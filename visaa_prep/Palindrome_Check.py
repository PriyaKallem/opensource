def is_palindrome(s):
    return s == s[::-1]
s=input()
if is_palindrome(s):
    print("TRUE")
else:
    print("FALSE")
