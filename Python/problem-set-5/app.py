import mysql.connector
from tkinter import *
from tkinter import ttk

# Establish database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)

# Create cursor
cursor = db.cursor()

# Create GUI
root = Tk()
root.title("CRUD Application")

root.configure(bg="#f2f2f2")

 # Create form fields
first_name_label = Label(root, text="First Name", font=("Arial", 12))
first_name_label.grid(row=0, column=0, padx=10, pady=10)
first_name_entry = Entry(root, font=("Arial", 12))
first_name_entry.grid(row=0, column=1, padx=10, pady=10)

last_name_label = Label(root, text="Last Name", font=("Arial", 12))
last_name_label.grid(row=1, column=0, padx=10, pady=10)
last_name_entry = Entry(root, font=("Arial", 12))
last_name_entry.grid(row=1, column=1, padx=10, pady=10)

contact_label = Label(root, text="Contact Number", font=("Arial", 12))
contact_label.grid(row=2, column=0, padx=10, pady=10)
contact_entry = Entry(root, font=("Arial", 12))
contact_entry.grid(row=2, column=1, padx=10, pady=10)

city_label = Label(root, text="City", font=("Arial", 12))
city_label.grid(row=3, column=0, padx=10, pady=10)
city_entry = Entry(root, font=("Arial", 12))
city_entry.grid(row=3, column=1, padx=10, pady=10)

state_label = Label(root, text="State", font=("Arial", 12))
state_label.grid(row=4, column=0, padx=10, pady=10)
state_entry = Entry(root, font=("Arial", 12))
state_entry.grid(row=4, column=1, padx=10, pady=10)

dob_label = Label(root, text="Date of Birth", font=("Arial", 12))
dob_label.grid(row=5, column=0, padx=10, pady=10)
dob_entry = Entry(root, font=("Arial", 12))
dob_entry.grid(row=5, column=1, padx=10, pady=10)

 # Create buttons
insert_button = Button(root, text="Insert", font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10, bd=0)
insert_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

update_button = Button(root, text="Update", font=("Arial", 12), bg="#008CBA", fg="white", padx=20, pady=10, bd=0)
update_button.grid(row=6, column=1, padx=10, pady=10, sticky="we")

delete_button = Button(root, text="Delete", font=("Arial", 12), bg="#f44336", fg="white", padx=20, pady=10, bd=0)
delete_button.grid(row=6, column=2, padx=10, pady=10, sticky="we")

view_button = Button(root, text="View All", font=("Arial", 12), bg="#555555", fg="white", padx=20, pady=10, bd=0)
view_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky="we")

# Configure button appearance when mouse hovers over it
hover_bg_color = "#f0f0f0"
insert_button.bind("<Enter>", lambda event: insert_button.config(bg=hover_bg_color))
insert_button.bind("<Leave>", lambda event: insert_button.config(bg="#4CAF50"))
update_button.bind("<Enter>", lambda event: update_button.config(bg=hover_bg_color))
update_button.bind("<Leave>", lambda event: update_button.config(bg="#008CBA"))
delete_button.bind("<Enter>", lambda event: delete_button.config(bg=hover_bg_color))
delete_button.bind("<Leave>", lambda event: delete_button.config(bg="#f44336"))
view_button.bind("<Enter>", lambda event: view_button.config(bg=hover_bg_color))
view_button.bind("<Leave>", lambda event: view_button.config(bg="#555555"))



# Create text widget to display records
tree = ttk.Treeview(root, columns=("First Name", "Last Name", "Contact Number", "City", "State", "Date of Birth"), show="headings")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Contact Number", text="Contact Number")
tree.heading("City", text="City")
tree.heading("State", text="State")
tree.heading("Date of Birth", text="Date of Birth")
tree.column("First Name", width=100)
tree.column("Last Name", width=100)
tree.column("Contact Number", width=100)
tree.column("City", width=100)
tree.column("State", width=100)
tree.column("Date of Birth", width=100)
tree.grid(row=8, column=0, columnspan=3, padx=10, pady=10)


# Define button actions
def insert_record():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    contact = contact_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    dob = dob_entry.get()
    cursor.execute("INSERT INTO records (first_name, last_name, contact, city, state, dob) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, last_name, contact, city, state, dob))
    db.commit()

def update_record():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    contact = contact_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    dob = dob_entry.get()
    cursor.execute("UPDATE records SET last_name = %s, contact = %s, city = %s, state = %s, dob = %s WHERE first_name = %s", (last_name, contact, city, state, dob, first_name))
    db.commit()

def delete_record():
    first_name = first_name_entry.get()
    cursor.execute("DELETE FROM records WHERE first_name = %s", (first_name,))
    db.commit()

def view_records():
    # Clear any existing records in the Treeview widget
    tree.delete(*tree.get_children())
    
    # Retrieve records from database and display in the Treeview widget
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    for record in records:
        tree.insert("", "end", values=record)

# Bind buttons to actions
insert_button.config(command=insert_record)
update_button.config(command=update_record)
delete_button.config(command=delete_record)
view_button.config(command=view_records)






# Run GUI
root.mainloop()

# Close database connection
db.close()
