def find_duplicate(nums):
    if nums == '' or len(nums) < 2:
        return False
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_duplicate = False
    for numb in numbers:
        contador = nums.count(numb)
        if contador > 1:
            is_duplicate = numb
    return is_duplicate
