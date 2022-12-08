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
    data = [list(row) for row in data]

    sum = 0
    x, y = 0, 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if y == 0 or x == 0 or y == len(data)-1 or x == len(data[0])-1:
                sum += 1
                continue
            tree = data[y][x]
            tallestLeft = max(data[y][:x])
            if tallestLeft < tree:
                sum += 1
                continue
            tallestRight = max(data[y][x+1:])
            if tallestRight < tree:
                sum += 1
                continue
            tallestAbove = max([row[x] for row in data[:y]])
            if tallestAbove < tree:
                sum += 1
                continue
            tallestBelow = max([row[x] for row in data[y+1:]])
            if tallestBelow < tree:
                sum += 1
                continue

    print(sum)


def print_part2(data):
    print("part 2: ", end="")

    data = [list(row) for row in data]

    def getScenicScore(data, x, y):
        # Find view distance for each direction and multiply them together
        l,r,u,d = 0,0,0,0
        tree = data[y][x]
        # left
        if x != 0:
            leftRow = data[y][0:x]
            leftRow.reverse()
            for i in range(len(leftRow)):
                if leftRow[i] >= tree:
                    l = i+1
                    break
            else:
                l = len(leftRow)
        # right
        if x != len(data[0])-1:
            rightRow = data[y][x+1:]
            for i in range(len(rightRow)):
                if rightRow[i] >= tree:
                    r = i+1
                    break
            else: r = len(rightRow)

        # up
        if y != 0:
            upCol = [row[x] for row in data[0:y]]
            upCol.reverse()
            for i in range(len(upCol)):
                if upCol[i] >= tree:
                    u = i+1
                    break
            else: u = len(upCol)

        # down
        if y != len(data)-1:
            downCol = [row[x] for row in data[y+1:]]
            for i in range(len(downCol)):
                if downCol[i] >= tree:
                    d = i+1
                    break
            else: d = len(downCol)

        return r*l*u*d


    highestScenicScore = 0
    for x in range(len(data[0])):
        for y in range(len(data)):
            scenicScore = getScenicScore(data, x, y)
            if scenicScore > highestScenicScore:
                highestScenicScore = scenicScore

    print(highestScenicScore)

if __name__ == "__main__":
    main()