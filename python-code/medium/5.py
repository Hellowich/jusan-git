for number in range(1, 1001):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    if divisors_sum == number:
        print(f"{number} является совершенным числом.")
