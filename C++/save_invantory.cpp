/*
Title: save_inventory.cpp
Author: Ginnie Steck
Date: 4/15/2024
Purpose: add buisness inventory
*/


#include <iostream>
#include <stdio.h>
#include <fstream>
#include <cstring>
using namespace std;



int main(int argc, char *argv[]){
    int part_num = 1, quant;
    float price; 
    fstream file; 
    file.open("inventory.txt");
    cout << "\nThis program stores a business inventory. \n\n";
    
    while(true){
        cout << "Please enter item data (part number, quantity, price): ";
        cin >> part_num;

        if(part_num == 0){
            cout << "\nThank you. Inventory stored in file inventory.txt. \n";
            break;
        }
        cin >> quant >> price;
        cout << endl; 

        file << part_num << " " << quant << " " << price << endl;
        
    }
    file.close();
}