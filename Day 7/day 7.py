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

def parse_input(data):
    filesystem = {'/': {'children': {}, 'parent': None}}
    root = filesystem
    lineindex = 0
    while True:
        line = data[lineindex]
        if line[0] == '$':
            # running command
            command = line[1:].strip().split(' ')[0]
            if command == 'cd':
                argument = line[1:].strip().split(' ')[1]
                if argument == '..':
                    # go up one level
                    root = root['parent']
                elif argument == '/':
                    # go to root
                    root = filesystem['/']
                else:
                    # go down one level
                    if argument not in root:
                        root['children'][argument] = {'children': {}, 'parent': root}
                    root = root['children'][argument]
            elif command == 'ls':
                # children will be listed
                pass
            else:
                raise Exception(f"Unknown command {command}")
        else:
            # console is printing files and directories in current directory
            size, name = line.split(' ')
            if size == 'dir':
                root['children'][name] = {'children': {}, 'parent': root}
            else:
                root['children'][name] = {'size': int(size), 'parent': root}
        lineindex += 1
        if lineindex >= len(data):
            break
    return filesystem


def print_filesystem(filesystem, level=0):
    if '/' in filesystem:
        filesystem = filesystem['/']
        print(' - /', end='')
        level = 1
    if 'children' in filesystem:
        print(f" (dir), {filesystem['size']} bytes")
        for child in filesystem['children']:
            print(f"{'  ' * level}- {child}", end="")
            print_filesystem(filesystem['children'][child], level+1)
    else:
        print(f" (file, size={filesystem['size']})")


def add_size_to_directories(filesystem, folders):
    if '/' in filesystem:
        filesystem = filesystem['/']
    if 'children' in filesystem:
        for child in filesystem['children']:
            add_size_to_directories(filesystem['children'][child], folders)
        filesystem['size'] = sum([filesystem['children'][child]['size'] for child in filesystem['children']])
        folders.append(filesystem)

def print_part1(data):
    print("part 1: ", end="")
    filesystem = parse_input(data)
    folders = []
    add_size_to_directories(filesystem, folders)
    sum = 0
    for folder in folders:
        if folder['size'] <= 100000:
            sum += folder['size']
    print()
    print(sum)
    # print_filesystem(filesystem)

    pass

def print_part2(data):
    print("part 2: ", end="")
    filesystem = parse_input(data)
    folders = []
    add_size_to_directories(filesystem, folders)
    total_space = 70000000
    needed_space = 30000000
    used_space = filesystem['/']['size']
    free_space = total_space - used_space
    missing_space = needed_space - free_space

    folders.sort(key=lambda x: x['size'])
    # find smallest folder to delete
    for folder in folders:
        if folder['size'] > missing_space:
            print(folder['size'])
            break





if __name__ == "__main__":
    main()