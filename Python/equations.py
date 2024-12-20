# -*- coding: utf-8 -
"""
Class that initilizes linear equations given m and b. 
It also calculates the value of the equation given x. 
It composes two equations. It also finds the sum of two equations. 


CSC 130 Fall 2023 Programming Assignment 7

By Ginnie Steck 

"""

class Linear_equations():
        def __init__(self,m,b):
            self.m = m
            self.b = b
        def __str__(self):
            return "y = " + str(self.m) + "x + " + str(self.b)
        def value(self,x):
            self.x = x
            answer= (self.m * self.x) + self.b
            return answer
        def compose(self , linearEquation):
            improved_m = self.m * linearEquation.m 
            improved_b = self.m * linearEquation.b + self.b
            return Linear_equations(improved_m,improved_b)
        def __add__(self, linearEquation): 
            improved_m = self.m + linearEquation.m 
            improved_b = self.b + linearEquation.b 
            return Linear_equations(improved_m,improved_b)

            
if __name__ == "__main__":
    
    
    

    y=Linear_equations(int(input("Enter m for equation 1: ")),int(input("Enter b for equation 1: ")))
    z=Linear_equations(int(input("Enter m for equation 2: ")),int(input("Enter b for equation 2: ")))
    x=int(input("Enter x for both equations: "))
    
    print("Equation 1:", y)
    print("Equation 2:", z)
    print("Value of Equation 1 when x equales", str(x) +":",y.value(x))
    print("Value of Equation 2 when x equales", str(x) +":",z.value(x))
    print("Composition of the equations \nin the form of Equation 1(Equation 2):",y.compose(z))
    print("Composition of the equations \nin the form of Equation 2(Equation 1):",z.compose(y))
    print("The sum of the equations is:",str(y+z))


