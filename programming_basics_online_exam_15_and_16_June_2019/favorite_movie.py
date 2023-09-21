#https://judge.softuni.org/Contests/Practice/Index/1699#9
from sys import maxsize

max_points = - maxsize
highest_points_film = ''
curr_points = 0
max_films = 7
total_points = 0
max_films_condition = False

while True:
    if max_films == 0:
        max_films_condition = True
        break

    film = input()
    if film == 'STOP':
        break

    max_films -= 1
    total_points = 0
    for char in film:
        curr_points = (ord(char))
        if char.isupper():
            curr_points -= len(film)
        elif char.islower():
            curr_points -= 2*(len(film))
        total_points += curr_points

    if total_points > max_points:
        max_points = total_points
        highest_points_film = film

if not max_films_condition:
    print(f"The best movie for you is {highest_points_film} with {max_points} ASCII sum.")

elif max_films_condition:
    print("The limit is reached.")
    print(f"The best movie for you is {highest_points_film} with {max_points} ASCII sum.")
  
