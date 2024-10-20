import ast

m = int(input())
s = ast.literal_eval(input())

index_map = {}
for i, num in enumerate(s):
    complement = m - num
    if complement in index_map:
        idx1, idx2 = index_map[complement], i
        print(' '.join(map(str, sorted([idx1, idx2]))))
        break
    index_map[num] = i
