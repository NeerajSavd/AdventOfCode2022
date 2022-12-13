#include <iostream>
#include <fstream>
#include <string>

//leaderboard 2654061-860b61ee

void part1()
{
    std::fstream file;
    file.open("day2.txt", std::ios::in);
    std::string line;
    unsigned total;
    while(std::getline(file, line))
    {
        char opp = line[0];
        char you = line[2];
        total += you - 87;
        if (opp == you - 23)
            total += 3;
        else if (opp == 'A' && you == 'Y' || opp == 'B' && you == 'Z' || opp == 'C' && you == 'X')
            total += 6;
    }
    std::cout << total << std::endl;
}

void part2()
{
    std::fstream file;
    file.open("day2.txt", std::ios::in);
    std::string line;
    unsigned total;
    while(std::getline(file, line))
    {
        char opp = line[0];
        char you = line[2];
        if (you == 'Y')
            total += 3 + opp - 64;
        else if (you == 'Z')
        {
            if (opp == 'A')
                total += 6 + 2;
            else if (opp == 'B')
                total += 6 + 3;
            else
                total += 6 + 1;
        }
        else
        {
            if (opp == 'A')
                total += 3;
            else if (opp == 'B')
                total += 1;
            else
                total += 2;
        }
    }
    std::cout << total << std::endl;
}

int main()
{
    part2();
    return 0;
}