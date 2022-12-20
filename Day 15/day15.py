from collections import defaultdict
def part1():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 15\day15.txt", "r")
    row = 2000000
    map = set()
    for line in file:
        coords = line.rstrip().replace("Sensor at x=","").replace(", y="," ").replace(": closest beacon is at x="," ").split(" ")
        sensor = (int(coords[0]), int(coords[1]))
        beacon = (int(coords[2]), int(coords[3]))
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        dist = dist - abs(sensor[1] - row)
        for i in range(sensor[0]-dist, sensor[0]+dist+1):
            map.add((i, row))
        if sensor in map:
            map.remove(sensor)
        if beacon in map:
            map.remove(beacon)
    print(len(map))

def inBounds(x, y, sensors, beacons):
    for i in range(len(sensors)):
        dist = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        if abs(sensors[i][0] - x) + abs(sensors[i][1] - y) <= dist:
            return False
    return True

def part2():
    file = open("d:\Onedrive\Coding\AdventOfCode2022\Day 15\day15.txt", "r")
    sensors = []
    beacons = []
    for line in file:
        coords = line.rstrip().replace("Sensor at x=","").replace(", y="," ").replace(": closest beacon is at x="," ").split(" ")
        sensors.append((int(coords[0]), int(coords[1])))
        beacons.append((int(coords[2]), int(coords[3])))
    for i in range(len(sensors)):
        dist = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1]) + 1
        for d in range(dist):
            for sign in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                point = (sensors[i][0] + sign[0]*d, sensors[i][1] + sign[1]*(dist - d))
                if point[0] < 0 or point[1] < 0 or point[0] > 4000000 or point[1] > 4000000:
                    continue
                if inBounds(point[0], point[1], sensors, beacons):
                    print(point[0]*4000000+point[1])
                    return

part2()