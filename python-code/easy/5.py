def pow_a_b():
    a, b = map(int, input().split())
    result = 1
    for _ in range(b):
        result *= a
    print(result)
pow_a_b()
