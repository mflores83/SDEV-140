"""
Author: Mayte Flores
Assignment: Final Project
Program Name: "What's For Dinner?"
Description: This program will attempt to help busy people decide what will be for dinner for a week. 
This program will take inputs from the user on what they typically eat on the daily and store them in a file. 
Then it will pull from the information stored and print the required number of meals.
"""
from breezypythongui import EasyFrame
import tkinter as tk

class MainWindow(EasyFrame):

    def __init__(self):
    
        #Main window that will include button selections
        mainWindow = tk.Tk()
        mainWindow.title("What's For Dinner?")
        mainWindow.geometry("600x400")

        label = tk.Label(mainWindow, text = "What's For Dinner?")
        label.pack()

        #Button that will link to add meal screen
        self.button1 = tk.Button(mainWindow, text="Add Meal",command= self.addMeal)
        self.button1.pack()

        #Button that will link to Generate a Meal Plan
        self.button2 = tk.Button(mainWindow, text="Generate a Meal Plan", command=self.generateMeal)
        self.button2.pack()

        self.button3 = tk.Button(mainWindow, text= "See Meal Plan", command= self.seePlan)
        self.button3.pack()

        self.button4 = tk.Button(mainWindow, text= "Quit", command= self.exit)

        def addMeal(self):
            "Allows the user to add a new meal to the list of meals"

        def generateMeal(self):
            "Will prompt the user to generate meals"

        def seePlan(self):
            "Allows the user to see the plan that has been generated and saved."

        def exit(self):
            "Allows the user to close the program"
            self.destroy()
            


def mainLoop():
    #Source: ChatGPT
    MainWindow().mainloop()

if __name__ == "__main__":
    mainLoop()       

