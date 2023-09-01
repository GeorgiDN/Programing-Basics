import string
from string import ascii_letters, digits
import random

password_sign = ascii_letters + digits
password_length = 10

password = ''.join(random.sample(password_sign, password_length))

print('Your new generated password is:', password)
