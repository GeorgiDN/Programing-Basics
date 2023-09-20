pictures_time = int(input())
scenes = int(input())
duration_scene = int(input())

area_prepare = pictures_time * 0.15

total_time = duration_scene * scenes + area_prepare
diff = abs(total_time - pictures_time)
diff = round(diff)

if total_time < pictures_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")
