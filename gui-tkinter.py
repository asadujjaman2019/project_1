import tkinter
from tkinter import ttk

# maim frame
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()
# main frame

# Saving user information Label frame
user_info_frame = tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row=0, column=0)

first_name_label = tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0, padx=20, pady=20)

last_name_label = tkinter.Label(user_info_frame,text="last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label =  tkinter.Label(user_info_frame,text="Title")
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)

age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality" )
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Asia"])
nationality_combobox.grid(row=3, column=1)

# Add padding to all grid in parent user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# Add padding to all grid in parent user_info_frame

# saving user information Label frame

window.mainloop()

