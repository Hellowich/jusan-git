def min_in_array():
    array_str = input().strip()
    if array_str == '[]':
        print(0)
    else:
        array_str = array_str.strip('[]')
        array = list(map(int, [s.strip() for s in array_str.split(',')]))
        print(min(array))
min_in_array()
