def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 10\day10.txt", "r")
    cycle = 0
    x = 1
    s = 0
    for line in file:
        if (line[0] == 'a'):
            for _ in range(2):
                cycle += 1
                if (cycle-20) % 40 == 0:
                    s += x*cycle
                    print(x,cycle)
            x += int(line[5:])
        else:
            cycle += 1
            if (cycle-20) % 40 == 0:
                s += x*cycle
                print(x,cycle)
    print(s)

def part2():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 10\day10.txt", "r")
    cycle = 0
    x = 1
    row = 0
    pos = 0
    CRT = []
    for _ in range(7):
        CRT.append([])
    for line in file:
        if (line[0] == 'a'):
            for _ in range(2):
                cycle += 1
                CRT[row].append('#' if (pos == x-1 or pos == x or pos == x+1) else '.')
                pos += 1
                if cycle % 40 == 0:
                    row += 1
                    pos = 0
            x += int(line[5:])
        else:
            cycle += 1
            CRT[row].append('#' if (pos == x-1 or pos == x or pos == x+1) else '.')
            pos += 1
            if cycle % 40 == 0:
                row += 1
                pos = 0
    for c in CRT:
        print(''.join(c))

part2()