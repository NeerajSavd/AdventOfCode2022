def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 18\day18.txt", "r")
    x, y, z = [], [], []
    sa = 0
    for line in file:
        line = [int(x) for x in line.strip().split(',')]
        sa += 6
        for sign in [-1,1]:
            xs = set([i for i in range(len(x)) if x[i] == line[0] + sign])
            ys = set([i for i in range(len(y)) if y[i] == line[1]])
            zs = set([i for i in range(len(z)) if z[i] == line[2]])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 2
            xs = set([i for i in range(len(x)) if x[i] == line[0]])
            ys = set([i for i in range(len(y)) if y[i] == line[1] + sign])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 2
            ys = set([i for i in range(len(y)) if y[i] == line[1]])
            zs = set([i for i in range(len(z)) if z[i] == line[2] + sign])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 2
        x.append(line[0])
        y.append(line[1])
        z.append(line[2])
    print(sa)

part1()