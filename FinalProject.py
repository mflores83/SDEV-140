"""
Author: Mayte Flores
Assignment: Final Project
Program Name: "What's For Dinner?"
Description: This program will attempt to help busy people decide what will be for dinner for a week. 
This program will take inputs from the user on what they typically eat on the daily and store them in a file. 
Then it will pull from the information stored and print the required number of meals.
"""

import tkinter as tk

class MainWindow(tk.Tk):
    
    def __init__(self):
    
        #Main window that will include button selections
        super().__init__() 
        self.title("What's For Dinner?")
        self.geometry("600x400")

        #Label on the main window that welcomes the user
        label = tk.Label(self, text = "What's For Dinner? Let's find out!\nClick on any button to get started!")
        label.pack(pady=10)

        #Button that will link to add meal screen
        self.button1 = tk.Button(self, text="Add Meal",command= self.addMealWindow)
        self.button1.pack(pady=5)

        #Button that will link to Generate a Meal Plan
        self.button2 = tk.Button(self, text="Generate a Meal Plan", command=self.generateMealWindow)
        self.button2.pack(pady=5)

        #Button that will link to See Meal Plan window
        self.button3 = tk.Button(self, text= "See Meal Plan", command= self.seePlan)
        self.button3.pack(pady=5)

        #Button open window that displays meals in file in a text and allows the user to delete them
        self.allMeals = tk.Button(self, text = "See or Edit Meals Added", command= self.allMealsList)
        self.allMeals.pack(pady=5)

        #Button that allows the user to close the window
        self.button4 = tk.Button(self, text= "Quit", command= self.exit)
        self.button4.pack(pady=5)

        #File path for the "meals.txt" file because it would not find file in same folder
        self.filePath = "C:/Users/Admin/OneDrive/Documents/Spring 2025/SDEV-140/meals.txt"
        #Meals List for randomMeals
        self.mealsList = []

    def addMealWindow(self):
        "Allows the user to add a new meal to the list of meals"
        #Creates a second window
        secondWindow = tk.Toplevel(self)
        secondWindow.title = ("Add a New Meal")
        secondWindow.geometry("300x200")

        label = tk.Label(secondWindow, text= "Enter the meal name: ")
        label.pack()

        self.mealName = tk.Entry(secondWindow)
        self.mealName.pack()

        self.submitButton = tk.Button(secondWindow, text= "Submit Meal", command= self.submitMeal)
        self.submitButton.pack(pady=10)

        #Created a label to display message that meal was added or not
        self.messageLabel = tk.Label(secondWindow, text= "")
        self.messageLabel.pack(pady=5)

        self.closeButton = tk.Button(secondWindow, text= "Close", command= secondWindow.destroy)
        self.closeButton.pack(pady=5)

    def submitMeal(self):
        "Will submit the meal entered by the user, and save it into a txt file."
        meal = self.mealName.get()
    
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
        self.generateWindow = tk.Toplevel(self)
        self.generateWindow.title = ("Generate Meals")
        self.generateWindow.geometry("400x300")

        label = tk.Label(self.generateWindow, text= "Click the button below to generate a \nlist of meals for each day of the week")
        label.pack(pady=5)

        self.generateButton = tk.Button(self.generateWindow, text= "Generate",command=self.randomMeals)
        self.generateButton.pack(pady=10)

        self.generatedLabel = tk.Label(self.generateWindow, text = "")
        self.generatedLabel.pack(pady=5)

        self.closeButton = tk.Button(self.generateWindow, text= "Close", command= self.generateWindow.destroy)
        self.closeButton.pack(pady=5)

    def randomMeals(self):
        "Will randomize the meals and output them in a label on Generate window"
        #Source: https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file
        import random
        
        self.mealsList.clear()
        self.lines = open(self.filePath).read().splitlines()

        if len(self.lines) > 0:
            self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for day in self.days_of_week:
                self.meal = random.choice(self.lines)
                self.mealsList.append(f"{day}: {self.meal}")

            self.generatedLabel.config(text="\n".join(self.mealsList))
        else:
            self.generatedLabel.config(text= "No meals available. Please add meals first to display.")

    def seePlan(self):
        "Allows the user to see the plan that has been generated and saved."
        if not self.mealsList:
            self.mealsList = ["No plan generated yet. Generate one first to display."]

        self.planWindow = tk.Toplevel(self)
        self.planWindow.title = ("Meal Plan")
        self.planWindow.geometry("400x300")

        self.label = tk.Label(self.planWindow, text = "Below is the list of the meals generated for the week:")
        self.label.pack(pady=5)

        #Add a label that displays the meals per day, indented
        self.displayMeals = tk.Label(self.planWindow, text= "\n".join(self.mealsList))
        self.displayMeals.pack(pady=5)

        #Add a button that clears the meals saved
        self.clearMeals = tk.Button(self.planWindow, text= "Clear Meal Plan", command= self.clearPlan)
        self.clearMeals.pack(pady=5)

        self.closeButton = tk.Button(self.planWindow, text= "Close", command= self.planWindow.destroy)
        self.closeButton.pack(pady=5)


    def clearPlan(self):
        "Allows the user to clear the plan created and restart"
        self.mealsList.clear()
        self.displayMeals.config(text= "Meal plan has been cleared! \nClick \"Generate\" Button on home screen to create another one.")

    def allMealsList(self):
        "Will open a listbox window that displays all meals in file"
        self.allMealsWindow = tk.Toplevel(self)
        self.allMealsWindow.title = ("List of All Meals")
        self.allMealsWindow.geometry("400x400")

        self.label = tk.Label(self.allMealsWindow, text= "List of All Meals Added: ")
        self.label.pack(pady=5)
        
        listbox = tk.Listbox(self.allMealsWindow, height= 10, width= 50, selectmode= "multiple")
        listbox.pack(pady= 10)

        try:
            with open(self.filePath, "r") as file:
                meals = file.readlines()
                for meal in meals:
                    listbox.insert(tk.END, meal.strip())
        except FileNotFoundError:
            listbox.insert(tk.END, "No meals found. Please add meals first to display.")

        self.deletedLabel = tk.Label(self.allMealsWindow, text= "")
        self.deletedLabel.pack(pady=5)

        def deleteMeal():
            "Will add the option to delete a meal directly from the listbox window"
            #Source: https://stackoverflow.com/questions/31015774/removing-a-selection-from-a-listbox-as-well-as-remove-it-from-the-list-that-pro
            #Allows the user to select the meal through listbox and will delete it in listbox with delete button
            selectedItems = listbox.curselection()
            if selectedItems:
                selectedMeal = listbox.get(selectedItems[0])
                listbox.delete(selectedItems[0])

                #Will delete meal in file if meal is the same as the selected meal in listbox
                try:
                    with open(self.filePath, "r") as file:
                        meals = file.readlines()
                    meals = [meal for meal in meals if meal.strip() != selectedMeal]

                    with open(self.filePath, "w") as file:
                        file.writelines(meals)
                except FileNotFoundError:
                    self.deletedLabel.config(text= "File not found. Please check the file path.")
                self.deletedLabel.config(text= f"{selectedMeal} has been deleted.")
            else:
                self.deletedLabel.config(text= "No meal was selected.")


        self.deleteButton = tk.Button(self.allMealsWindow, text= "Delete Meal", command = deleteMeal)
        self.deleteButton.pack(pady=5)

        self.closeButton = tk.Button(self.allMealsWindow, text= "Close", command= self.allMealsWindow.destroy)
        self.closeButton.pack(pady=5)


    def exit(self):
        "Allows the user to close the program"
        self.destroy()

def mainLoop():
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    mainLoop()       

