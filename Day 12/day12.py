def day12(part1):
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 12\day12.txt", "r")
    map = []
    start = (0,0)
    end = (0,0)
    for line in file:
        map.append(list(line.rstrip()))
        if map[-1].count('S') == 1:
            start = (len(map)-1, map[-1].index('S'))
        if map[-1].count('E') == 1:
            end = (len(map)-1, map[-1].index('E'))
    map[start[0]][start[1]] = 'a'
    map[end[0]][end[1]] = 'z'
    queue = [start]
    visited = [] # (step, previous step)
    while len(queue) > 0:
        step = queue.pop(0)
        if step == end:
            path = [step]
            if part1:
                while step != start:
                    path.append(step)
                    step = [v[1] for v in visited if v[0] == step][0]
            else:
                while map[step[0]][step[1]] != 'a':
                    path.append(step)
                    step = [v[1] for v in visited if v[0] == step][0]
            path.append(start)
            path.reverse()
            print(len(path)-2)
            return
        nextsteps = [(step[0]+1, step[1]), (step[0]-1, step[1]), (step[0], step[1]+1), (step[0], step[1]-1)]
        for n in nextsteps:
            if n[0] < 0 or n[0] >= len(map) or n[1] < 0 or n[1] >= len(map[0]):
                continue
            if n in [v[0] for v in visited]:
                continue
            if map[n[0]][n[1]] == map[step[0]][step[1]] or ord(map[n[0]][n[1]]) <= ord(map[step[0]][step[1]])+1:
                queue.append(n)
                visited.append((n,step))
    print('no path found')

day12(False)