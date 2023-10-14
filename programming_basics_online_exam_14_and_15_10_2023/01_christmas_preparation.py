paper_price_per_roll = 5.80
cloth_price_per_roll = 7.20
glue_price_per_litter = 1.20

paper_rolls_number = int(input())
cloth_rolls_number = int(input())
litters_glue = float(input())
reduction = int(input())
reduction_percent = reduction / 100

paper_rolls_price = paper_rolls_number * paper_price_per_roll
rolls_price = cloth_rolls_number * cloth_price_per_roll
glue_price = litters_glue * glue_price_per_litter
total_price = paper_rolls_price + rolls_price + glue_price

total_price_with_reduction = total_price - (reduction_percent * total_price)

print(f"{total_price_with_reduction:.3f}")
