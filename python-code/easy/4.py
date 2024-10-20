def print_even_a_b():
    a, b = map(int, input().split())
    start = a if a % 2 == 0 else a + 1
    for i in range(start, b + 1, 2):
        print(i, end=' ')
    print()
print_even_a_b()
