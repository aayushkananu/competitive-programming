def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i+1
        j = j-1
    return True

print(is_palindrome("civic")) 
print(is_palindrome("level")) 
print(is_palindrome("a"))
print(is_palindrome("programming"))    