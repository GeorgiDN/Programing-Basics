command = input()
word = ''
secret_command_c = 0
secret_command_o = 0
secret_command_n = 0
words = []
last_word = ''

while command != 'End':
    if command.isalpha():
        if secret_command_c >= 1 and secret_command_o >= 1 and secret_command_n >= 1:
            word += ' '
            secret_command_c = 0
            secret_command_o = 0
            secret_command_n = 0
            if last_word:
                words.append(last_word.strip())
            last_word = word.strip()
            word = ''
        if command == 'c':
            secret_command_c += 1
            if secret_command_c > 1:
                word += command
        elif command == 'o':
            secret_command_o += 1
            if secret_command_o > 1:
                word += command
        elif command == 'n':
            secret_command_n += 1
            if secret_command_n > 1:
                word += command
        else:
            word += command

    command = input()

if secret_command_c >= 1 and secret_command_o >= 1 and secret_command_n >= 1:
    word += ' '
    words.append(last_word.strip())
    last_word = word.strip()

if last_word:
    words.append(last_word.strip())

print(' '.join(words))
