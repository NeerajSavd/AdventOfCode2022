def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 21\day21.txt", "r")
    lines = [l for l in file]
    while len(lines) > 0:
        l = lines.pop(0)
        try:
            exec(l.strip().replace(': ', "="))
        except:
            lines.append(l)
    exec(l.strip())
    print(root) #fails

def part2():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 21\day21p2.txt", "r")
    lines = [l for l in file]
    variables = {}
    for l in lines:
        l = l.strip().replace(": ", "=")
        variables[l.split("=")[0]] = l.split("=")[1]
    for k,v in variables.items():
        print(k, v)

part2()