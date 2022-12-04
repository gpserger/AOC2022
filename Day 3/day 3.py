with open("data/input1") as f:
    data = f.readlines()


priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for rucksack in data:
    rucksack = rucksack.strip()
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




