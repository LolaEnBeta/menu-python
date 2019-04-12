
import random

week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

with open("menu-list.txt", "r") as menus:
    meals = []
    for meal in menus:
        meals.append(meal.split())

for day in week:
    random.shuffle(meals)
    print(day, "\n", meals.pop())
    