def calc_deposit():
    month_of_str, rate_str, balance_str = input().split() # тут я использовал явное считывание ввода в строки а затем преобразовал в нужный тип данных 
    month_of = int(month_of_str)
    rate = float(rate_str)
    balance = float(balance_str)
    for _ in range(month_of):
        balance += balance * (rate / 100)
    print(balance)
calc_deposit()
