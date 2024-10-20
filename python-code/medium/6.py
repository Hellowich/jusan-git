number = 25
a, b = 0, 1

while b < number:
    a, b = b, a + b

if b == number or number == 0:
    print(f"{number} является числом Фибоначчи.")
else:
    print(f"{number} не является числом Фибоначчи.")
