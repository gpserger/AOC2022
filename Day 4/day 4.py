with open("data/input") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

def range_subset(range1, range2):
    """Whether range1 either of range2 is a subset of the other"""
    if range1.start in range2 and range1[-1] in range2:
        return True
    if range2.start in range1 and range2[-1] in range1:
        return True


# part 1
sum = 0
for pair in data:
    pass
    elf1, elf2 = pair.split(",")
    elf1bounds = elf1.split("-")
    elf2bounds = elf2.split("-")
    if range_subset(range(int(elf1bounds[0]), int(elf1bounds[1]) + 1), range(int(elf2bounds[0]), int(elf2bounds[1]) + 1)):
        sum += 1

print(sum)

# part 2
sum = 0
for pair in data:
    elf1, elf2 = pair.split(",")
    elf1bounds = elf1.split("-")
    elf2bounds = elf2.split("-")
    elf1range = range(int(elf1bounds[0]), int(elf1bounds[1]) + 1)
    elf2range = range(int(elf2bounds[0]), int(elf2bounds[1]) + 1)
    if elf1range.start in elf2range or elf1range[-1] in elf2range:
        sum += 1
    elif elf2range.start in elf1range or elf2range[-1] in elf1range:
        sum += 1
print(sum)