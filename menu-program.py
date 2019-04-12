
import random

week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
weekend = ["SATURDAY", "SUNDAY"]

with open("menu-list.txt", "r") as menus:
    meals = []
    for meal in menus:
        meals.append(meal.split())

with open("weekend_menu.txt", "r") as weekend_menus:
    weekend_meals = []
    for meal in weekend_menus:
        weekend_meals.append(meal.split())

for day in week:
    random.shuffle(meals)
    print(day, "\n", meals.pop())
    
for day in weekend:
    random.shuffle(weekend_meals)
    print(day, "\n", "Lunch", "\n", weekend_meals.pop(), "\n", "Dinner", "\n", weekend_meals.pop())
