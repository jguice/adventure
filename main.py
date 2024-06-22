import game

# Only start the game if executed directly (enables import without starting a game)
if __name__ == '__main__':
    instance = game.Game()
    instance.gameloop()
