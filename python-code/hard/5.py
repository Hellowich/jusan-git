import ast

def median(array):
    array.sort()
    mid = (len(array) - 1) // 2
    return array[mid]

array = ast.literal_eval(input())
print(median(array))
