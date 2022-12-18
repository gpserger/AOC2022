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

def parseMonkeys(data):
    monkeys = []
    monkey = {}
    for row in data:
        if row == '':
            monkeys.append(monkey)
            monkey = {}
            continue
        if 'Monkey' in row:
            monkey['number'] = int(row.split(' ')[1][:-1])
            continue
        if 'Starting items:' in row:
            monkey['items'] = [int(x) for x in row.split(': ')[1].split(', ')]
            continue
        if 'Operation: ' in row:
            operationstring = row.split(': ')[1]
            operationstring = operationstring.split(' = ')[1]
            monkey['operation'] = operationstring
            continue
        if 'Test: ' in row:
            test = row.split(': ')[1]
            denominator = int(test.split('divisible by ')[1])
            monkey['testnum'] = int(denominator)
            continue
        if 'If true: ' in row:
            monkey['trueDestination'] = int(row.split('monkey ')[1])
            continue
        if 'If false: ' in row:
            monkey['falseDestination'] = int(row.split('monkey ')[1])
            continue

    if len(monkey) > 0:
        monkeys.append(monkey)
    return monkeys


def print_part1(data):
    print("part 1: ", end="")
    monkeys = parseMonkeys(data)
    for monkey in monkeys:
        monkey['inspections'] = 0

    for roundNumber in range(20):
        for monkey in monkeys:
            items = monkey['items']
            for item in items:
                monkey['inspections'] += 1
                old = item
                item = eval(monkey['operation'])
                # boredom
                item = item // 3
                if item % monkey['testnum'] == 0:
                    monkeys[monkey['trueDestination']]['items'].append(item)
                else:
                    monkeys[monkey['falseDestination']]['items'].append(item)
            monkey['items'] = []
        # print([m['items'] for m in monkeys])

    levels = [m['inspections'] for m in monkeys]
    # find highest 2 levels
    levels.sort(reverse=True)
    print(levels[0] * levels[1])

def print_part2(data):
    print("part 2: ", end="")
    monkeys = parseMonkeys(data)
    for monkey in monkeys:
        monkey['inspections'] = 0

    # chinese remainder
    bigmodulo = 1
    for monkey in monkeys:
        bigmodulo *= monkey['testnum']

    for roundNumber in range(10000):
        for monkey in monkeys:
            items = monkey['items']
            for item in items:
                monkey['inspections'] += 1
                # truncating to save time

                old = item
                item = eval(monkey['operation'])
                item = item % bigmodulo

                if divmod(item, monkey['testnum'])[1] == 0:
                    monkeys[monkey['trueDestination']]['items'].append(item)
                else:
                    monkeys[monkey['falseDestination']]['items'].append(item)
            monkey['items'] = []
        # print([m['items'] for m in monkeys])

    levels = [m['inspections'] for m in monkeys]
    # find highest 2 levels
    levels.sort(reverse=True)
    print(levels[0] * levels[1])

if __name__ == "__main__":
    main()