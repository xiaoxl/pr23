import random
# %%
results = {'remain': 0, 'switch': 0}
N=4

doors = list(range(1, N+1))
# %%
door_with_car = random.choice(doors)
initial_choice = random.choice(doors)
# %%
rest_doors = doors[:]
if door_with_car == initial_choice:
    rest_doors.remove(door_with_car)
    door_host_open = random.sample(rest_doors, N-2)
elif door_with_car != initial_choice:
    rest_doors.remove(door_with_car)
    rest_doors.remove(initial_choice)
    door_host_open = random.sample(rest_doors, N-2)

tmpdoors = doors[:]
tmpdoors.remove(initial_choice)
for door in tmpdoors:
    tmpdoors.remove(door)
door_unopened = tmpdoors[0]

if door_with_car == initial_choice:
    winner = 'remain'
elif door_with_car == door_unopened:
    winner = 'switch'
