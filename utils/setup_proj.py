import os

# set working dir to parent
os.chdir('..')
for day in range(11, 18):
    # Create directory named Day {day} with subdir data
    os.mkdir(f"Day {day}")
    os.mkdir(f"Day {day}/data")
    # put empty sample and input files in data
    with open(f"Day {day}/data/sample", "w"):
        pass
    with open(f"Day {day}/data/input", "w"):
        pass
    # copy template.py to Day {day}\day {day}.py
    with open("utils/template.py") as f:
        template = f.read()
    with open(f"Day {day}/day {day}.py", "w") as f:
        f.write(template)
    # add readme file with just a title saying reflections
    with open(f"Day {day}/README.md", "w") as f:
        f.write(f"# Day {day} Reflections")


