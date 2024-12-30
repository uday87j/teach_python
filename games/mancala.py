#!python3

# File: mancala.py
# date: 29 Dec 2024

# Brief: This file contains code to simulate a game of "Mancala"

# Detail: 
# Along with code are also written documentation to explain the code
# It is hoped that anyone who reads the documentation alongside code
# will understand the control flow of the game
# and learn simple aspects of programming in Python

# Basics of programming in python

# Declaring a variable to hold some data in memory which will continue to live until its scope ends
    # This is how an integer is created
        # integer = 2
    # Every data has 2 things associated with it: value and type
    # So, one can also be more explicit in decaring above integer as
        # integer: int = 2

# Loops
    # for loop
        # Loop until some condition is true such as 
            # for idx in range(0, 5)
            # Loop 5 times, each time `idx` takes the value of 0, 1, 2, 3, 4 respectively
            # Loop terminates when `idx` equals 5
            # This is the stopping condition
    # while loop
        # Loop until some condition is true such as 
            # while n < 3
            # If `n` was initially 0, this loops 3 times for n = 0, 1, 2
            # Loop exits when `n` equals 3

# Functions or Methods
    # Contian p=individual pieces of list of code-lines to execute when "invoked"
    # Calling or invoking a function amounts to writing its name with required parameters
    # Declare a simple function that decides whether a given integer is "even"
        # def is_even(n: int):
            # return n % 2 == 0
    # Call a function
        # is_even(8)
        # is_even(13)

# Classes
    # Template of code that is usued to instantiate actual data objects
    # In real world, one can have a "Class of Window" and one can actually create
    # 10 windows of the same shape and material as indicated by its "Class"
    # In this game, there are many classes: House, Player, Board

# Start reading code from the last line of this file which has:
# if __name__ == "__main__":
#     main()

# Search for the function `main()` and continue to read code this way
# Every time, you come across a function, search for its definition and read it
        

# Code starts here

# Import external packages
import sys

class House:
    def __init__(self):
        """Initializing method.
        This is called automaticaly whenever an instance of `House` is created 
        Example: See `Player's __init__(self, name: str, id: int)`"""
        self.id = 0 # Every house has an ID
        self.num_gems = 0 # Track the number of gems in a house
        self.is_last = False # Store the truth of whether this is the last house
        self.next = self # Link to next house, initially set to itself, later changed by Player

    def add_gems(self, n: int) -> None:
        """Add some gems to this house
        n: int, number of gems"""
        self.num_gems += n

    def pop_gems(self) -> int:
        """Remove all the gems from this house
        and return the number of gems removed"""
        n = self.num_gems
        self.num_gems = 0
        return n

class Player:
    def __init__(self, name: str, id: int):
        """Initializing method.
        This is called automaticaly whenever an instance of `Player` is created 
        Example: See `Board's __init__(self)`"""
        # Create all the data member required to represent a Player
        self.id = id
        self.name = name
        self.houses = []
        self.MAX_H = 7
        self.MAX_H_ID = 6 # Index of last house is 6 because indexing starts from 0
        self.MIN_H_ID = 0
        self.INIT_GEMS = 4

        # Create 7 houses per Player
        for idx in range(0, self.MAX_H):
            self.houses.append(House())

        # For each house, link the next house and add initial gems
        for idx in range(0, self.MAX_H - 1):
            self.houses[idx].id = idx
            self.houses[idx].add_gems(self.INIT_GEMS)
            self.houses[idx].next = self.houses[idx + 1]
        self.houses[self.MAX_H_ID].id = self.MAX_H_ID
        self.houses[self.MAX_H_ID].is_last = True
        self.houses[self.MAX_H_ID].next = self.houses[self.MIN_H_ID]

        # Create data to count total gems won by this Player
        self.gems_in_pot = 0

        # Check if the houses are linked correctly
        for idx in range(0, 6):
            assert self.houses[idx].next != self.houses[idx]

    def add_gems(self, n: int) -> None:
        """Add gems to current Player's tally
        n: int, number of gems"""
        self.gems_in_pot += n

    def done(self) -> bool:
        """Return True if game is finished for this Player,
        otherwise return False"""
        # Check if all my houses are empty (Except for the last-house)
        for idx in range(0, 6):
            if self.houses[idx].num_gems != 0:
                return False
        return True
        
    def print_state(self) -> None:
        """Print my house content"""
        print(f"Total: {self.gems_in_pot}")
        gems = [h.num_gems for h in self.houses]
        print(gems)

    def get_gems_per_house(self) -> []:
        """Return a list of gems per-house"""
        gems = [h.num_gems for h in self.houses]
        return gems

class Board:
    def __init__(self):
        """Initializing method.
        This is called automaticaly whenever an instance of `Board` is created 
        Example: See `main()`"""

        # Create 2 players, give them names and IDs
        self.p0 = Player("P0", 0)
        self.p1 = Player("P1", 1)

        # Define some values that are useful later
        self.MAX_H = 7
        self.MAX_H_ID = 6 # Index of last house is 6 because indexing starts from 0

        # Write down rules and store them in this data-member
        self.rules = ("\nRules:"
        "\nThe indexes of houses start from 1 i.e. a player can choose from house 1, 2, 3, 4, 5, 6."
        "\nPick all the gems from a house of your choice (from houses belonging to you)."
        "\nThe game will put one gem per house starting from the house next to the one from where the gems were picked."
        "\nIf you end up putting the last gem into an empty house, then you get all the gems from the opposite house of your opponent."
        "\nIf you end up putting the last gem into your last-house, you get to play again."
        "\nOnly these inputs are allowed: 'r', 'q', '1', '2', '3', '4', '5', '6'"
        "\nr = rules, q = quit"
        "\nPress 'q' to exit\n")

    def convert_world1_to_world0(self, n: int) -> int:
        """Convert from the world of numbers where indexing starts from 1 (such as in human world)
        to computer's world where indexing starts from 0."""
        assert n > 0
        return n - 1

    def print_state(self) -> None:
        """Print content of baord from players' perspective"""
        print("Players' perspective:")
        print("P0:")
        self.p0.print_state()
        print("P1:")
        self.p1.print_state()

    def draw_state(self, p: Player) -> None:
        """Draw the contents of the board from the perspective of the player
        whose turn it is to play now.
        p: Player, whose turn it is right now
        """
        opp = self.opponent(p)
        p_gems = p.get_gems_per_house()
        opp_gems = opp.get_gems_per_house()
        opp_gems = reversed(opp_gems)

        print('-' * 33)
        print(" " * 5 + f"{opp.name} : {opp.gems_in_pot}" + " " * 5)
        print('-' * 33)
        print('|', end = '')
        for g in opp_gems:
            print(f' {g} |', end = '')
        print('   |')
        print("|   |" + '-' * 23 + '|   |')
        print('|   |', end = '')
        for g in p_gems:
            print(f' {g} |', end = '')
        print("\n" + '-' * 33)
        print(" " * 5 + f"{p.name} : {p.gems_in_pot}" + " " * 5)
        print('-' * 33)

    def play(self) -> None:
        """The main game-loop which runs until the finish"""

        # Player P0 starts the game
        cur_player = self.p0

        # This is in infinite loop as in
        # it will run until deliberately chosen to stop
        # One can exit the loop and the game using `sys.exit()`
        while True:
            # self.print_state()
            self.draw_state(cur_player)

            # Get input from player
            print(f"Play {cur_player.name}")
            keypress = input()
            # print(keypress)
            key_lower = keypress.lower()

            # Process the input
            if key_lower == 'r' or key_lower == 'h':
                self.print_rules()
            if key_lower == 'q':
                sys.exit()
            try:
                # Here, we are sure that the input is a number and not some letter
                # All letter inputs such as `r`, `h` are handled before we get here
                key_int = self.convert_world1_to_world0(int(key_lower))

                # We now have a house number chosen by the player
                # Let us move the gems
                repeat: bool = self.move_gems(cur_player, key_int)

                # Check if the game has ended and exit
                if cur_player.done() or self.opponent(cur_player).done():
                    self.finish_game()
                    sys.exit()
                if not repeat: # The last gem wasn't placed in the last house
                    cur_player = self.opponent(cur_player) # Switch player
                    print(f"Switch player to {cur_player.name}")
                else: # The last gem wasn placed in the last house
                    print(f"Same player to play again")
            except Exception as e:
                # Oops, something went wrong, let us print the exception message
                print(e)
                print("\nInvalid input, only these allowed: 'r', 'q', '1', '2', '3', '4', '5', '6'")

    def finish_game(self):
        """Game has ended
        Print the final board and points per player"""
        self.draw_state(self.p0)
        self.p0.gems_in_pot += self.p0.houses[self.MAX_H_ID].pop_gems()
        self.p1.gems_in_pot += self.p1.houses[self.MAX_H_ID].pop_gems()
        print(f"Player P0 has {self.p0.gems_in_pot} and P1 has {self.p1.gems_in_pot}")
        if self.p0.gems_in_pot > self.p1.gems_in_pot:
            print("P0 won.")
        else:
            print("P1 won.")
        print("Game over.")

    def opponent(self, p: Player) -> Player:
        """Given a player, return their opponent
        p: Player"""
        assert p.id == 0 or p.id == 1
        if p.id == 0:
            return self.p1
        return self.p0

    def move_gems(self, p: Player, k: int) -> bool: 
        """Move the gems from the chosen house of player `p`
        p: Player, who has opted to move their gems
        k: int, the house index from which they started moving
        Return bool: Whether needs to play the same player again
        """
        # The house number has to be between [0..6] otherwise, it is incorrect
        assert k >= 0 and k < 6 

        # Fetch the correct house
        h: House = p.houses[k]

        # Remove gems from the house
        gems = h.pop_gems()

        # Create a tracking variable called `nh`
        # which will represent "next-house" while
        # we continue to spread the gems
        # from one house to the next house
        nh = h
        while gems > 0:
            nh = nh.next # Go to next house
            nh.add_gems(1) # Add a gem to the new house
            gems -= 1 # Decrease the gems picked up from original house by one
        # print(f"Ended up in house {nh.id} which has {nh.num_gems} gems")
        assert nh.id >= 0 and nh.id <= 6

        # If we end up in the last-house, we need to play again, so return True
        if nh.id == 6:
            return True
        # If we didn't end up in the last-house, but we finished in an empty house,
        # pick up all the gems from opponent's opposite house
        if nh.num_gems == 1:
            opp = self.opponent(p)
            g: int = opp.houses[self.MAX_H - 2 - nh.id].pop_gems() # -2 is needed to get correct index of opposite house
            print(f"Opp-house belonging to {opp.name} has {g} gems")
            p.add_gems(g)
        return False # The same player doesn't play again if we reach here
            

    def print_rules(self):
        """Print rules"""
        print(self.rules)

def make_board() -> Board:
    """Create an instance of board, which has all the logic to play the game"""
    b = Board()
    return b

# This is the main entry point to this game
def main():
    # Create an instance of board, which has all the logic to play the game
    b: Board = make_board()

    # Print rules before start of play
    b.print_rules()

    # Start playing the game
    b.play()

# This is the start of control-flow
if __name__ == "__main__":
    main()
