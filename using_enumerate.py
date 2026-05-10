games = ["rocket league", "dream league", "sudoku", "fiest"]

for index , game in enumerate(games, start=1):
    print(f"Number {index}: {game.title()}")

# comprehension version
games = ["rocket league", "dream league", "sudoku", "fiest"]

compressed = [f"Number {index}: {game.title()}" for index, game in enumerate(games, start=1)]
print(compressed)



















