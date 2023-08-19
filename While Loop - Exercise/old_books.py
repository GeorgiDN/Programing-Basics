ani_book = input()
curr_book = input()
counter = 0

is_found = False

while curr_book != 'No More Books':
    if curr_book == ani_book:
        is_found = True
        print(f"You checked {counter} books and found it.")
        break

    counter += 1
    curr_book = input()

if not is_found:
    print('The book you search is not here!')
    print(f"You checked {counter} books.")
