with open("../../input/06.txt") as f: input_ = f.read()
f = [input_.count(str(i)) for i in range(0, 9)]
def x(): global f; f = f[1:7] + [f[0] + f[7], f[8], f[0]]; return f
print([sum([x() for _ in range(i)][-1]) for i in (80, 176)])
