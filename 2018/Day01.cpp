#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::vector<int> readFile() 
{
    std::vector<int> data;
    int line;
    std::ifstream input("Day01_input.txt");
    
    if(input.is_open()) 
    {
        while(input >> line) 
        {
            //std::cout << line << std::endl;
            data.push_back(line);
        }
    }
    return data;
}

void problem1()
{
    std::vector<int> data = readFile();
    int sum = 0;
    for(int num : data)
    {
        sum += num;
    }
    
    std::cout << sum;
}

void problem2()
{
    std::vector<int> data = readFile();
    std::vector<int> sums;

    int sum = 0;

    bool solved = false;

    while(!solved)
    {
        for(int num : data)
        {
            sum += num;

            if(std::find(sums.begin(), sums.end(), sum) != sums.end()) {
                std::cout << "FOUND!" << std::endl;;    
                std::cout << sum;    
                solved = true;
                break;
            }
            sums.push_back(sum);
        }
        //std::cout << sum << std::endl;
    }
}

int main() 
{
    problem2();

    return 1;
}