#pragma once
#include <iostream>

class country
{
public:
    std::string rank;
    std::string country_Name;
    std::string continent_Name;
    std::string population;
    std::string percentage;
    void print_Data()
    {
        std::cout << "Poplulation-wise Rank:       " << rank << std::endl;
        std::cout << "Name of country:             " << country_Name << std::endl;
        std::cout << "Contient:                    " << continent_Name << std::endl;
        std::cout << "Population:                  " << population << std::endl;
        std::cout << "Percent of World population: " << percentage << std::endl << std::endl;
    }
};

class hash_map
{
    int bucketSize;
    std::string fileName;

public:
    country **ptrArr;
    bool *is_Filled;
    hash_map(int size = 400)
    {
        fileName = "World Population.csv";
        bucketSize = size;
        ptrArr = new country*[bucketSize];
        is_Filled = new bool[bucketSize];
        for (size_t i = 0; i < size; i++)
        {
            is_Filled[i] = false;
        }
        
    }
    void read_Data();
    int hash_Function(std::string);
    int hash_Function2(std::string);
    void insert(country *);
    void search(std::string);
};