import time

def get_data(filename):
    with open (f"data/{filename}") as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    return data

def time_part(func, data):
    start = time.time()
    func(data)
    return time.time() - start

def main():
    start = time.time()
    sample = get_data("sample")
    input = get_data("input")

    print("########### SAMPLE ###########")
    time1 = time_part(print_part1, sample)
    time2 = time_part(print_part2, sample)
    print(f"time: part 1: {time1}s, part 2: {time2}s, total: {time1+time2}s")

    print("######### REAL INPUT #########")
    time1 = time_part(print_part1, input)
    time2 = time_part(print_part2, input)
    print(f"time: part 1: {time1}s, part 2: {time2}s, total: {time1+time2}s")

    print(f"total time: {time.time()-start}s")


outcomes = {
    "L": 0,  # lose
    "D": 3,  # draw
    "W": 6,  # win
}

def print_part1(data):
    print("part 1: ", end="")
    points = {
        "A": 1, "X": 1,  # rock
        "B": 2, "Y": 2,  # paper
        "C": 3, "Z": 3,  # scissors
    }
    rules = {
        "AX": "D",  # rock beats scissors
        "AY": "W",  # rock beats paper
        "AZ": "L",  # rock loses to paper
        "BX": "L",  # paper loses to rock
        "BY": "D",  # paper beats rock
        "BZ": "W",  # etc
        "CX": "W",
        "CY": "L",
        "CZ": "D",
    }
    sum = 0
    for row in data:
        plays = row.split()
        opponentsplay = plays[0]
        myplay = plays[1]
        outcome = rules[opponentsplay + myplay]
        sum += outcomes[outcome]
        sum += points[myplay]
    print(sum)

def print_part2(data):
    print("part 2: ", end="")
    points = {
        "A": 1, "R": 1,  # rock
        "B": 2, "P": 2,  # paper
        "C": 3, "S": 3,  # scissors
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
    sum = 0
    for row in data:
        plays = row.split()
        opponentsplay = plays[0]
        instr = {"X": "L", "Y": "D", "Z": "W"}[plays[1]]
        myplay = strattable[opponentsplay + instr]
        sum += outcomes[instr]
        sum += points[myplay]
    print(sum)


if __name__ == "__main__":
    main()