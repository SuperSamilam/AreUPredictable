#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>

int min = 1;
int max = 9;
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

bool checkList(std::vector<int> temp1, std::vector<int> temp2)
{
    for (int i = 0; i < temp1.size(); i++)
    {
        if (temp1[i] != temp2[i])
        {
            return false;
        }
    }
    return true;
}

int guess()
{

    float retro = 0;
    int n = inputs.size();
    for (int i = 0; i < inputs.size(); ++i)
    {
        retro = static_cast<double>(i) / inputs.size();

        confidenceLevels[inputs[i]] += retro * 0.7;
        for (int j = 2; j < std::min(12, n - 1); ++j)
        {
            std::vector<int> temp, tempc;

            // Build temp and tempc arrays
            for (int k = 0; k < j; ++k)
            {
                temp.insert(temp.begin(), inputs[i - k]);
                tempc.insert(tempc.begin(), inputs[n - 1 - k]);
            }

            if (temp == tempc) {
                if (i + 1 < n) {
                    confidenceLevels[inputs[i + 1]] += (j - 1) * 10.9 * retro;
                }
            } else {
                break;  // Exit inner loop if temp != tempc
            }
        }
    }

    // Calculate all confidence values
    // Adjust the values depending on, if the difference between the number is a set one
    // Find strict patterns
    // THe latsest numbers has a pattern
    // The latsest numbers can be divided or ultpler by 2
    // Do they have the same ratio 33 66 99 example
    // Fallback 7

    int heighestConfidenceNum = -1;
    float confidence = -100;

    for (int i = min; i <= max; i++)
    {
        if (confidenceLevels[i] > confidence)
        {
            confidence = confidenceLevels[i];
            heighestConfidenceNum = i;
        }
    }

    return heighestConfidenceNum;
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

        int computer = guess();
        inputs.push_back(pInput);
        std::cout << computer << " ComputerGuess" << '\n';
    }

    return 0;
}

// Be able to find strict patterns like 1 2 1 2 1 2 1 2 1 2
// Is the difference any of theese can be pretty confident in that guess then
// Look if the past 5 numbers have the same difference
// Multiples of 2 divisions of 2, 3, 4, 5, 6,7,8,9,10
// Prime number pattern