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

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def print_part1(data):
    print("part 1: ", end="")
    total = 0
    for rucksack in data:
        compartment1 = set(rucksack[:len(rucksack) // 2])
        compartment2 = rucksack[len(rucksack) // 2:]
        # Find sum of common letter priorities
        sum = 0
        for letter in compartment1:
            if letter in compartment2:
                # letter exists in both compartments
                sum += priorities.index(letter) + 1
        total += sum
    print(total)
    pass

def print_part2(data):
    print("part 2: ", end="")
    # every 3 rucksacks is a new group
    total = 0
    groups = [data[i:i + 3] for i in range(0, len(data), 3)]
    for group in groups:
        # find only common letter in all 3 rucksacks
        common = set(group[0])
        for letter in common:
            if letter in group[1] and letter in group[2]:
                total += priorities.index(letter) + 1
                break
    print(total)
    pass

if __name__ == "__main__":
    main()