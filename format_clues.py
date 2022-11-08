with open("clues.txt") as f:
    clues = f.read().split("\n\n")
    for i, clue in enumerate(clues):
        msg = f"\nClue coord {i % 14}, {i // 14}:\n"
        print(msg, clue.strip("\n"))
