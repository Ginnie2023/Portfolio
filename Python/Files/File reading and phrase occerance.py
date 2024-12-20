# -*- coding: utf-8 -*-
"""
processes a file given by user into a dictionary. 
asks user for words. Gives the lines that all words given are in. 

CSC130 PROGRAMMING ASSIGNMENT # 6 Fall 2023

By Ginnie 
"""

import string

def open_file(): 
    x=0
    file_path = input('Enter a file name: ')
    while x == 0:
        try:
            file= open(file_path, 'r')
            x=1
            return file
        except FileNotFoundError:
            print('File not found:' + file_path)
            file_path = input('File not Found...Enter another file name: ')
            
def read_data(fp):
    dictionary={}
    line_n=0
    
    for line in fp:
        line_n = line_n+1
        line = line.lower() 
        line = line.split() 
        for word in line: 
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.replace("'","")
            word = word.replace("-","")
            
            if word.isalpha() and len(word)>1:
                testing = dictionary.get(word)
                if testing is not None: 
                    dictionary[word].add(line_n)
                else:
                    dictionary[word] = {line_n}
    return dictionary
    
def find_cooccurance(D, inp_str):
    inp_str = inp_str.lower()
    inp_str = inp_str.translate(str.maketrans('', '', string.punctuation))
    inp_str = inp_str.replace("'","")
    inp_str = inp_str.replace("-","")
    inp_str = inp_str.split()
    none_a = [] #ask
    the_set = set()
    for i in inp_str:
        if i in D:
            if not the_set:
                the_set = D[i]
            else:
                the_set = the_set.intersection(D[i])
        else:
            return []
            #none_a = none_a + i #ask 
    the_set = sorted(the_set)
    return the_set
        
def main():
    a = open_file()
    b = read_data(a)
    x="d"
    while x != "Q" and x!= "q":
        user_input=input("Enter space seperated words, \nor to exit, enter 'q' or 'Q':")
        x = user_input
        if x !="q" and x != "Q": 
            lines = find_cooccurance(b,user_input)
            user_input = user_input.replace(" ",", ")
            print("The co-occurance for: " + user_input)
            if lines == []:
                print("Lines: None.")
            else:
                lines=', '.join(map(str, lines))
                print("Lines: " + lines)
            print("")
    

if __name__ == "__main__":
    main()








