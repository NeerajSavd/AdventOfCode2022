def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 9\day9.txt", "r")
    head = (0,0)
    tail = (0,0)
    visited = set()
    for line in file:
        move = line[0]
        dist = int(line[1:])
        for i in range(dist):
            if move == 'U':
                head = (head[0], head[1]+1)
            elif move == 'D':
                head = (head[0], head[1]-1)
            elif move == 'L':
                head = (head[0]-1, head[1])
            elif move == 'R':
                head = (head[0]+1, head[1])
            
            if (tail[0]+2 == head[0] or tail[0]-2 == head[0] or tail[1]+2 == head[1] or tail[1]-2 == head[1]):
                if (tail[0] < head[0]):
                    tail = (tail[0]+1, tail[1])
                if (tail[0] > head[0]):
                    tail = (tail[0]-1, tail[1])
                if (tail[1] < head[1]):
                    tail = (tail[0], tail[1]+1)
                if (tail[1] > head[1]):
                    tail = (tail[0], tail[1]-1)
            visited.add(tail)
            
            print(head, tail)
    
    print(visited)
    print(len(visited))


def part2():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 9\day9.txt", "r")
    rope = [(0,0)]*10
    visited = set()
    for line in file:
        move = line[0]
        dist = int(line[1:])
        for i in range(dist):
            if move == 'U':
                rope[0] = (rope[0][0], rope[0][1]+1)
            elif move == 'D':
                rope[0] = (rope[0][0], rope[0][1]-1)
            elif move == 'L':
                rope[0] = (rope[0][0]-1, rope[0][1])
            elif move == 'R':
                rope[0] = (rope[0][0]+1, rope[0][1])
            
            for k in range(1,10):
                if (rope[k][0]+2 == rope[k-1][0] or rope[k][0]-2 == rope[k-1][0] or rope[k][1]+2 == rope[k-1][1] or rope[k][1]-2 == rope[k-1][1]):
                    if (rope[k][0] < rope[k-1][0]):
                        rope[k] = (rope[k][0]+1, rope[k][1])
                    if (rope[k][0] > rope[k-1][0]):
                        rope[k] = (rope[k][0]-1, rope[k][1])
                    if (rope[k][1] < rope[k-1][1]):
                        rope[k] = (rope[k][0], rope[k][1]+1)
                    if (rope[k][1] > rope[k-1][1]):
                        rope[k] = (rope[k][0], rope[k][1]-1)
            visited.add(rope[9])
        print(rope)
    
    print(visited)
    print(len(visited))


part2()