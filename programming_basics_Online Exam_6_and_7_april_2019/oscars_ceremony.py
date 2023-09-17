def ceremony_expenditures(price):
    statuettes = price * 0.7
    kettering = statuettes * 0.85
    voiceover = kettering * 0.5

    total_price = price + statuettes + kettering + voiceover
    print(f"{total_price:.2f}")

rent = int(input())
ceremony_expenditures(rent)
