import tkinter as tk
from tkinter import font

def on_window_resize(event):
    width = event.width
    height = event.height
    print(f"Window resized to {width}x{height}")

# Create the main window
window = tk.Tk()
window.geometry("300x300")
window.title("PythonExamples.org")

# Bind the resize event to a function
window.bind("<Configure>", on_window_resize)

# Run the application
window.mainloop()