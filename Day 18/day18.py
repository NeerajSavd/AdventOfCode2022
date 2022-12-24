from collections import defaultdict

def day18(part1):
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 18\day18.txt", "r")
    x, y, z = [], [], []
    lava = defaultdict(int)
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
        lava[(line[0], line[1], line[2])] = 1
    if part1:
        print(sa)
        return
    queue = [(22,22,22)]
    while len(queue) > 0:
        ix, iy, iz = queue.pop(0)
        if lava[(ix,iy,iz)] == 1:
            continue
        lava[(ix,iy,iz)] = 1
        if ix > 0:
            queue.append((ix-1,iy,iz))
        if iy > 0:
            queue.append((ix,iy-1,iz))
        if iz > 0:
            queue.append((ix,iy,iz-1))
        if ix < 22:
            queue.append((ix+1,iy,iz))
        if iy < 22:
            queue.append((ix,iy+1,iz))
        if iz < 22:
            queue.append((ix,iy,iz+1))
    inside = [(ix,iy,iz) for ix in range(22) for iy in range(22) for iz in range(22) if lava[(ix,iy,iz)] == 0]
    for drop in inside:
        for sign in [-1,1]:
            xs = set([i for i in range(len(x)) if x[i] == drop[0] + sign])
            ys = set([i for i in range(len(y)) if y[i] == drop[1]])
            zs = set([i for i in range(len(z)) if z[i] == drop[2]])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 1
            xs = set([i for i in range(len(x)) if x[i] == drop[0]])
            ys = set([i for i in range(len(y)) if y[i] == drop[1] + sign])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 1
            ys = set([i for i in range(len(y)) if y[i] == drop[1]])
            zs = set([i for i in range(len(z)) if z[i] == drop[2] + sign])
            inter = xs.intersection(ys, zs)
            if len(inter) > 0:
                sa -= 1
    print(sa)

day18(False)