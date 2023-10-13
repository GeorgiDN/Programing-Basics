# https://judge.softuni.org/Contests/Practice/Index/1538#2
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5337

final_result = {'won': 0, "lost": 0, 'draw': 0}

for i in range(3):
    result = list(map(int, input().split(":")))
    host_result = result[0]
    guests_result = result[1]

    if host_result > guests_result:
        final_result['won'] += 1
    elif host_result < guests_result:
        final_result['lost'] += 1
    else:
        final_result['draw'] += 1

print(f"Team won {final_result['won']} games.\n"
      f"Team lost {final_result['lost']} games.\n"
      f"Drawn games: {final_result['draw']}")
