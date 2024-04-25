def range_ten_from_seven(n=7):
    if n + 10 > 1000:
        print(n)
        return
    else:
        print(n)
        range_ten_from_seven(n + 10)


range_ten_from_seven()


# for num in range(7, 1000, 10):
#     print(num)
