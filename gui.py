import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title("Merge Excel")
window.geometry("640x400+100+100")
window.resizable(False, False)

def ask():
	window.dirName = filedialog.askdirectory()
	label.configure(text="선택된 폴더: " + window.dirName)


btn = tk.Button(window, text="폴더 선택", command=ask)
btn.pack()

label = tk.Label(window, text="선택된 폴더")
label.pack()


window.mainloop()