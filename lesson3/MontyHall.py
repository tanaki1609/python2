import random
opened_doors = [0, 0, 0]
prized_doors = [0, 0, 0]
comp_choice = random.randint(0, 2)
user_choice = int(input('Enter a number: '))
prized_doors[comp_choice] = 1
opened_doors[user_choice] = 1
doors = []
for i in range(3):
    if opened_doors[i] == 0 and prized_doors[i] == 0:
        doors.append(i)
opened_door = random.choice(doors)
opened_doors[opened_door] = -1
prized_doors[opened_door] = -1
print('your choice', opened_doors)
print('comp choice', prized_doors)
change_door = int(input('Do you want to change the door: [0,1]'))
is_winner = -1

if change_door == 1:
    for i in range(3):
        if opened_doors[i] == 0:
            is_winner = (prized_doors[i])
            break
if change_door == 0:
    is_winner = (prized_doors[user_choice])
if is_winner:
    print('you win')
else:
    print('you loose')

