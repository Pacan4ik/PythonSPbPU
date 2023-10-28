money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
increase_coefficient = 1 + increase
debt = spend - salary


while debt <= money_capital:
    months += 1
    money_capital -= debt
    spend *= increase_coefficient
    debt = spend - salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
