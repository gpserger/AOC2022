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

def hasDuplicateChar(s):
    return len(s) != len(set(s))

def print_part1(data):
    print("part 1: ", end="")
    for row in data:
        for i in range(len(row)):
            s = row[i:i+4]
            if not hasDuplicateChar(s):
                print(i+4)
                break
    pass

def print_part2(data):
    print("part 2: ", end="")
    for row in data:
        for i in range(len(row)):
            s = row[i:i+14]
            if not hasDuplicateChar(s):
                print(i+14)
                break
    pass

if __name__ == "__main__":
    main()