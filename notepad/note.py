import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents","*.txt"), ("All Files","*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents","*.txt"), ("All Files","*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                content = text_area.get(1.0, tk.END)
                file.write(content)
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Create main window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

# Text area
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
