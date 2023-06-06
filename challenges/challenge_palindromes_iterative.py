def is_palindrome_iterative(word):
    if len(word) <= 0:
        return False
    reversed_word = word[::-1]
    if word != reversed_word:
        return False
    return True
