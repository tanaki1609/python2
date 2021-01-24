import random


class Game:
    list_of_choices = ['rock', 'scissors', 'paper']

    def __init__(self):
        self.your_choice = int(input('Enter number: [0,1,2] '))
        print('Your choice is', self.list_of_choices[self.your_choice])
        self.comp_choice = random.randint(0, 2)
        print('Computer choice is', self.list_of_choices[self.comp_choice])

    def get_winner(self):
        if self.your_choice == self.comp_choice:
            print('You DRAW')
        elif self.your_choice == 0 and self.comp_choice == 1:
            print('You winner')
        elif self.your_choice == 0 and self.comp_choice == 2:
            print('You loser')
        elif self.comp_choice == 0 and self.your_choice == 1:
            print('You loser')
        elif self.comp_choice == 0 and self.your_choice == 2:
            print('You winner')


game = Game()
game.get_winner()
