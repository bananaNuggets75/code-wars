def array_plus_array(arr1,arr2):
    total = 0
    for x in arr1:
        total += x
    for y in arr2:
        total += y
    return total

#or 
""" def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2) """