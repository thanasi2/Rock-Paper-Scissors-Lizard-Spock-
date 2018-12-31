#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']



class Player:

    def move():
        return 'rock'

    def learn(self, move1, move2):
        pass


class random_player(Player):

    def move(self, round):
        return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


class method_player(Player):

    def move(self, round):
        for move in moves:
            return moves[round]


class human_player(Player):

    def move(self, round):
        while True:
            x = input("What's your move? ")
            lower = x.lower()
            if lower not in ('rock', 'paper', 'scissors', 'lizard', 'spock'):
                print('Sorry, that was not a valid input! Please try again!')
            else:
                return lower


class ReflectPlayer(Player):

    def learn(self, move1, move2):
        self.move2 = move2

    def move(self, round):
        if round == 0:
            return random.choice(moves)
        elif round >= 1:
            return self.move2


def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock') or
                (one == 'lizard' and two == 'spock') or
                (one == 'scissors' and two == 'lizard') or
                (one == 'lizard' and two == 'paper') or
                (one == 'paper' and two == 'spock') or
                (one == 'rock' and two == 'lizard') or
                (one == 'spock' and two == 'rock') or
                (one == 'spock' and two == 'scissors'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def win_lose(self, round, move1, move2, name):
        if move1 == move2:
            print("\nTie!")
            self.p1_score += 0
            self.p2_score += 0
        elif beats(move1, move2) is True:
            print(f"\n{name} wins this round!")
            self.p1_score += 1
        elif beats(move1, move2) is False:
            print("\nplayer 2 wins this round!")
            self.p2_score += 1
        input(f"""
{name} has {self.p1_score} point(s),
Player 2 has {self.p2_score} point(s)...
Press enter to continue!""")

    def play_round(self, round, name):
        move1 = self.p1.move(round)
        move2 = self.p2.move(round)
        print(f"\n{name}: {move1}  Player 2: {move2}")
        self.p2.learn(move2, move1)
        self.win_lose(round, move1, move2, name)

    def play_game(self):
        name = input("""Welcome to Rock, Paper , Scissors , Lizard , Spock!
What is your name? """)
        input(f"""
Thanks for playing {name}!

Before we begin let's gover over a few rules!
Press enter to continue! """)
        input("""
RULES

*All inputs must be made in lowercase*

There are 5 valid moves:

-rock
-paper
-scissors
-lizard
-spock

To earn a point your 'move' must beat your oponents 'move'.

Scoring Guide:

-rock crushes scissors
-scissors cuts paper
-paper covers rock
-rock crushes lizard
-lizard poisons spock
-spock smashes scissors
-scissors decapitates lizard
-lizard eats paper
-paper disproves spock
-spock vaporizes rock



Have fun!! and remember all inputs must be made in lowercase.
Press enter to continue!""")

        while True:
            try:
                rounds = input(f"""
{name},
How many rounds would you like to play? """)
                x = int(rounds)
            except ValueError:
                print("""Sorry, that wasn't a valid input!
Please enter a number!""")
            else:
                break
        print("\nGame start!")
        for round in range(x):
            turn = round + 1
            print(f"\nRound {turn}:")
            self.play_round(round, name)

        if self.p1_score < self.p2_score:
            print("\nPlayer 2 wins!")
        elif self.p1_score > self.p2_score:
            print(f"\n{name} wins!")
        elif self.p1_score == self.p2_score:
            print("It's a Draw")
        print("Game over!")


if __name__ == '__main__':

    playr1 = method_player()
    playr2 = ReflectPlayer()
    playr3 = random_player()
    game = Game(human_player(), random.choice([playr1, playr2, playr3]))

    game.play_game()
