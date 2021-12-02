hor = 0
dep = 0
with open("../input.txt", "r") as f:
    for line in f:
        match line.strip().split():
            case ["forward", num]:
                hor += int(num)
            case ["down", num]:
                dep += int(num)
            case ["up", num]:
                dep -= int(num)

print(hor, dep, hor * dep)

aim = 0
hor = 0
dep = 0
with open("../input.txt", "r") as f:
    for line in f:
        match line.strip().split():
            case ["forward", num]:
                hor += int(num)
                dep += aim * int(num)
            case ["down", num]:
                aim += int(num)
            case ["up", num]:
                aim -= int(num)

print(hor, dep, hor * dep)
