from collections import defaultdict

maxPressure = {}

def findPressure(valves, prev, current, openV, minutes):
    # print("Entering", prev, current, openV, minutes)
    if minutes == 0:
        # print("Returning 0 minutes")
        return 0
    if len(openV) == len(valves):
        return 0
    if (current, minutes) in maxPressure:
        return maxPressure[(current, minutes)]
    
    pressure = [0]
    for valve in valves[current][1:]:
        pressure.append(findPressure(valves, current, valve, [], minutes-1))
    if current not in openV:
        pressure.append(valves[current][0]*(minutes-1) + findPressure(valves, current, current, [current], minutes-1))
    # print("Returning", prev, current, openV, pressure, minutes)
    maxPressure[(current, minutes)] = max(pressure)
    return max(pressure)

def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 16\day16.txt", "r")
    valves = defaultdict(list)
    for line in file:
        key = line[6:8]
        value = [int(line[line.find("=")+1:line.find(";")])]
        if "valves" in line:
            value += line[line.find("valves ")+7:].strip().split(", ")
        else:
            value += [line[line.find("valve ")+6:].strip()]
        valves[key] = value
    for key in valves:
        print(key, valves[key])
    print(findPressure(valves, "", "AA", [], 30))
    print(maxPressure)
    

part1()