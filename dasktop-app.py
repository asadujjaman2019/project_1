import tkinter as tk

window=tk.Tk()
window.title("SAMPLE DESKTOP APP")
window.geometry("700x500")
window.state('zoomed')

label = tk.Label(window, text="Click the Button to update this Text",
font=('Calibri 15 bold'))
label.pack(pady=29)


# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You clicked first button"


# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked second button"


# Create 1st button to update the label widget
btn1 = tk.Button(window, text="Button1", command=on_click_btn1)
btn1.pack(pady=20)

# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="Button2", command=on_click_btn2)
btn2.pack(pady=40)

text_box = tk.Text()
text_box.pack()
text_box.get("1.0")
frame = tk.Frame()
frame.pack()

window.mainloop()

