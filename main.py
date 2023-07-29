from game_functions.game_functions import GameHandler

# grid width and height
width = 15
height = 15

# Create a 2D list of None to represent an empty grid
cells = [[None for _ in range(width)] for _ in range(height)]

def main():
    game = GameHandler(cells)
    game.run()

if __name__ == '__main__':
    main()
