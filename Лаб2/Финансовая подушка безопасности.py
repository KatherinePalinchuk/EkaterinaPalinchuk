money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
total = 0

while True:
    difference = spend - salary
    if money_capital < difference:
        break
    total += 1
    spend *= increase + 1
    money_capital -= difference
print("Количество месяцев, которое можно протянуть без долгов:", total)
