number = int(input("Введите число: "))
divisors_sum = 0

for i in range(1, number):
    if number % i == 0:
        divisors_sum += i

if divisors_sum == number:
    print(f"{number} является совершенным числом.")
else:
    print(f"{number} не является совершенным числом.")
