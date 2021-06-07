from tkinter import *
from tkinter import ttk


from CardiologyToolkit import CardiologyToolkit


root = Tk()
my_tools = CardiologyToolkit()

root.title("Data Entry Screen")
root.geometry('1000x1000')
root.resizable(True, True)

upper_frame = Frame(root, width=800, height=300, bd=5, bg="aqua", relief="sunken")
upper_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=30)


checkboxes = {}
# global item variable is selected item in combobox

""" First function puts the checkboxes on the GUI screen"""


def CreateCheckBoxes(criteria_list):


    Cbcolumn = 3
    Cbrow = 6
    Chkcount = 0

    #  checkboxes = {}    #    resets checkboxes dictionary and clears any prior values

    for Checkbox in range(len(criteria_list)):

        name = criteria_list[Checkbox]
        current_var = IntVar()
        current_box = Checkbutton(upper_frame, text=name, font="Arial,16", height=2, width=20, bg="aqua", fg="blue", variable=current_var)
        current_box.var = current_var
        current_box.grid(row=Cbrow, column=Cbcolumn)
        checkboxes[current_box] = name  # so checkbutton object is the key and value is string
        if Cbcolumn == 5:
            Cbcolumn = 3
            Cbrow += 1
        else:
            Cbcolumn += 1
        Chkcount += 1


def checkboxesclear():
    checkboxes = {}
    return checkboxes

CreateCheckBoxes(my_tools.get_current_criteria_list())

#  print(checkboxes)  # debug


""" Next function creates the dictionary of responses from checkboxes"""


def CreateDictionary():
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


def show_result_in_label():
    a = CreateDictionary()
    labeltext = str(a)
    my_tools.result_text = ("Final entries are", labeltext)
    result_label = Label(root, text=my_tools.result_text, font="helvetica, 12", bg='gray', fg='yellow',
                         relief='sunken')

    my_tools.current_function = my_tools.get_current_score_or_rec_function()

    result_label.config(text=str(my_tools.result_text) + "\n\n" + my_tools.item + " is: \n\n" + str(my_tools.current_function))
       #  result_label.config(text=str(result_text) + "\n\n" + item + " is: \n\n" + str(
        #  Functions_list.CHADS_VASc_score_dictionary_method(response_dict)))
    # print("CF is:", current_function)
    # result_label.config(text=str(result_text) + "\n\n" + item + " is: \n\n" + str(current_function))
    result_label.grid(row=16, pady=50, column=1, columnspan=3)
    #  print("Result text is:", result_text)


def show_response_text():
    print("Final result text is:", my_tools.result_text) # debug to see if variable is global and value is saved

def open_new_window():

    my_tools.current_function = my_tools.get_current_score_or_rec_function()

    my_tools.showtext = str(my_tools.result_text) + "\n\n" + my_tools.item + " is:  \n\n" + str(my_tools.current_function)


    new = Toplevel()
    new.title("Results")
    new.geometry('800x800')
    new.resizable(True, True)

    res_label=Label(new, text="Results appear here:  " + my_tools.showtext, font=("Helvetica", 16),  bg="yellow")
    res_label.grid(row=2, column=1, columnspan=3, pady=50)

    res_close_button = Button(new, text="Close", command=new.destroy)
    res_close_button.grid(row=4, column=3, pady=50)

    res_references = Button(new, text="References")
    res_references.grid(row=4, column=2, pady=50)

    res_more_button = Button(new, text="More")
    res_more_button.grid(row=4, column=1, pady=50)

    print("Show text in new window is:", my_tools.showtext)

    new.mainloop()


""" Functions for menus:"""

def new_command():
    pass

def cut_command():
    pass

def copy_command():
    pass

def paste_command():
    pass


first_label = Label(upper_frame, text="Make entries:", font="Helvetica, 20", fg="blue")
first_label.grid(row=0, column=0)

combo_label = Label(root, text="Select topic:", fg="blue", font="Helvetica, 24")
combo_label.grid(row=0, column=2, pady=10, padx=10)

print_cbox_button = Button(root, text='Print dictionary', font="Helvetica, 24", fg="orange", relief='ridge', command=CreateDictionary)
print_cbox_button.grid(row=10, pady=50, column=1, columnspan=3)

result_button = Button(root, text="Show Calculated Result", font="Helvetica, 24", fg="red", command=show_result_in_label)
result_button.grid(row=14, pady=50, column=1, columnspan=3)

open_button = Button(root, text="Open new Results window", font="Helvetica, 24", fg="green", command = open_new_window)
open_button.grid(row=18, column=1, columnspan=3, pady=50)

quit_button = Button(root, text="Exit", font="Helvetica, 24", fg="blue", command=quit)
quit_button.grid(row=22, pady=50, column=3)

# show_label_button = Button(root, text= "Show response text", font="Helvetica, 20", fg="blue", command=show_response_text)
# show_label_button.grid(row=14, column=0, columnspan=3)

# CHADS_button = Button(root, text="Calculate CHADS score", fg="red", font="Helvetica, 20", command=CHADS_VASc_score_dictionary_method(response_dict))
# CHADS_button.grid(row=20, pady=20, column=0, columnspan=3)


#  create a File menu

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


#  create an Edit menu

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_command)
edit_menu.add_command(label="Copy", command=copy_command)
edit_menu.add_command(label="Paste", command=paste_command)






# make a combo box that includes the criteria lists:


def combocallbackfunc(event):
    my_tools.item = my_combo.get()
    print("Combo item is:", my_tools.item)
    checkboxesclear()
    CreateCheckBoxes(my_tools.get_current_criteria_list())

options = [
    "",
    "CHADS score",
    "CHADS-VASc score",
    "Post-code algorithm"
    ]

my_combo = ttk.Combobox(root, value=options, state = "readonly")
my_combo.current(0)
my_combo.grid(row=0, column=3, padx=10, pady=10)

my_combo.bind("<<ComboboxSelected>>", combocallbackfunc)


root.mainloop()

# print("GUI loop is over. stored variables are:", response_dict, result_text)
# print('response dict is:', response_dict)
# print("result text is", result_text)



"""

Comments:
So... if "Quit" the application, all variable values are lost.
But... if close only the GUI, all global variable values are SAVED, and the program still runs....





Also probably needs some way to reset the global checkboxes dictionary if this function is ran more than once.

"""
