#https://judge.softuni.org/Contests/Practice/Index/1745#9

word = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
most_powerful_word = ''
max_power_word = 0
current_word_sum = 0

while word != "End of words":

    for letter in word:
        current_word_sum += ord(letter)

    if word[0].lower() in vowels:
        current_word_sum *= len(word)
    else:
        current_word_sum //= len(word)

    if current_word_sum > max_power_word:
        max_power_word = current_word_sum
        most_powerful_word = word

    current_word_sum = 0
    word = input()

print(f"The most powerful word is {most_powerful_word} - {max_power_word}")
