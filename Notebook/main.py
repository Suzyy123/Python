#import tkinter for creating Gui
import tkinter as tk
from tkinter import filedialog, messagebox

#main window code
root = tk.Tk()
root.title("Sujita's Notebook")
root.geometry("800x600")

#create text area
text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Arial", 12)
)
text.pack(expand = True, fill = tk.BOTH)
#Function 1
def new_file():
    text.delete(1.0, tk.END)
#Function 2
def open_new_file():
    # open file dialog
    file_path = filedialog.askopenfilename(
        defaultextension = ".txt",
        filetypes =[("Text Files", "*.txt")]

    )
    if file_path:
        #open file
        with open(file_path, "r") as file: # r means read mode
            #clear old text
            text.delete(1.0, tk.END)#clear if something is there
            text.insert(tk.END, file.read() ) # file content insert gareko
#function 3
def save_file():
    #open save file dialogue
    file_path = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("Text Files", "*.txt")]
        )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("File saved successfully")
#MENU
menu = tk.Menu(root)
root.config(menu = menu)
file_menu = tk.Menu(menu)

#New, Open, Save, Exit
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label ="New", command = new_file)
file_menu.add_command(label ="Open", command = open_new_file)
file_menu.add_command(label ="Save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

#starts the window
root.mainloop()