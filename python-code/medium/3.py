number = int(input("Введите число: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Число не является простым.")
            break
    else:
        print("Число является простым.")
else:
    print("Число не является простым.")
