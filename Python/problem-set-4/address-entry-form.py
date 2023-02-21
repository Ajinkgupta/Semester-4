import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frame1 = tk.Frame(master=window)
frame1["relief"] = tk.SUNKEN
frame1["borderwidth"] = 3
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.X)

list = {
    0: "First Name",
    1: "Last Name",
    2: "Address Line 1",
    3: "Address Line 2",
    4: "City",
    5: "State/Province",
    6: "Postal Code",
    7: "Country",
}

for i in list:
    label = tk.Label(master=frame1)
    label["text"] = list[i] + ":"
    label.grid(row=i, column=0, sticky=tk.E)

    entry = tk.Entry(master=frame1)
    entry["width"] = 50
    entry.grid(row=i, column=1)

button1 = tk.Button(master=frame2)
button1["text"] = "Submit"
button1["width"] = 7
button1["height"] = 1
button1.pack(padx=5, pady=5, side=tk.RIGHT)

button2 = tk.Button(master=frame2)
button2["text"] = "Clear"
button2["width"] = 5
button2["height"] = 1
button2.pack(padx=5, pady=5, side=tk.RIGHT)

window.mainloop()
