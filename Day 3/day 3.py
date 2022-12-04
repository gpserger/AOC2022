with open("data/input1") as f:
    data = f.readlines()
    data = [x.strip() for x in data]


priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# part 1
total = 0
for rucksack in data:
    compartment1 = set(rucksack[:len(rucksack)//2])
    compartment2 = rucksack[len(rucksack)//2:]
    # Find sum of common letter priorities
    sum = 0
    for letter in compartment1:
        if letter in compartment2:
            # letter exists in both compartments
            sum += priorities.index(letter) + 1
    total += sum
print(total)

# part 2
# every 3 rucksacks is a new group
total = 0
groups = [data[i:i+3] for i in range(0, len(data), 3)]
for group in groups:
    # find only common letter in all 3 rucksacks
    common = set(group[0])
    for letter in common:
        if letter in group[1] and letter in group[2]:
            total += priorities.index(letter) + 1
            break

print(total)
