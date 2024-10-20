import ast

array1 = ast.literal_eval(input())
array2 = ast.literal_eval(input())

missing_numbers = sorted(set(array2) - set(array1))
print(missing_numbers)
