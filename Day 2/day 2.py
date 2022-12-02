
with open("data/input") as f:
    data = f.readlines()

points = {
    "A": 1, "R": 1, # rock
    "B": 2, "P": 2, # paper
    "C": 3, "S": 3, # scissors
}

rules = {
    "AR": "D", # rock beats scissors
    "AY": "W", # rock beats paper
    "AZ": "L", # rock loses to paper
    "BR": "L", # paper loses to rock
    "BY": "D", # paper beats rock
    "BZ": "W", # etc
    "CR": "W",
    "CY": "L",
    "CZ": "D",
}

# built with copilot
strattable = {
    "AW": "P",  # play paper to beat rock
    "AD": "R",  # play rock to draw rock
    "AL": "S",  # play scissors to lose to rock
    "BW": "S",  # play scissors to beat paper
    "BD": "P",  # etc
    "BL": "R",
    "CW": "R",
    "CD": "S",
    "CL": "P",
}

outcomes = {
    "L": 0, # lose
    "D": 3, # draw
    "W": 6, # win
}

sum = 0
for row in data:
    if row == '\n':
        break
    else:
        plays = row.split()
        opponentsplay = plays[0]
        instr = {"X": "L", "Y": "D", "Z": "W"}[plays[1]]
        myplay = strattable[opponentsplay+instr]
        sum += outcomes[instr]
        sum += points[myplay]

print(sum)



