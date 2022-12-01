with open("data/stage1") as f:
    data = f.readlines()

elves = []
elf = 0
for row in data:
    if row == '\n':
        elves.append(elf)
        elf = 0
    else:
        elf += int(row)

print(sum(sorted(elves, reverse=True)[:3]))
