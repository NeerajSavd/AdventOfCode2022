#include <iostream>
#include <fstream>
#include <string>

void part1()
{
    std::fstream file;
    file.open("day4.txt", std::ios::in);
    std::string line;
    unsigned sum = 0;
    while(std::getline(file, line))
    {
        std::string first = line.substr(0, line.find(','));
        std::string second = line.substr(line.find(',') + 1, line.length());
        int num1 = std::stoi(first.substr(0, first.find('-')));
        int num2 = std::stoi(first.substr(first.find('-') + 1, first.length()));
        int num3 = std::stoi(second.substr(0, second.find('-')));
        int num4 = std::stoi(second.substr(second.find('-') + 1, second.length()));
        if (num1 <= num3 && num2 >= num4)
            sum++;
        else if (num1 >= num3 && num2 <= num4)
            sum++;
    }
    std::cout << sum << std::endl;
}

void part2()
{
    std::fstream file;
    file.open("day4.txt", std::ios::in);
    std::string line;
    unsigned sum = 0;
    while(std::getline(file, line))
    {
        std::string first = line.substr(0, line.find(','));
        std::string second = line.substr(line.find(',') + 1, line.length());
        int num1 = std::stoi(first.substr(0, first.find('-')));
        int num2 = std::stoi(first.substr(first.find('-') + 1, first.length()));
        int num3 = std::stoi(second.substr(0, second.find('-')));
        int num4 = std::stoi(second.substr(second.find('-') + 1, second.length()));
        if (num1 <= num3 && num3 <= num2)
            sum++;
        else if (num3 <= num1 && num1 <= num4)
            sum++;
    }
    std::cout << sum << std::endl;
}

int main()
{
    part2();
    return 0;
}