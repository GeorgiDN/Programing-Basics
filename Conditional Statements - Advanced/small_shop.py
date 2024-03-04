product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = quantity * 0.50
    elif product =='water':
        price = quantity * 0.80
    elif product =='beer':
        price = quantity * 1.20
    elif product =='sweets':
        price = quantity * 1.45
    elif product =='peanuts':
        price = quantity * 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price = quantity * 0.40
    elif product == 'water':
        price = quantity * 0.70
    elif product == 'beer':
        price = quantity * 1.15
    elif product == 'sweets':
        price = quantity * 1.30
    elif product == 'peanuts':
        price = quantity * 1.50
elif city == 'Varna':
    if product == 'coffee':
        price = quantity * 0.45
    elif product == 'water':
        price = quantity * 0.70
    elif product == 'beer':
        price = quantity * 1.10
    elif product == 'sweets':
        price = quantity * 1.35
    elif product == 'peanuts':
        price = quantity * 1.55

print(price)




# product = input()
# city = input()
# quantity = float(input())

# info = {"Sofia": {
#     "coffee": 0.50,
#     "water": 0.80,
#     "beer": 1.20,
#     "sweets": 1.45,
#     "peanuts": 1.60,
#     },
#     "Plovdiv": {
#         "coffee": 0.40,
#         "water": 0.70,
#         "beer": 1.15,
#         "sweets": 1.30,
#         "peanuts": 1.50,
#     },
#     "Varna": {
#         "coffee": 0.45,
#         "water": 0.70,
#         "beer": 1.10,
#         "sweets": 1.35,
#         "peanuts": 1.55,
#     }
# }


# price = info[city][product] * quantity
# print(price)




# Do not do this!

# product, city, quantity = input(), input(), float(input())
# print(quantity * 0.50 if city == 'Sofia' and product == 'coffee' 
#       else quantity * 0.80 if city == 'Sofia' and product == 'water'
#       else quantity * 1.20 if city == 'Sofia' and product == 'beer'
#       else quantity * 1.45 if city == 'Sofia' and product == 'sweets'
#       else quantity * 1.60 if city == 'Sofia' and product == 'peanuts'
#       else quantity * 0.40 if city == 'Plovdiv' and product == 'coffee'  
#       else quantity * 0.70 if city == 'Plovdiv' and product == 'water'
#       else quantity * 1.15 if city == 'Plovdiv' and product == 'beer'
#       else quantity * 1.30 if city == 'Plovdiv' and product == 'sweets'
#       else quantity * 1.50 if city == 'Plovdiv' and product == 'peanuts'
#       else quantity * 0.45 if city == 'Varna' and product == 'coffee'  
#       else quantity * 0.70 if city == 'Varna' and product == 'water'
#       else quantity * 1.10 if city == 'Varna' and product == 'beer'
#       else quantity * 1.35 if city == 'Varna' and product == 'sweets'
#       else quantity * 1.55 if city == 'Varna' and product == 'peanuts'
#       else "")
