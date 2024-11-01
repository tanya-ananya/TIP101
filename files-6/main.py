'''
CP: https://courses.codepath.org/courses/tip101/unit/5#!session_two
Answers: https://github.com/codepath/compsci_guides/wiki/Unit-5-Session-2
'''

'''
Problem 1: Calculate Tournament Placement
In the Player class below, each player has a race_outcomes attribute which holds a list of integers
describing what place they came in for each race in a tournament.

Write a method get_tournament_place() that takes in one parameter opponents, a list of other
player objects also participating in the tournament, and returns the place in the overall tournament.

Rank in the tournament is determined by the lowest average race outcome. (1st place is better than
2nd!)
Each opponent in opponents is guaranteed to have participated in the same number of races as
the current player.
'''

class Players:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.outcomes = outcomes

    def get_tournament_place(self, oppponents):
        pass

player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")