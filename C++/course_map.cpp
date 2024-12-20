/*
Title: Lab10_1.cpp
Author: Ginnie Steck
Date:11/1/24
Perpose: uses maps to organize school courses
*/
#include <iostream>
using namespace std;
#include <string>
#include<map>


map<string, int> rooms =
{
{"CS101", 3004}, {"CS102", 4501},
{"CS103", 6755}, {"NT110", 1244},
{"CM241", 1411}
};

map<string, string> instructor =
{
{"CS101", "Haynes"}, {"CS102", "Alvarado"},
{"CS103", "Rich"}, {"NT110", "Burke"},
{"CM241", "Lee"}
};

map<string, string> times =
{
{"CS101", "8:00am"}, {"CS102", "9:00am"},
{"CS103", "10:00am"}, {"NT110", "11:00am"},
{"CM241", "1:00pm"}
};


int main(){
    string course;
    int valid = 0;

    while(valid == 0){
        cout << "Enter a course number: "; 
        cin >> course;
        for (const auto& rooms : rooms) {
            if (rooms.first == course){
                valid = 1;
                cout << rooms.first << ":" << endl;
                cout <<"\tRoom Number: " << rooms.second << endl;
            }
        }
        for (const auto& instructor : instructor) {
            if (instructor.first == course){
                cout <<"\tInstructor: " << instructor.second << endl;
            }
        }
        for (const auto& times : times) {
            if (times.first == course){
                cout <<"\tTime: " << times.second << endl;
            }
        }
        if(valid == 0){cout << "Invalid course number. " <<endl;}
    }

}