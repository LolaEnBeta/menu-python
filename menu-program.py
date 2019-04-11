import random

week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

with open("menu-list.txt", "r") as menus:
    for meal in menus:
        meal = meal.split("; ")
        print(meal)


for day in week:
    print(day, "\n", random.choice(meal))

