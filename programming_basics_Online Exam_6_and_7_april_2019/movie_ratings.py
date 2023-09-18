number_films = int(input())
film_ratings = {}

for num in range(number_films):
    film = input()
    rating = float(input())

    film_ratings[film] = rating

highest_rating_film = max(film_ratings, key=film_ratings.get)
max_rating = film_ratings[highest_rating_film]

lowest_rating_film = min(film_ratings, key=film_ratings.get)
min_rating = film_ratings[lowest_rating_film]

ratings = list(film_ratings.values())
average_rating = sum(ratings) / len(ratings)

print(f"{highest_rating_film} is with highest rating: {max_rating:.1f}\n"
      f"{lowest_rating_film} is with lowest rating: {min_rating:.1f}\n"
      f"Average rating: {average_rating:.1f}")
