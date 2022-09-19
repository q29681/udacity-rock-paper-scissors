import random
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("Please type Rock, Paper, Scissors >").lower()
            if move_human in moves:
                return move_human
            else:
                print("Oops, invalid input!")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    scoreP1 = 0
    scoreP2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.scoreP1 += 1
            print("Player one Wins")
        elif beats(move2, move1):
            self.scoreP2 += 1
            print("Player two Wins")
        else:
            print("TIE")
        print(f"Score: Player One {self.scoreP1}, Player Two {self.scoreP2}")

    def play_game(self):
        print("Rock, Paper, Scissors, Game start!")
        for round in range(6):
            print(f"Round {round +1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
