sum_needed = int(input())

pay_cash_sum = 0
pay_credit_card_sum = 0
total_price_of_objects = pay_cash_sum + pay_credit_card_sum

cash_times_pay = 0
card_time_pay = 0

counter = 1

while total_price_of_objects < sum_needed:
    command = input()
    if command == 'End':
        break
    curr_price_object = int(command)
    if (counter % 2) != 0:
        if curr_price_object <= 100:
            pay_cash_sum += curr_price_object
            total_price_of_objects += curr_price_object
            cash_times_pay += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    elif (counter % 2) == 0:
        if curr_price_object >= 10:
            pay_credit_card_sum += curr_price_object
            total_price_of_objects += curr_price_object
            card_time_pay += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    counter += 1

average_cash_pay = pay_cash_sum / cash_times_pay
average_credit_card_pay = pay_credit_card_sum / cash_times_pay

if total_price_of_objects >= sum_needed:
    print(f"Average CS: {average_cash_pay:.2f}")
    print(f"Average CC: {average_credit_card_pay:.2f}")
else:
    print("Failed to collect required money for charity.")
