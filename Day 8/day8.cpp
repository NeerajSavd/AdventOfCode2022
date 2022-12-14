#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

void part1()
{
    std::fstream file;
    file.open("day8.txt", std::ios::in);
    std::string line;
    std::vector<std::vector<int>> forest;
    int i = 0;
    while (std::getline(file, line))
    {
        forest.push_back(std::vector<int>());
        for (int j = 0; j < line.size(); j++)
        {
            forest[i].push_back(line[j] - '0');
        }
        i++;
    }
    int visible = 2 * (forest.size() + forest[0].size()) - 4;
    int score = 0;
    for (int r = 1; r < forest[0].size()-1; r++)
    {
        for (int c = 1; c < forest.size()-1; c++)
        {
            int v = 0;
            int j = 0;
            int s = 0;
            for (j = r-1; j >= 0; j--)
            {
                if (forest[j][c] >= forest[r][c])
                    break;
            }
            if (j == -1)
            {
                v++;
                s = r-(j+1);
            }
            else
                s = r-j;
            for (j = r+1; j < forest[0].size(); j++)
            {
                if (forest[j][c] >= forest[r][c])
                    break;
            }
            if (j == forest[0].size())
            {
                v++;
                s *= j-r-1;
            }
            else
                s *= j-r;
            for (j = c-1; j >= 0; j--)
            {
                if (forest[r][j] >= forest[r][c])
                    break;
            }
            if (j == -1)
            {
                v++;
                s *= c-(j+1);
            }
            else
                s *= c-j;
            for (j = c+1; j < forest.size(); j++)
            {
                if (forest[r][j] >= forest[r][c])
                    break;
            }
            if (j == forest[0].size())
            {
                v++;
                s *= j-c-1;
            }
            else
                s *= j-c;
            if (v > 0)
                visible++;
            if (s > score)
                score = s;
        }
    }
    std::cout << visible << std::endl;
    std::cout << score << std::endl;
}

void part2()
{
    
}

int main()
{
    part1();
    return 0;
}