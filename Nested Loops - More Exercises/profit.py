one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_banknotes = int(input())
target_sum = int(input())

for i in range(one_lv_coins + 1):
    for j in range(two_lv_coins + 1):
        for k in range(five_lv_banknotes + 1):
            current_sum = i + 2*j + 5*k
            if current_sum == target_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {current_sum} lv.")
              
