import time
from queue import LifoQueue as Stack

def get_data(filename):
    with open (f"data/{filename}") as f:
        data = f.readlines()
        data = [x.replace('\n', '') for x in data]
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


def get_stacks_and_instructions(data):
    split = data.index('')
    stackNumbers = [int(num) for num in data[split-1] if num != ' ']
    stacks = [Stack() for i in stackNumbers]
    contents = data[:split-1]
    contents.reverse()
    for row in contents:
        for i in range(len(stacks)):
            spot = row[i*4:i*4+4]
            if '[' in spot:
                spot = spot.replace(']','').replace('[','').replace(' ','')
                stacks[i].put(spot)
    # print([stack.queue for stack in stacks])

    instructions = [[int(instr) for instr in row.split(' ') if instr.isnumeric()] for row in data[split+1:]]  # Convert to 3 numbers
    return stacks, instructions


def print_part1(data):
    print("part 1: ", end="")
    stacks, instructions = get_stacks_and_instructions(data)
    for instr in instructions:
        count, fromStack, toStack = instr
        for i in range(count):
            stacks[toStack-1].put(stacks[fromStack-1].get())
    print(''.join([stack.get() for stack in stacks]))



def print_part2(data):
    print("part 2: ", end="")
    stacks, instructions = get_stacks_and_instructions(data)
    for instr in instructions:
        count, fromStack, toStack = instr
        fromStack -= 1
        toStack -= 1
        cratesToMove = [stacks[fromStack].get() for i in range(count)]
        for crate in reversed(cratesToMove):
            stacks[toStack].put(crate)
    print(''.join([stack.get() for stack in stacks]))
    pass

if __name__ == "__main__":
    main()