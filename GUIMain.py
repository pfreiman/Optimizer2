""" Create the base form"""


import tkinter as tk

import GUIFormFunctions

import CardiologyToolkit



class MainApplication(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        root = tk.Tk()

        root.title("Data Entry Screen")
        root.geometry('1000x1000')
        root.resizable(True, True)

        upper_frame = tk.Frame(root, width=800, height=300, bd=5, bg="aqua", relief="sunken")
        upper_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=30)

        lower_frame = tk.Frame(root, width=800, height=300, bd=5, bg="grey", relief="sunken")
        lower_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=30)

        def new_command(self):
            pass

        def cut_command(self):
            pass

        def copy_command(self):
            pass

        def paste_command(self):
            pass

            #  create a File menu

        my_menu = tk.Menu(root)
        root.config(menu=my_menu)

        file_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=new_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        #  create an Edit menu

        edit_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=cut_command)
        edit_menu.add_command(label="Copy", command=copy_command)
        edit_menu.add_command(label="Paste", command=paste_command)


        #  GUIFormFunctions.FormMethods.create_checkboxes(self, criteria_list)   #  THIS YIELDS ERROR-- "criteria_list" not defined...

        tk.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()