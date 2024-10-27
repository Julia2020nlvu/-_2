salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0

for months in range(1, months + 1):
    remains_of_spend = spend - salary
    if remains_of_spend > 0:
        money_capital+= remains_of_spend
        spend *= 1 + increase

money_capital = int(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)


