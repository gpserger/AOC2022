
with open("data/input2") as f:
    data = f.readlines()

points = {
    "A": 1, "X": 1, # rock
    "B": 2, "Y": 2, # paper
    "C": 3, "Z": 3, # scissors
}

rules = {
    "AX": "D", # rock beats scissors
    "AY": "W", # rock beats paper
    "AZ": "L", # rock loses to paper
    "BX": "L", # paper loses to rock
    "BY": "D", # paper beats rock
    "BZ": "W", # etc
    "CX": "W",
    "CY": "L",
    "CZ": "D",
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
        myplay = plays[1]
        outcome = rules[opponentsplay+myplay]
        sum += outcomes[outcome]
        sum += points[myplay]

print(sum)



