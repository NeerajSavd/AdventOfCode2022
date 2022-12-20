def day14(part1):
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 14\day14.txt", "r")
    cave = []
    for line in file:
        coords = [v.rstrip().split(',') for v in line.split(" -> ")]
        for i in range(1, len(coords)):
            first = coords[i-1]
            second = coords[i]
            if first[0] == second[0]:
                if int(first[1]) > int(second[1]):
                    cave += [(int(first[0]), x) for x in range(int(second[1]), int(first[1])+1)]
                else:
                    cave += [(int(first[0]), x) for x in range(int(first[1]), int(second[1])+1)]
            else:
                if int(first[0]) > int(second[0]):
                    cave += [(x, int(first[1])) for x in range(int(second[0]), int(first[0])+1)]
                else:
                    cave += [(x, int(first[1])) for x in range(int(first[0]), int(second[0])+1)]
    bottom = max([x[1] for x in cave]) + 2
    cave += [(x, bottom) for x in range(300, 700)]
    cave = set(cave)
    overflow = True
    numSand = 0
    while overflow:
        sand = (500, 0)
        while True:
            if sand[1] == bottom-1:
                cave.add(sand)
                numSand += 1
                if part1:
                    numSand -= 1
                    overflow = False
                break
            elif (sand[0], sand[1]+1) not in cave:
                sand = (sand[0], sand[1]+1)
            elif (sand[0]-1, sand[1]+1) not in cave:
                sand = (sand[0]-1, sand[1]+1)
            elif (sand[0]+1, sand[1]+1) not in cave:
                sand = (sand[0]+1, sand[1]+1)
            else:
                if sand == (500, 0):
                    overflow = False
                cave.add(sand)
                numSand += 1
                break
    print(numSand)

day14(False)