def is_palindrome_recursive(word, low_index, high_index):
    if not type(low_index) == int or not type(high_index) == int or len(word)<=0:
        return False
    if word[low_index] != word[high_index]:
        return False
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)