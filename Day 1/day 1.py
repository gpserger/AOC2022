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


def print_part1(data):
    print("part 1: ", end="")
    elves = []
    elf = 0
    for row in data:
        if row == '':
            elves.append(elf)
            elf = 0
        else:
            elf += int(row)
    elves.append(elf)
    print(max(elves))

def print_part2(data):
    print("part 2: ", end="")
    elves = []
    elf = 0
    for row in data:
        if row == '' and elf != 0:
            elves.append(elf)
            elf = 0
        else:
            elf += int(row)
    elves.append(elf)

    print(sum(sorted(elves, reverse=True)[:3]))


if __name__ == "__main__":
    main()