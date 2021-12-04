from collections import Counter

with open("../../input/03.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

bits = zip(*data)


gamma = ""
epsilon = ""

for bit in bits:
    c = Counter(bit)
    if c["0"] > c["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        epsilon += "0"
        gamma += "1"

gamma_i = int(gamma, 2)
epsilon_i = int(epsilon, 2)

print(gamma, epsilon, gamma_i * epsilon_i)

oxy = ""
co = ""

oxy_data = data[:]
for i, _ in enumerate(data[0]):
    c = Counter(a[i] for a in oxy_data)
    if c["0"] > c["1"]:
        oxy_data = [x for x in oxy_data if x[i] == "0"]
    else:
        oxy_data = [x for x in oxy_data if x[i] == "1"]

    if len(oxy_data) == 1:
        break

codata = data[:]
for i, _ in enumerate(data[0]):
    c = Counter(a[i] for a in codata)
    if c["0"] > c["1"]:
        codata = [x for x in codata if x[i] == "1"]
    else:
        codata = [x for x in codata if x[i] == "0"]

    if len(codata) == 1:
        break

oxy = oxy_data[0]
co = codata[0]
print(oxy, co, int(oxy, 2) * int(co, 2))
