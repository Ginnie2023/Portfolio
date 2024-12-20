/*
Title: lab13_2.cpp
Author: Ginnie Steck
Date: 11/22/24
Perpose: Palindrome Detector
*/

#include <iostream>
using namespace std;
#include <string>
#include <cctype>

bool book(string phrase,int idx1, int idx2, int half, int count){

    if (phrase[idx1] == phrase[idx2]){
        if (count == half){return true;}
        return book(phrase,idx1+1,idx2-1,half,count+1);
    }
    if(phrase[idx1] != phrase[idx2]){return false;}
    return false;
};

int main(){
    string phrase; 
    char onward = 'y';
    cout << "Enter a text to check for palindrome: ";
    getline(cin,phrase);
    string phrase2;
    int len = phrase.size();
    for(int i=0; i<len; i++){
        if(isalpha(phrase[i])){
            phrase2 = phrase2 + static_cast<char>(tolower(phrase[i])); 
        }
    }
    
    int len2 = phrase2.size();
    int half = len2/2;
    if(book(phrase2,0,len2-1,half,0)){
        cout << "\"" << phrase << "\" is a palindrome.\n";
    }
    else if(!(book(phrase2,0,len2-1,half,0))){
        cout << "\"" << phrase << "\" is not a palindrome.\n";
    }
    cout << "Do you want to check another text? (y/n): ";
    cin >> onward;
    while (onward != 'n'){
        cin.ignore();
        cout << "Enter a text to check for palindrome: ";
        getline(cin,phrase);
        len = phrase.size();
        phrase2 = "";

        for(int i=0; i<len; i++){
            if(isalpha(phrase[i])){
                phrase2 = phrase2 + static_cast<char>(tolower(phrase[i])); 
            }
        }

        len2 = phrase2.size();
        half = len2/2;
        if(book(phrase2,0,len2-1,half,0)){
            cout << "\"" << phrase << "\" is a palindrome.\n";
        }
        else if(!(book(phrase2,0,len2-1,half,0))){
            cout << "\"" << phrase << "\" is not a palindrome.\n";
        }
        cout << "Do you want to check another text? (y/n): ";
        // cin.ignore();
        cin >> onward;
    }




}