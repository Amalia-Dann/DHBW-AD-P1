is_palindrome = lambda s: s == s[::-1]
word = input("Gib ein Wort ein, welches du testen möchtest: ")
print(is_palindrome(word))
