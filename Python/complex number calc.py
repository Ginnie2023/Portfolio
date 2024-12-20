# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:38:01 2023

Complex number calculator  given two imagenary parts and two real parts. 

By Ginnie Steck
"""

from tkinter import *
import math
import Cplex

class CplexCalc():
    def __init__(self):
        window=Tk()
        window.title("Complex Calculator")
        
        # create lables
        Label(window,text="First Complex:").grid(row=1,column=1,sticky=W)
        Label(window,text="Second Complex:").grid(row=4,column=1,sticky=W)
        Label(window,text="Real Part").grid(row=3,column=2,sticky=W)
        Label(window,text="Imaginary Part").grid(row=3,column=4,sticky=W)
        Label(window,text="Real Part").grid(row=6,column=2,sticky=W)
        Label(window,text="Imaginary Part").grid(row=6,column=4,sticky=W)
        Label(window,text="Operation").grid(row=7,column=1,sticky=W)
        Label(window,text="Add").grid(row=8,column=2)
        Label(window,text="Subtract").grid(row=8,column=3)
        Label(window,text="Multiply").grid(row=8,column=4)
        Label(window,text="Devide").grid(row=8,column=5)
        Label(window,text="Result").grid(row=9,column=1,sticky=W)
        Label(window,text="Real Part").grid(row=10,column=2,sticky=W)
        Label(window,text="Imaginary").grid(row=10,column=4,sticky=W)
        
        #create text box 
        self.firstCplexRealVar=StringVar()
        Entry(window,textvariable=self.firstCplexRealVar,justify=LEFT).grid(row=2,column=2)
        self.firstCplexImagVar=StringVar()
        Entry(window,textvariable=self.firstCplexImagVar,justify=LEFT).grid(row=2,column=4)
        self.secondCplexRealVar=StringVar()
        Entry(window,textvariable=self.secondCplexRealVar,justify=LEFT).grid(row=5,column=2)
        self.secondCplexImagVar=StringVar()
        Entry(window,textvariable=self.secondCplexImagVar,justify=LEFT).grid(row=5,column=4)
        self.resultRealVar=StringVar()
        Entry(window,textvariable=self.resultRealVar,justify=LEFT).grid(row=9,column=2)
        self.resultImagVar=StringVar()
        Entry(window,textvariable=self.resultImagVar,justify=LEFT).grid(row=9,column=4)
        
        #buttons
        btAdd=Button(window,text="+",command=self.addCplex).grid(row=7,column=2)
        btSub=Button(window,text="-",command=self.subCplex).grid(row=7,column=3)
        btMult=Button(window,text="*",command=self.multCplex).grid(row=7,column=4)
        btDiv=Button(window,text="/",command=self.divCplex).grid(row=7,column=5)
        btClear=Button(window,text="Clear Entries",command=self.clearEntries).grid(row=11, column=2, columnspan=3)
        
        window.mainloop()
        
    def addCplex(self):
        try:
            complex1 = Cplex.Cplex(float(self.firstCplexRealVar.get()), float(self.firstCplexImagVar.get()))
            complex2 = Cplex.Cplex(float(self.secondCplexRealVar.get()), float(self.secondCplexImagVar.get()))

            # Add the two complex numbers
            result = complex1 + complex2
            # Print the result
            self.resultRealVar.set(result.get_RealPart())
            self.resultImagVar.set(result.get_ImagPart())
        except ValueError:
            self.resultRealVar.set("Invalid Entries")
            self.resultImagVar.set("Invalid Entries")
        
    def subCplex(self):
        try:
        
            complex1 = Cplex.Cplex(float(self.firstCplexRealVar.get()), float(self.firstCplexImagVar.get()))
            complex2 = Cplex.Cplex(float(self.secondCplexRealVar.get()), float(self.secondCplexImagVar.get()))

        
            result = complex1 - complex2
        
            self.resultRealVar.set(result.get_RealPart())
            self.resultImagVar.set(result.get_ImagPart())
        except ValueError:
            self.resultRealVar.set("Invalid Entries")
            self.resultImagVar.set("Invalid Entries")
          
    def multCplex(self):
        try:
            complex1 = Cplex.Cplex(float(self.firstCplexRealVar.get()), float(self.firstCplexImagVar.get()))
            complex2 = Cplex.Cplex(float(self.secondCplexRealVar.get()), float(self.secondCplexImagVar.get()))

        
            result = complex1 * complex2

       
            self.resultRealVar.set(result.get_RealPart())
            self.resultImagVar.set(result.get_ImagPart()) 
        except ValueError:
            self.resultRealVar.set("Invalid Entries")
            self.resultImagVar.set("Invalid Entries")
        
    def divCplex(self):
        try:
            complex1 = Cplex.Cplex(float(self.firstCplexRealVar.get()), float(self.firstCplexImagVar.get()))
            complex2 = Cplex.Cplex(float(self.secondCplexRealVar.get()), float(self.secondCplexImagVar.get()))

    
            result = complex1 / complex2

            self.resultRealVar.set(result.get_RealPart())
            self.resultImagVar.set(result.get_ImagPart())
        except ValueError:
            self.resultRealVar.set("Invalid Entries")
            self.resultImagVar.set("Invalid Entries")
        
    def clearEntries(self):
        self.firstCplexRealVar.set("")
        self.firstCplexImagVar.set("")
        self.secondCplexRealVar.set("")
        self.secondCplexImagVar.set("")
        self.resultRealVar.set("")
        self.resultImagVar.set("")
        
        
        
CplexCalc()
