# with open("clues.txt") as f:
#     clues = f.read().split("\n\n")
#     for i, clue in enumerate(clues):
#         msg = f"\nClue coord {i % 14}, {i // 14}:\n"
#         print(msg, clue.strip("\n"))

#         print(clue[-1])

with open("clues.txt") as f:
    for i, clue in enumerate(f.read().split("\n\n\n")):
        coord = f"{i % 14},{i // 14}"
        clue = clue.split("\n")
        clue[0] = "<b>" + clue[0] + "</b>"

        quoter = clue[-1].split()[0]
        if quoter[-1] == ":":
            quote = open("message_box.html").read()
            quote = quote.replace("PICTURE_HERE", f"/pfp/{quoter}.png")
            print(quote)
            clue.append(quote)