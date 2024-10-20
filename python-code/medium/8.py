month = int(input("Введите номер месяца (1-12): "))
day = int(input("Введите день (1-31): "))

if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day <= 19):
    season = "зима"
elif (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day <= 20):
    season = "весна"
elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 22):
    season = "лето"
elif (month == 9 and day >= 23) or (month in [10, 11]) or (month == 12 and day <= 20):
    season = "осень"
else:
    season = "Некорректная дата"

print(f"Дата относится к сезону: {season}.")
