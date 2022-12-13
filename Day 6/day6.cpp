#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <algorithm>

void part1()
{
    std::fstream file;
    file.open("day6.txt", std::ios::in);
    std::string line;
    std::getline(file, line);
    for (int i = 3; i < line.size(); i++)
    {
        if (line[i] == line[i - 1] || line[i] == line[i - 2] || line[i] == line[i - 3])
        {
            continue;
        }
        if (line[i-1] == line[i-2] || line[i-1] == line[i-3] || line[i-2] == line[i-3])
        {
            continue;
        }
        std::cout << i + 1 << std::endl;
        break;
    }
}

void part2()
{
    std::fstream file;
    file.open("day6.txt", std::ios::in);
    std::string line;
    std::getline(file, line);
    for (int i = 13; i < line.size(); i++)
    {
        std::unordered_set<char> set;
        for (int j = i - 13; j <= i; j++)
        {
            set.insert(line[j]);
        }
        if (set.size() == 14)
        {
            std::cout << i + 1 << std::endl;
            break;
        }
    }
}

int main()
{
    part2();
    return 0;
}