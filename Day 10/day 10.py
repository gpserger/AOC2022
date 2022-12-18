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
    sample = get_data("sample2")
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
    x = 1
    xhistory = [x]
    for instr in data:
        if instr == 'noop':
            xhistory.append(x)
        elif instr.split()[0] == 'addx':
            instr, arg = instr.split(' ')
            xhistory.append(x)
            x += int(arg)
            xhistory.append(x)

    tosum = [20, 60, 100, 140, 180, 220]
    sum = 0
    for i in tosum:
        strength = xhistory[i-1]*i
        sum += strength
    print(sum)


def print_part2(data):
    print("part 2: ")
    rowwidth = 40
    spritewidth = 3
    spritechar = '#'
    offchar = '.'
    row = ""
    rows = []


    x = 1
    xhistory = [x]

    def cycle(x):
        nonlocal row
        nonlocal rows
        nCycle = len(xhistory) % rowwidth
        if nCycle == 0:
            rows.append(row)
            row = ""

        if x+1 == nCycle or x-1 == nCycle or x == nCycle:
            row += spritechar
        else:
            row += offchar


    for instr in data:
        if instr == 'noop':
            xhistory.append(x)
            cycle(x)
        elif instr.split()[0] == 'addx':
            instr, arg = instr.split(' ')
            xhistory.append(x)
            cycle(x)
            xhistory.append(x)
            cycle(x)
            x += int(arg)

    [print(row) for row in rows]

if __name__ == "__main__":
    main()