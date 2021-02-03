import random


class MontyHall:
    def __init__(self):
        self.opened_doors = [0, 0, 0]
        self.prized_doors = [0, 0, 0]
        self.comp_choice = random.randint(0, 2)
        self.user_choice = random.randint(0, 2)
        self.prized_doors[self.comp_choice] = 1
        self.opened_doors[self.user_choice] = 1

    def open_unprized_door(self):
        doors = []
        for i in range(3):
            if self.opened_doors[i] == 0 and self.prized_doors[i] == 0:
                doors.append(i)
        self.opened_door = random.choice(doors)
        self.opened_doors[self.opened_door] = -1
        self.prized_doors[self.opened_door] = -1

    def changing_door(self):
        self.change_door = 1
        self.is_winner = -1

        if self.change_door == 1:
            for i in range(3):
                if self.opened_doors[i] == 0:
                    self.is_winner = (self.prized_doors[i])
                    break
        if self.change_door == 0:
            self.is_winner = (self.prized_doors[self.user_choice])
        if self.is_winner:
            return 1
        else:
            return 0


counter = 0
for i in range(10000):
    monty_hall = MontyHall()
    monty_hall.open_unprized_door()
    counter += monty_hall.changing_door()
print(counter)
