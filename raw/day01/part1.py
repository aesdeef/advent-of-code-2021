with open("../../input/01.txt", "r") as f:
    nums = [int(line) for line in f.readlines()]

print(sum(1 for x, y in zip(nums[:-1], nums[1:]) if x < y))

sums = [a + b + c for a, b, c in zip(nums[:-2], nums[1:-1], nums[2:])]
print(sum(1 for x, y in zip(sums[:-1], sums[1:]) if x < y))
