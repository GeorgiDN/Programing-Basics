# https://judge.softuni.org/Contests/Practice/Index/2275#6
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/8864

days = int(input())
total_quantity_of_food = float(input())
dog_total_food_eaten = 0
cat_total_food_eaten = 0
total_biscuits = 0
total_food_eaten = 0


for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    dog_total_food_eaten += dog_food
    cat_total_food_eaten += cat_food
    total_food_eaten += cat_food + dog_food

    if day % 3 == 0:
        total_food_per_day = dog_food + cat_food
        biscuits = total_food_per_day * 0.1
        total_biscuits += biscuits

percent_total_food_eaten = (total_food_eaten / total_quantity_of_food) * 100
percent_dog_total_food_eaten = (dog_total_food_eaten / total_food_eaten) * 100
percent_cat_total_food_eaten = (cat_total_food_eaten / total_food_eaten) * 100
total_biscuits = round(total_biscuits)

print(f"Total eaten biscuits: {total_biscuits}gr.\n"
      f"{percent_total_food_eaten:.2f}% of the food has been eaten.\n"
      f"{percent_dog_total_food_eaten:.2f}% eaten from the dog.\n"
      f"{percent_cat_total_food_eaten:.2f}% eaten from the cat.")
