from tkinter import *
from tkinter import ttk


import Criteria_list_constants
from Criteria_list_constants import *

root = Tk()

root.title("Data Entry Screen")
root.geometry('1000x1000')
root.resizable(True, True)

# criteria_list = ['CHF', 'HTN', 'AGE', 'Diabetes', 'Stroke_hx']  # literal list of criteria list
criteria_list = Criteria_list_constants.cl_CHADS  # pulls in criteria list constant from constants file

#  criteria_list = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo','Foxtrot']
#  criteria_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print("Criteria list:", criteria_list)

checkboxes = {}
response_dict = {}
result_text = ""

""" First function puts the checkboxes on the GUI screen"""


def CreateCheckBoxes(criteria_list):
    Cbcolumn = 3
    Cbrow = 6
    Chkcount = 0

    for Checkbox in range(len(criteria_list)):
        name = criteria_list[Checkbox]
        current_var = IntVar()
        current_box = Checkbutton(root, text=name, font="Arial,20", height=2, width=10, fg="blue", variable=current_var)
        current_box.var = current_var
        current_box.grid(row=Cbrow, column=Cbcolumn)
        checkboxes[current_box] = name  # so checkbutton object is the key and value is string
        if Cbcolumn == 4:
            Cbcolumn = 3
            Cbrow += 1
        else:
            Cbcolumn += 1
        Chkcount += 1


CreateCheckBoxes(criteria_list)

#  print(checkboxes)  # debug


""" Next function creates the dictionary of responses from checkboxes"""


def CreateDictionary():
    global response_dict
    # print("checkbox list:", checkboxes)
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
        response_dict = dict(zip(kl, vl))

    print("Dictionary of responses is:", response_dict)  # debug
    result_text = "Dictionary of responses is:", response_dict
    return response_dict


def show_result_in_label():
    a = CreateDictionary()
    global result_text
    labeltext = str(a)
    result_text = ("Final entries are", labeltext)
    result_label = Label(root, text=result_text, font="helvetica, 24", bg='gray', fg='yellow',
                         relief='sunken')
    result_label.config(text=str(result_text) + "\n\n CHADS score is:  " + str(CHADS_VASc_score_dictionary_method(response_dict)))
    result_label.grid(row=16, pady=50, column=1, columnspan=4)
    #  print("Result text is:", result_text)


def CHADS_VASc_score_dictionary_method(entries):
    chads_vasc_score = 0
    # entries = response_dict

    print("Entries are:", entries)  # debug

    if entries['CHF'] == 1:
        chads_vasc_score += 1
    if entries['HTN'] == 1:
        chads_vasc_score += 1
    if entries['AGE'] == 1:
        chads_vasc_score += 1
    if entries['Diabetes'] == 1:
        chads_vasc_score += 1
    if entries['Stroke_hx'] == 1:
        chads_vasc_score += 2
    # if entries['Vascular_Disease'] == 'Y':
    #     chads_vasc_score += 1
    # if entries['Female_Gender'] == 'Y':
    #     chads_vasc_score += 1

    print("\n\nCHADS-VASc score is: ", chads_vasc_score)
    return chads_vasc_score

def show_response_text():
    print("Final result text is:", result_text) # debug to see if variable is global and value is saved

def open_new_window():

    global showtext
    showtext = str(result_text) + "\n\n CHADS score is:  " + str(CHADS_VASc_score_dictionary_method(response_dict))


    new = Toplevel()
    new.title("Results")
    new.geometry('800x800')
    new.resizable(True, True)

    res_label=Label(new, text="Results appear here:  " + showtext,  bg="yellow")
    res_label.grid(row=2, column=1, columnspan=3, pady=50)

    res_close_button = Button(new, text="Close", command=new.destroy)
    res_close_button.grid(row=4, column=3, pady=50)

    res_references = Button(new, text="References")
    res_references.grid(row=4, column=2, pady=50)

    res_more_button = Button(new, text="More")
    res_more_button.grid(row=4, column=1, pady=50)

    print("Show text in new window is:", showtext)

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


first_label = Label(root, text="Make entries:", font="Helvetica, 24", fg="blue")
first_label.grid(row=2, column=0)

combo_label = Label(root, text="Select topic:", fg="blue", font="Helvetica, 14")
combo_label.grid(row=0, column=4)

print_cbox_button = Button(root, text='Print dictionary', font="Helvetica, 24", fg="orange", relief='ridge', command=CreateDictionary)
print_cbox_button.grid(row=10, pady=50, column=1, columnspan=4)

result_button = Button(root, text="Print Dictionary and Show CHADS Result", font="Helvetica, 24", fg="red", command=show_result_in_label)
result_button.grid(row=14, pady=50, column=1, columnspan=4)

open_button = Button(root, text="Open new results window", font="Helvetica, 24", fg="green", command = open_new_window)
open_button.grid(row=18, column=1, columnspan=4, pady=50)

quit_button = Button(root, text="Exit", font="Helvetica, 24", fg="blue", command=quit)
quit_button.grid(row=22, pady=50, column=4)

# show_label_button = Button(root, text= "Show response text", font="Helvetica, 20", fg="blue", command=show_response_text)
# show_label_button.grid(row=14, column=0, columnspan=4)

# CHADS_button = Button(root, text="Calculate CHADS score", fg="red", font="Helvetica, 20", command=CHADS_VASc_score_dictionary_method(response_dict))
# CHADS_button.grid(row=20, pady=20, column=0, columnspan=4)



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

options = [
    "CHADS score",
    "CHADS-VASc score",
    "Post_code algorithm"
]

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.grid(row=0, column=5)







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
