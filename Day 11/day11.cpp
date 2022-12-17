#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>

void part1()
{
    std::fstream file;
    file.open("day11.txt", std::ios::in);
    std::string line;
    std::vector<std::queue<int>> items;
    std::vector<std::vector<int>> operation;

    int i = 0;
    while (std::getline(file, line))
    {
        std::getline(file, line);
        items.push_back(std::queue<int>());
        line = line.substr(18, line.size());
        while (line.size() != 0)
        {
            std::string item = line.substr(0, line.find(","));
            items[i].push(std::stoi(item));
            line = line.substr(4, line.size());
        }

        std::getline(file, line);
        operation.push_back(std::vector<int>());
        if (std::count(line.begin(), line.end(), "old") == 2)
        {
            operation[i].push_back(0);
            operation[i].push_back(0);
        }
        else
        {
            if (std::count(line.begin(), line.end(), "+") == 1)
                operation[i].push_back(1);
            else
                operation[i].push_back(2);
            operation[i].push_back(std::stoi(line.substr(25, line.size())));
        }

        std::getline(file, line);
        operation[i].push_back(std::stoi(line.substr(21, line.size())));
        std::getline(file, line);
        operation[i].push_back(std::stoi(line.substr(29, line.size())));
        std::getline(file, line);
        operation[i].push_back(std::stoi(line.substr(30, line.size())));
        if (!std::getline(file, line))
            break;
        i++;
        // i give up
    }
    
}

void part2()
{
    
}

int main()
{
    part1();
    return 0;
}