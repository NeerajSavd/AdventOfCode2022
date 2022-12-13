#include <iostream>
#include <fstream>
#include <string>

void part1()
{
    std::fstream file;
    file.open("day3.txt", std::ios::in);
    std::string line;
    unsigned sum = 0;
    while(std::getline(file, line))
    {
        int half = line.size() / 2;
        std::string first = line.substr(0, half);
        std::string second = line.substr(half, line.size());
        for (int i = 0; i < half; i++)
        {
            if (second.find(first[i]) != std::string::npos)
            {
                if (first[i] >= 'a')
                    sum += first[i] - 96;
                else
                    sum += first[i] - 38;
                break;
            }
        }
    }
    std::cout << sum << std::endl;
}

void part2()
{
    std::fstream file;
    file.open("day3.txt", std::ios::in);
    std::string line1;
    std::string line2;
    std::string line3;
    unsigned sum = 0;
    while(std::getline(file, line1))
    {
        std::getline(file, line2);
        std::getline(file, line3);
        for (int i = 0; i < line1.size(); i++)
        {
            if (line2.find(line1[i]) != std::string::npos && line3.find(line1[i]) != std::string::npos)
            {
                if (line1[i] >= 'a')
                    sum += line1[i] - 96;
                else
                    sum += line1[i] - 38;
                break;
            }
        }
    }
    std::cout << sum << std::endl;
}

int main()
{
    part2();
    return 0;
}