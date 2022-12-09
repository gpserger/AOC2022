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

# return new tail coordinate
def followHead(tail,head):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail  # the tail and head are touching

    if head[0] == tail[0]:
        # vertical
        if head[1] > tail[1]:
            # head is above tail
            return tail[0], tail[1]+1
        else:
            return tail[0], tail[1]-1

    elif head[1] == tail[1]:
        # horizontal
        if head[0] > tail[0]:
            # head is right of tail
            return tail[0]+1, tail[1]
        else:
            return tail[0]-1, tail[1]

    else:
        # diagonal
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]
        return int(tail[0]+1*(abs(dx)/dx)), int(tail[1]+1*(abs(dy)/dy))


def print_part1(data):
    print("part 1: ", end="")
    coordsVisited = set()
    head = (0, 0)
    tail = (0, 0)
    for row in data:
        dir, dist = row.split(' ')
        for i in range(int(dist)):
            if dir == 'R':
                head = (head[0]+1, head[1])
            elif dir == 'L':
                head = (head[0]-1, head[1])
            elif dir == 'U':
                head = (head[0], head[1]+1)
            elif dir == 'D':
                head = (head[0], head[1]-1)
            else:
                print("invalid direction")
                return
            tail = followHead(tail, head)
            coordsVisited.add(tail)

    print(len(coordsVisited))


def print_part2(data):
    print("part 2: ", end="")

    ropelength = 10
    coordsVisited = set()
    rope = [(0, 0) for i in range(ropelength)]
    for row in data:
        dir, dist = row.split(' ')
        for i in range(int(dist)):
            head = rope[0]
            if dir == 'R':
                rope[0] = (head[0] + 1, head[1])
            elif dir == 'L':
                rope[0] = (head[0] - 1, head[1])
            elif dir == 'U':
                rope[0] = (head[0], head[1] + 1)
            elif dir == 'D':
                rope[0] = (head[0], head[1] - 1)
            else:
                print("invalid direction")
                return
            for k,knot in enumerate(rope):
                if k == 0:
                    continue
                else:
                    rope[k] = followHead(knot, rope[k-1])
            coordsVisited.add(rope[-1])

    print(len(coordsVisited))


if __name__ == "__main__":
    main()