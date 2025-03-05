"""
Author: Mayte Flores
Assignment: Final Project
Program Name: "What's For Dinner?"
Description: This program will attempt to help busy people decide what will be for dinner for a week. 
This program will take inputs from the user on what they typically eat on the daily and store them in a file. 
Then it will pull from the information stored and print the required number of meals.
"""

import tkinter as tk

class MainWindow:
    
    def __init__(self):
    
        #Main window that will include button selections
        self.mainWindow = tk.Tk()
        self.mainWindow.title("What's For Dinner?")
        self.mainWindow.geometry("600x400")

        label = tk.Label(self.mainWindow, text = "What's For Dinner?")
        label.pack()

        #Button that will link to add meal screen
        self.button1 = tk.Button(self.mainWindow, text="Add Meal",command= self.addMealWindow)
        self.button1.pack()

        #Button that will link to Generate a Meal Plan
        self.button2 = tk.Button(self.mainWindow, text="Generate a Meal Plan", command=self.generateMealWindow)
        self.button2.pack()

        self.button3 = tk.Button(self.mainWindow, text= "See Meal Plan", command= self.seePlan)
        self.button3.pack()

        self.button4 = tk.Button(self.mainWindow, text= "Quit", command= self.exit)
        self.button4.pack()

        self.filePath = "C:/Users/Admin/OneDrive/Documents/Spring 2025/SDEV-140/meals.txt"

    def addMealWindow(self):
        "Allows the user to add a new meal to the list of meals"
        #Creates a second window
        secondWindow = tk.Toplevel(self.mainWindow)
        secondWindow.title = ("Add a New Meal")
        secondWindow.geometry("300x200")

        label = tk.Label(secondWindow, text= "Enter the meal name: ")
        label.pack()

        self.mealName = tk.Entry(secondWindow)
        self.mealName.pack()

        self.submitButton = tk.Button(secondWindow, text= "Submit Meal", command= self.submitMeal)
        self.submitButton.pack()

        #Created a label to display message that meal was added or not
        self.messageLabel = tk.Label(secondWindow, text= "")
        self.messageLabel.pack()

        #List that displays the meals added so far

    def submitMeal(self):
        "Will submit the meal entered by the user, and save it into a txt file."
        meal = self.mealName.get()
        #Had to add file path because it would not find file in same folder.
        self.filePath = "C:/Users/Admin/OneDrive/Documents/Spring 2025/SDEV-140/meals.txt"

        #Checks for input and displays label
        if meal:
            with open(self.filePath,"a") as file:
                file.write(meal + "\n")
                file.flush()
            self.messageLabel.config(text= f"Meal added: {meal}")
            self.mealName.delete(0,tk.END)
        else:
            self.messageLabel.config(text= "No meal entered.")

    def generateMealWindow(self):
        "Will prompt the user to generate meals"
        self.generateWindow = tk.Toplevel(self.mainWindow)
        self.generateWindow.title = ("Generate Meals")
        self.generateWindow.geometry("400x300")

        label = tk.Label(self.generateWindow, text= "Click the button below to generate a \nlist of meals for each day of the week")
        label.pack()

        self.generateButton = tk.Button(self.generateWindow, text= "Generate",command=self.randomMeals)
        self.generateButton.pack()

        self.generatedLabel = tk.Label(self.generateWindow, text = "")
        self.generatedLabel.pack()

    def randomMeals(self):
        "Will randomize the meals and output them in a label on Generate window"
        #Source: https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file
        import random
        self.lines = open(self.filePath).read().splitlines()
        self.myline = random.choice(self.lines)
        self.mealsList = []
        self.generatedLabel.config(text= self.myline)
        
        

    def seePlan(self):
        "Allows the user to see the plan that has been generated and saved."

    def exit(self):
        "Allows the user to close the program"
        self.master.quit()
            


def mainLoop():
    #Source: ChatGPT
    app = MainWindow()
    app.mainWindow.mainloop()

if __name__ == "__main__":
    mainLoop()       

