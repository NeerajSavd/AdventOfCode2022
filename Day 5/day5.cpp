#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

void part1()
{
    std::fstream file;
    file.open("day5.txt", std::ios::in);
    std::string line;
    std::map<int, std::vector<char>> crates;
    while(std::getline(file, line))
    {
        if (line.find("[") != std::string::npos)
        {
            int i = 1;
            while (true)
            {
                char c = line[1];
                if (c != ' ')
                    crates[i].push_back(c);
                if (line.size() > 3)
                    line = line.substr(4);
                else
                    break;
                i++;
            }
        }
        else if (line != "" && line[1] == '1')
        {
            for (auto& c : crates)
            {
                std::reverse(c.second.begin(), c.second.end());
            }
        }
        else if (line[0] == 'm')
        {
            std::stringstream ss(line);
            std::string s;
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int count = std::stoi(s);
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int a = std::stoi(s);
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int b = std::stoi(s);
            for (int i = 0; i < count; i++)
            {
                crates[b].push_back(crates[a].back());
                crates[a].pop_back();
            }
        }
    }
    // for (auto& c : crates)
    // {
    //     std::cout << c.first << ": ";
    //     while (!c.second.empty())
    //     {
    //         std::cout << c.second.top();
    //         c.second.pop();
    //     }
    //     std::cout << std::endl;
    // }
    for (auto& c : crates)
    {
        std::cout << c.second.back();
    }
}

void part2()
{
    std::fstream file;
    file.open("day5.txt", std::ios::in);
    std::string line;
    std::map<int, std::vector<char>> crates;
    while(std::getline(file, line))
    {
        if (line.find("[") != std::string::npos)
        {
            int i = 1;
            while (true)
            {
                char c = line[1];
                if (c != ' ')
                    crates[i].push_back(c);
                if (line.size() > 3)
                    line = line.substr(4);
                else
                    break;
                i++;
            }
        }
        else if (line != "" && line[1] == '1')
        {
            for (auto& c : crates)
            {
                std::reverse(c.second.begin(), c.second.end());
            }
        }
        else if (line[0] == 'm')
        {
            std::stringstream ss(line);
            std::string s;
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int count = std::stoi(s);
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int a = std::stoi(s);
            std::getline(ss, s, ' '); std::getline(ss, s, ' ');
            int b = std::stoi(s);
            std::vector<char> temp;
            for (int i = 0; i < count; i++)
            {
                temp.push_back(crates[a].back());
                crates[a].pop_back();
            }
            for (int i = 0; i < count; i++)
            {
                crates[b].push_back(temp.back());
                temp.pop_back();
            }
        }
    }
    for (auto& c : crates)
    {
        std::cout << c.second.back();
    }
}

int main()
{
    part2();
    return 0;
}