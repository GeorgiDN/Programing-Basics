def character_sequence(n=0):
    if n == len(text):
        return
    else:
        print(text[n])
        return character_sequence(n+1)


text = input()
character_sequence()


# word = input()
# for ch in word:
#     print(ch)
