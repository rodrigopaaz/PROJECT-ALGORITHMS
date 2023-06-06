def find_duplicate(nums):
    if nums == '':
        return False
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_duplicate = False
    for numb in numbers:
        contador = nums.count(numb)
        if contador > 1:
            is_duplicate = numb
    print(is_duplicate)
    return is_duplicate
