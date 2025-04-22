def is_palindrome(word):
    reversed_word = ""
    i = len(word) - 1
    while i >= 0:
        reversed_word = reversed_word + word[i]
        i = i - 1
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrome("madam")) 
print(is_palindrome("hello")) 
