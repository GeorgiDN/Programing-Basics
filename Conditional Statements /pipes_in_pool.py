V_volume_litters = int(input())
P1_debit_hour_first_pipe = int(input())
P2_debit_hour_second_pipe = int(input())
H_hours_worker_absent = float(input())

over_flow_liters = 0

first_pipe = P1_debit_hour_first_pipe * H_hours_worker_absent
second_pipe = P2_debit_hour_second_pipe * H_hours_worker_absent

total_water = first_pipe + second_pipe

filled_space = (total_water / V_volume_litters) * 100


first_pipe_contribution = (first_pipe / total_water) * 100

second_pipe_contribution = (second_pipe / total_water) * 100

if total_water > V_volume_litters:
    over_flow_liters = (total_water - V_volume_litters)

if total_water <= V_volume_litters:
    print(f"The pool is {filled_space:.2f}% full. Pipe 1: {first_pipe_contribution:.2f}%. Pipe 2:"
          f"{second_pipe_contribution:.2f}%.")
else:
    print(f"For {H_hours_worker_absent:.2f} hours the pool overflows with {over_flow_liters:.2f} liters.")
