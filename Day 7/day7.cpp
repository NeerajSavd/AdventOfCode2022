#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

void part1()
{
    std::fstream file;
    file.open("day7.txt", std::ios::in);
    std::string line;
    std::vector<std::string> dirs;
    std::unordered_map<std::string, int> sizes;
    while (std::getline(file, line))
    {
        if (line == "$ cd ..")
        {
            dirs.pop_back();
        }
        else if (line == "$ ls")
        {
            continue;
        }
        else if (line[0] == '$')
        {
            dirs.push_back(line.substr(5));
        }
        else if (line[0] == 'd')
        {
            continue;
        }
        else
        {
            int s = std::stoi(line.substr(0, line.find(' ')));
            // std::cout << line << std::endl;
            for (int i = 0; i < dirs.size(); i++)
            {
                std::string path = "";
                for (int j = 0; j <= i; j++)
                {
                    path += dirs[j] + "/";
                }
                sizes[path] += s;
                // std::cout << "\t" << path << " " << sizes[path] << std::endl;
            }
        }
    }
    //print map
    // for (auto it = sizes.begin(); it != sizes.end(); it++)
    // {
    //     std::cout << it->first << " " << it->second << std::endl;
    // }
    int total = 0;
    for (auto it = sizes.begin(); it != sizes.end(); it++)
    {
        if (it->second <= 100000)
        {
            total += it->second;
        }
    }
    std::cout << total << std::endl;

    int unused = 70000000 - sizes["//"];
    int space = 30000000 - unused;
    std::cout << "need: " << space << std::endl;
    std::string min = "//";
    for (auto it = sizes.begin(); it != sizes.end(); it++)
    {
        if (it->second >= space && it->second < sizes[min])
        {
            min = it->first;
        }
    }
    std::cout << min << " " << sizes[min] << std::endl;
}

void part2()
{
    
}

int main()
{
    part1();
    return 0;
}