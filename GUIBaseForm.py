""" Set up the basic GUI shell and initial frames, menu bar """

import tkinter as tk
from tkinter import ttk

class BaseForm:

    def __init__(self):

        root = tk.Tk()

        root.title("Data Entry Screen")
        root.geometry('1000x1000')
        root.resizable(True, True)

        # upper_frame = tk.Frame(root, width=800, height=300, bd=5, bg="aqua", relief="sunken")
        # upper_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=30)
        #
        # lower_frame = tk.Frame(root, width=800, height=300, bd=5, bg="grey", relief="sunken")
        # lower_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=30)


        tk.mainloop()

bf = BaseForm()




