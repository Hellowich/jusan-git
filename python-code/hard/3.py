def swap_bits(a):
    return ((a & 0x0F) << 4) | ((a & 0xF0) >> 4)

a = int(input())
result = swap_bits(a)
print(result)
