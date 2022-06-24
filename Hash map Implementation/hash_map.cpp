#pragma once

#include <iostream>
#include "datatype.hpp"
#include <fstream>
#include <algorithm>
#include <cmath>

void hash_map::read_Data()
{
    std::ifstream myFile;
    myFile.open(fileName);
    std::string str = "", line;
    getline(myFile, line, '\n'); // ignore column names
    while (myFile.good())
    {
        country *nn = new country();

        getline(myFile, line, ',');
        nn->rank = line;

        getline(myFile, line, ',');
        nn->country_Name = line;

        getline(myFile, line, ',');
        nn->continent_Name = line;

        getline(myFile, line, ',');
        nn->population = line;

        getline(myFile, line, ',');
        nn->percentage = line;

        getline(myFile, line, '\n');
        line = "";

        insert(nn);
    }
}

void hash_map::insert(country *ptr)
{
    int index = hash_Function(ptr->country_Name);
    ptrArr[index] = ptr;
    is_Filled[index] = true;
}

int hash_map::hash_Function(std::string str)
{
    int index = 0;
    for (size_t i = 0; i < str.length(); i++)
    {
        int ascii = str[i];
        index = index + ascii * 128 * i;
    }
    index = index % bucketSize;

    if (is_Filled[index] == false)
        return index;
    else
    {
        int probe = 1;
        while (is_Filled[index] != false)
        {
            index = index + probe * probe;
            probe++;
            index = index % bucketSize;
        }
    }
    return index;
}

void hash_map::search(std::string str)
{
    int index = hash_Function2(str);
    if (index == -9999 || is_Filled[index] == false)
        std::cout << "Country not found." << std::endl;
    else if (ptrArr[index]->country_Name == str)
        ptrArr[index]->print_Data();
    else
        std::cout << "Country not found." << std::endl;
}

int hash_map::hash_Function2(std::string str)
{
    long int index = 0;
    for (size_t i = 0; i < str.length(); i++)
    {
        int ascii = str[i];
        index = index + ascii * 128 * i;
    }
    index = index % bucketSize;
    if (ptrArr[index]->country_Name == str)
        return index;
    else
    {
        int probe = 1;
        for (size_t i = 0; i < bucketSize; i++)
        {
            index = index + probe * probe;
            probe++;
            index = index % bucketSize;

            if (is_Filled[index] == true && ptrArr[index]->country_Name == str)
                return index;
        }
        return -9999; // error value
    }
}
