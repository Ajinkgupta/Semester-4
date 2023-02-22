import tkinter as tk
import random

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")
        
        # create the slot machine slots
        self.slot1 = tk.Label(master, text=" ", font=("Arial", 100))
        self.slot1.grid(row=0, column=0)
        self.slot2 = tk.Label(master, text=" ", font=("Arial", 100))
        self.slot2.grid(row=0, column=1)
        self.slot3 = tk.Label(master, text=" ", font=("Arial", 100))
        self.slot3.grid(row=0, column=2)
        
        # create the roll button
        self.roll_button = tk.Button(master, text="Roll Again", command=self.roll_slots)
        self.roll_button.grid(row=1, column=1)
        
    def roll_slots(self):
        # generate random numbers for each slot
        slot1_value = random.randint(1, 9)
        slot2_value = random.randint(1, 9)
        slot3_value = random.randint(1, 9)
        
        # update the text of each slot to display the random number
        self.slot1.config(text=str(slot1_value))
        self.slot2.config(text=str(slot2_value))
        self.slot3.config(text=str(slot3_value))
        
root = tk.Tk()
game = SlotMachine(root)
root.mainloop()
