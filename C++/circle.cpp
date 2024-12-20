/*
Title: circle.cpp
Author: Ginnie Steck
Date: 1/27/2024
Purpose: Given the radius, calculates a 
circle's diameter, area, and circumfrence, 
and a square's area and perimiter.
*/

#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int r, d, perimiterS, areaS; 
    float circumfrenceC, areaC, difference;
    float const pi = 3.14f;
    cout << "This program computes values related to an inscribed circle." << endl;
    cout << "Enter the value of the radius: ";
    cin >> r;
    d = r*2;
    cout << "The diameter of the circle is: " << d << endl;
    circumfrenceC = 2 * r * pi; 
    cout << "The circumference of the circle is: " << circumfrenceC << endl;
    areaC = pi * (r*r);
    cout << "The area of the circle is: " << areaC << endl;
    perimiterS = d*4;
    cout << "The perimeter of the square is: " << perimiterS << endl; 
    areaS = d*d;
    cout << "The area of the square is: " << areaS << endl;
    difference = areaS - areaC;
    cout << "The difference between the area of the square and the circle is: " << difference << endl;
}