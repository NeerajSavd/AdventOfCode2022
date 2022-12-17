def day11(part1):
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 11\day11.txt", "r")
    items = []
    operations = []
    while True:
        line = file.readline()
        line = file.readline()
        items.append([int(n) for n in line[18:len(line)-1].split(", ")])
        operation = []
        line = file.readline()
        if (line.count("old") == 2):
            operation.append('s')
        elif (line.count("+") == 1):
            operation.append('a')
        else:
            operation.append('m')
        operation.append((line.rstrip()[25:]))
        operation.append(int(file.readline().rstrip()[21:]))
        operation.append(int(file.readline().rstrip()[29:]))
        operation.append(int(file.readline().rstrip()[30:]))
        operation.append(0)
        operations.append(operation)
        if (file.readline() == ''):
            break
    # 0 = sign, 1 = worry, 2 = test, 3 = true, 4 = false, 5 = inspected
    n = 20 if part1 else 10000
    mod = 1
    for j in range(len(operations)):
        mod *= operations[j][2]
    for _ in range(n):
        print(_)
        for m in range(len(items)):
            while (len(items[m]) != 0):
                worry = items[m].pop(0)
                if (operations[m][0] == 's'):
                    worry = worry * worry
                elif (operations[m][0] == 'a'):
                    worry = worry + int(operations[m][1])
                else:
                    worry = worry * int(operations[m][1])
                if part1:
                    worry = int(worry / 3)
                worry = worry % mod
                if (worry % operations[m][2] == 0):
                    items[operations[m][3]].append(worry)
                else:
                    items[operations[m][4]].append(worry)
    operations = sorted(operations, key=lambda x: x[5], reverse=True)
    print(operations[0][5]*operations[1][5])

day11(False)