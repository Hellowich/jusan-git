import ast

def is_perfectly_balanced(array):
    total_sum = sum(array)
    left_sum = 0
    for num in array:
        total_sum -= num
        if left_sum == total_sum:
            return True
        left_sum += num
    return False

array = ast.literal_eval(input())

if is_perfectly_balanced(array):
    print("true")
else:
    print("false")
