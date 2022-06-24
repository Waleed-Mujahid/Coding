#include <iostream>
#include "datatype.hpp"
#include "hash_map.cpp"
#include <fstream>

using namespace std;

int main()
{
    string country_Name;
    char c = 'y';
    hash_map map;
    map.read_Data();
    cout << "Welcome to the Population database of the world." << endl;
    while (c == 'y')
    {
        cout << "Which country would you like to search: ";
        getline(cin, country_Name);
        cout << endl;
        map.search(country_Name);
        cout << "Would you like to search for more countries?" << endl;
        cout << "Press 'y' for yes." << endl;
        cout << "Press any other key for no." << endl;
        cin >> c;
        cin.sync();
    }
}