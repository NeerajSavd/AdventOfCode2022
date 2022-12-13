#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::fstream file;
    file.open("day1.txt", std::ios::in);
    std::string line;
    int max1 = 0;
    int max2 = 0;
    int max3 = 0;
    int n = 0;
    while(std::getline(file, line))
    {
        if (line == "")
        {
            if (n > max1)
            {
                int t = max1;
                max1 = n;
                n = t;
            }
            if (n > max2)
            {
                int t = max2;
                max2 = n;
                n = t;
            }
            if (n > max3)
            {
                max3 = n;
            }
            n = 0;
        }
        else
            n += stoi(line);
    }
    std::cout << max1 + max2 + max3 << std::endl;
    return 0;
}