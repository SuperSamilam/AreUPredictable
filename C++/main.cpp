#include <iostream>
#include <vector>
#include <map>

int min = 1;
int max = 8;
std::vector<int> inputs;
std::map<int, float> confidenceLevels;

void setup()
{
    for (int i = min; i <= max; i++)
    {
        confidenceLevels.insert(std::make_pair(i, 0));
    }
}

int registerInput()
{
    int input;
    std::cin >> input;

    if (min <= input && input <= max) // Input is valid
    {
        return input;
    }
    else
    {
        std::cout << "Number is not valid" << '\n';
        return -1;
    }
}

void printConfidenceTable()
{
    for (const auto &pair : confidenceLevels)
    {
        std::cout << pair.first << ": " << pair.second << '\n';
    }
}

void printInputList()
{
    for (const auto &input : inputs)
    {
        std::cout << input << ", ";
    }
    std::cout << '\n';
}

void spacer()
{
    std::cout
        << '\n'
        << '\n'
        << '\n';
}

void guess()
{
    //Calculate all confidence values
    //Adjust the values depending on, if the difference between the number is a set one
    //Find strict patterns
    //THe latsest numbers has a pattern
    //The latsest numbers can be divided or ultpler by 2
    //Do they have the same ratio 33 66 99 example
    //Fallback 7
}

int main()
{
    setup();
    while (true)
    {
        int pInput;
        if ((pInput = registerInput()) == -1)
        {
            continue;
        }
    }

    return 0;
}

// Be able to find strict patterns like 1 2 1 2 1 2 1 2 1 2
// Is the difference any of theese can be pretty confident in that guess then
// Look if the past 5 numbers have the same difference
// Multiples of 2 divisions of 2, 3, 4, 5, 6,7,8,9,10
// Prime number pattern