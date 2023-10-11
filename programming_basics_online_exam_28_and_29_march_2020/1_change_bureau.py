# https://judge.softuni.org/Contests/Practice/Index/2275#1
# https://judge.softuni.org/Contests/Practice/DownloadResource/8853

price_per_bitcoin = 1168
price_per_chineese_uan = 0.15
price_per_dolar = 1.76
price_per_euro = 1.95

bitcoins = int(input())
chineese_uan = float(input())
commission = float(input())
commission_percent = commission / 100

bitcoin_sum_lv = bitcoins * price_per_bitcoin
sum_chineese_uan_dollars = chineese_uan * price_per_chineese_uan
sum_chineese_uan_lv = sum_chineese_uan_dollars * price_per_dolar

total_sum_lv = bitcoin_sum_lv + sum_chineese_uan_lv
total_sum_euro = total_sum_lv / price_per_euro

total_sum_euro -= total_sum_euro * commission_percent
print(f"{total_sum_euro:.2f}")
