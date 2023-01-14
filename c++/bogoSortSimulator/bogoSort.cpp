/**
 * @file bogoSort.cpp
 * @author John "Matt" Shenk (shenk2015@gmail.com)
 * @brief A program that displays the awesome and EFFICIENT BogoSort algorithm!
 * @version 0.1
 * @date 2023-01-11
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>        
#include <chrono>
#include <random>      

// Function declarations
bool isSorted(std::vector<int> numbers);

void displayVector(std::vector<int> numbers);

int main(){

    int numNums;
    std::cout << "Welcome to the BOGO Sort Simulator!\nEnter a length for the vector: ";
    std::cin >> numNums; 


    std::vector<int> numbers;
    int next;

    for(int x = 0; x < numNums; x++){
        std::cout << "Enter a number: ";
        std:: cin >> next;
        numbers.push_back(next);
    }

    std::cout << "Original vector:  ";
    displayVector(numbers);

    while(!isSorted(numbers)){
        std::cout << "\nVector not sorted! Randomizing...\n";
        unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
        std::shuffle(numbers.begin(), numbers.end(), std::default_random_engine(seed));
        std::cout << "Randomized vector: \n";
        displayVector(numbers);
    }

    std::cout << "\nVector Sorted!";

}

bool isSorted(std::vector<int> numbers){
    //If the length of the vector is 0 or 1, don't bother checking 
    if(numbers.size() <= 0 || numbers.size() == 1){
        return true;
    }


    if(std::is_sorted(numbers.begin(), numbers.end())){
        return true;
    }

    return false;
}

void displayVector(std::vector<int> numbers){
    std::cout << "[ ";
    for(auto itr = numbers.begin(); itr != numbers.end(); itr++){

        std::cout << *itr;

        if(itr != --numbers.end())
            std::cout << ", ";
    }
    std::cout << " ]";
}