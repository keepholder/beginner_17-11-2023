string = "6..58київ\nоДеса   Львів\tжитоМИР   уЖгОрОд ХарКІВ    слАвУтИч74$:?$"

list_of_cities = string.strip("6..5874$:?$").title().split()

for city in list_of_cities:
    print(f"Я \U00002764 {city}")
