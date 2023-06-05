
def custom_sort(arr):
    array_min = arr.lower()
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    array = []
    for letter in alfabeto:
        contador = array_min.count(letter)
        array.extend([letter] * contador)
    return ''.join(array)


def is_anagram(first_string, second_string):
    ordered_first = []
    ordered_second = []
    ordered_first = custom_sort(first_string)
    ordered_second = custom_sort(second_string)
    check = True
    if (ordered_first != ordered_second or len(first_string)
            != len(second_string)):
        check = False
    if first_string == '' or second_string == '':
        check = False
    join_first = ''.join(ordered_first)
    join_second = ''.join(ordered_second)
    return (join_first, join_second, check)
