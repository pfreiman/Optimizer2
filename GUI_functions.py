""" Set up the basic GUI shell and the entry fields, i.e. checkboxes and radiobuttons"""

import tkinter as tk

import CardiologyToolkit

criteria = ['test1', 'test2', 'test3', 'test4']
second_list_radio = ['Larry', 'Moe', 'Curly', 'Shepp']
third_list_radio = ['Mercury', 'Venus', 'Earth', 'Mars']


class GUIShell:

    def __init__(self):

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

        """ Create checkboxes on the GUI screen"""

        def CreateCheckBoxes(self, criteria_list):

            checkboxes = {}

            # global item variable is selected item in combobox
            Cbcolumn = 3
            Cbrow = 6
            Chkcount = 0

            #  checkboxes = {}    #    resets checkboxes dictionary and clears any prior values

            for Checkbox in range(len(criteria_list)):

                name = criteria_list[Checkbox]
                current_var = tk.IntVar()
                current_box = tk.Checkbutton(upper_frame, text=name, font="Arial,16", height=2, width=20, bg="aqua",
                                             fg="blue",
                                             variable=current_var)
                current_box.var = current_var
                current_box.grid(row=Cbrow, column=Cbcolumn)
                checkboxes[current_box] = name  # so checkbutton object is the key and value is string
                if Cbcolumn == 5:
                    Cbcolumn = 3
                    Cbrow += 1
                else:
                    Cbcolumn += 1
                Chkcount += 1



        CreateCheckBoxes(self, criteria)



        """Create dictionary from checkbox selections"""

        def CreateDictionary(self):
            kl = []
            vl = []
            for box in checkboxes:
                key = str(checkboxes[box])
                # print("Key:", key)
                value = int(box.var.get())
                # print("Value", value)

                kl.append(key)
                vl.append(value)

                # print("Built lists:", kl, vl)  # debug
                my_tools.response_dict = dict(zip(kl, vl))

            print("Dictionary of responses is:", my_tools.response_dict)  # debug
            my_tools.result_text = "Dictionary of responses is:", my_tools.response_dict
            return my_tools.response_dict

        """ Create radiobuttons on the GUI"""

        def CreateRadioButtons(self):
            top_label = tk.Label(lower_frame, text="Choose a diagnosis:")
            top_label.grid(row=0, column=0, columnspan=4)

            v1 = tk.StringVar()
            v2 = tk.StringVar()


            chosen_list = second_list_radio
            print(chosen_list)

            def get_entries():
                print(v1.get())
                print(v2.get())

            def ShowChoice():
                print(v1.get())

            def ShowChoice2():
                print(v2.get())

            idx = 0
            for item in chosen_list:
                tk.Radiobutton(lower_frame,
                               text=item, fg="blue",
                               pady=10,
                               variable=v1,
                               command=ShowChoice,
                               indicatoron=0,
                               value=item).grid(row=1, column=idx)
                idx += 1

            second_label = tk.Label(lower_frame, text="\n\nEnter one criterion:")
            second_label.grid(row=2, pady=10, columnspan=4)

            chosen_list = third_list_radio
            print(chosen_list)

            idx = 0
            for item in chosen_list:
                tk.Radiobutton(lower_frame,
                               text=item, fg="blue",
                               pady=10,
                               variable=v2,
                               command=ShowChoice2,
                               indicatoron=0,
                               value=item).grid(row=3, column=idx)
                idx += 1

        CreateRadioButtons(self)

        tk.mainloop()


GUIShell()
# GUIShell.CreateCheckBoxes(criteria)
