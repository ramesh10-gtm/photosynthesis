# This program uses a turtle to depict a nested loop 
import turtle # import the turtle 

myPen = turtle.Turtle() # define turtle
myPen.speed(0)          # mention the speed 
myPen.color("Red")      # mention color 


for j in range (1,75):   # loop for direction in y axis with parameters 
  for i in range (1,3):  # loop for direction in x axis with parameters
      myPen.left(69)     # move the pen left with defined angle   
      myPen.forward(175) # move the pen forward 
  myPen.left(5)         # move the pen left 
