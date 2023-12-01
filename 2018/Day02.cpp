#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <map>

std::vector<std::string> readFile()
{
    std::vector<std::string> data;
    std::string line;
    std::ifstream input("Day02_input.txt");

    if(input.is_open())
    {
        while(getline(input, line))
        {
            data.push_back(line);
        }
    }
    return data;
}

void problem1()
{
    std::vector<std::string> data = readFile();

    int twoCount = 0;
    int threeCount = 0;

    for(std::string line : data)
    {
        std::map<char, int> charCount;
        bool foundTwo = false;
        bool foundThree = false;
        for(char c : line)
        {
            charCount[c]++;   
        }

        for(auto const& x : charCount)
        {
            if(foundTwo && foundThree) break;

            if(x.second == 2 && !foundTwo)
            {
                foundTwo = true;
                twoCount++;
            } 
                
            if(x.second == 3 && !foundThree)
            {
                foundThree = true;
                threeCount++;
            }
        }
    }

    std::cout << twoCount * threeCount;
}

void problem2()
{
    std::string fgrf = "gfr";
}

int main()
{
    problem1();

    return 1;
}