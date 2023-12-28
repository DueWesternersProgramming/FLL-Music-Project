"""The module that creates an error window"""
import tkinter
import customtkinter as ct

def new_error_window(error, exception):
    """Function prints the error and displays an error window"""
    print("\n" + error + "\n" + str(exception))

    error_window = tkinter.Tk()
    error_window.geometry("400x150")
    error_window.title("Error")
    error_window.configure(background="#242424")
    error_window.resizable(True, False)

    error_text = ct.CTkLabel(error_window,text=error,text_color="#dce4ee")
    error_text.configure(font=("Serif", 15))
    error_text.pack(fill="both",expand=True)
