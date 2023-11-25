print("-*-" * 40)

name = input("Enter mame >>>").strip().title()

user_age = input("Enter age >>>")
user_age = int(user_age)

average_salary = input("Enter average salary >>>")
average_salary = float(average_salary)

retirement_age = 65

years_till_retirement = retirement_age - user_age

print(years_till_retirement)

total_money = years_till_retirement * 12 * average_salary
currency_rate = 37.3
usd_amount = total_money / currency_rate
usd_amount = round(usd_amount, 0)

print(usd_amount)

cars_quantity = usd_amount // 31500

print(cars_quantity)

user_name = "Arthur"

usd_amount = 94102
cars_quantity = 2.0

text = f""" I\'m {user_name} is able to earn {usd_amount} dollars
only which is enough for {cars_quantity}
Toyota cars it don\'t suits to\nme that is why
i\'ll change my life\nand study programming hardy """

print(text)
