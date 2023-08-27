clients_men = int(input())
clients_women = int(input())
max_num_tables = int(input())

output = ""

for men in range(1, clients_men + 1):
    for women in range(1, clients_women + 1):
        if max_num_tables > 0:
            output += f"({men} <-> {women}) "
            max_num_tables -= 1

print(output)
