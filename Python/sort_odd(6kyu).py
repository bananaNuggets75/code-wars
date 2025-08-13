""" Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0] """

def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])
    
    result = []
    odd_index = 0
    for num in source_array:
        if num % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(num)
    return result


# one liner LOL
"def sort_array(a): return [next(it) if x % 2 else x for it in [iter(sorted([n for n in a if n % 2]))] for x in a]"
