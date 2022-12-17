from functools import cmp_to_key

def compare(l, r):
    left = l.copy()
    right = r.copy()
    if len(left) == 0:
        return -1
    if len(right) == 0:
        return 0 if len(left) == 0 else 1
    if type(left[0]) == int and type(right[0]) == int:
        if left[0] == right[0]:
            return compare(left[1:], right[1:])
        return -1 if left[0] < right[0] else 1
    if type(left[0]) == int:
        left[0] = [left[0]]
    if type(right[0]) == int:
        right[0] = [right[0]]
    if left[0] == right[0]:
        return compare(left[1:], right[1:])
    return compare(left[0], right[0])


def day13(part1):
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 13\day13.txt", "r")
    i = 1
    sum = 0
    packets = [[[2]],[[6]]]
    while True:
        left = eval(file.readline())
        right = eval(file.readline())
        if compare(left, right) != 1:
            sum += i
        packets.append(left)
        packets.append(right)
        i += 1
        if file.readline() == '':
            break
    print(sum)
    packets = sorted(packets, key=cmp_to_key(compare))
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))

day13(False)