from tkinter import *
from tkinter import ttk

from CardiologyToolkit import CardiologyToolkit

my_tools = CardiologyToolkit()

root = Tk()

root.title("Data Entry Screen")
root.geometry('1600x1600')
root.resizable(True, True)

upper_frame = Frame(root, width=800, height=300, bd=5, bg="aqua", relief="sunken")
lower_frame = Frame(root, width=800, height=300, bd=5, bg="grey", relief="sunken")

""" First function creates the checkboxes in upper frame"""

checkboxes = {}


def create_checkboxes(criteria_list):
    Cbcolumn = 3
    Cbrow = 6
    Chkcount = 0

    for Checkbox in range(len(criteria_list)):

        name = criteria_list[Checkbox]
        current_var = IntVar()
        current_box = Checkbutton(upper_frame, text=name, font="Arial,16", height=2, width=20, bg="aqua", fg="blue",
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


def checkboxesclear():
    global checkboxes
    checkboxes = {}


""" Next function creates the dictionary of responses from checkboxes"""


def create_dictionary_checkboxes():
    kl = []  # key list
    vl = []  # value list

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
    my_tools.result_text = "Selected responses:", my_tools.response_dict
    return my_tools.response_dict


""" Section puts radiobutttons in lower frame and builds response dictionary """

key_list = []
response_list = []
response_dict = {}

var_list = [StringVar() for i in range(0, 16)]

"""creates frame, labels and radiobutton choices from question:choices dictionary"""


def create_radiobuttons(questions_dict):
    counter = 0  # counts row to display each question

    questions_dict = my_tools.heart_score_criteria

    for question in questions_dict:  # sets up labels and builds key_list from initial dictionary
        label_question = Label(lower_frame, text=question, font=("Arial", 20), fg="blue", bg="silver", height=2,
                               pady=10)
        label_question.grid(row=counter, column=0)
        key_list.append(question)

        counter += 1

    """ make the radiobutton entry fields and place in lower frame """

    idx = 0  # sets index of columns(response options) to zero
    rowcount = 0  # counts the number of rows of response options to display

    for key, choices in questions_dict.items():

        var = var_list[rowcount]
        for item in choices:
            new_buttons = Radiobutton(lower_frame,
                                      text=item,
                                      font=("Arial, 20"), fg="red",
                                      bd=8,
                                      selectcolor="blue",
                                      padx=20, width=24, height=4,
                                      variable=var,
                                      indicatoron=0,
                                      value=item)
            new_buttons.grid(row=rowcount, column=idx + 1)

            idx += 1
        idx = 0  # resets column counter to zero
        rowcount += 1


# create_radiobuttons()

def create_dictionary_radiobuttons():  # creates the response dictionary from responses

    response_list = []

    for response in range(len(key_list)):
        response_list.append(var_list[response].get())

    print("\n\nKey list;", key_list)
    print("\nFinal response list:", response_list)
    my_tools.response_dict = dict(zip(key_list, response_list))

    """ needs code to validate entries and screen for values with empty strings"""

    print("\nResponse dictionary:", my_tools.response_dict)
    my_tools.result_text = "Selected responses:", my_tools.response_dict
    return my_tools.response_dict


def show_result_in_label():
    print("Selected combo item is:", my_tools.item)

    """ next section selects which frame(s) to display"""

    if my_tools.item in my_tools.set_of_checkbox_questions:
        a = create_dictionary_checkboxes()
    if my_tools.item in my_tools.set_of_radiobutton_questions:
        b = create_dictionary_radiobuttons()
    if my_tools.item in my_tools.set_of_numerical_input_questions:
        pass

    my_tools.result_for_current_function = my_tools.get_result_for_current_function()  # returns the result of current function

    result_label = Label(root, text=my_tools.result_text, font="helvetica, 12", bg='gray', fg='yellow',
                         relief='sunken')
    result_label.config(
        text=str(my_tools.result_text) + "\n\n" + my_tools.item + " is: \n\n" + str(
            my_tools.result_for_current_function))
    result_label.grid(row=10, column=1, columnspan=3)


def combo_call_back_func(event):
    my_tools.item = my_combo.get()
    print("Combo item is:", my_tools.item)

    checkboxesclear()

    create_checkboxes(my_tools.get_current_criteria_list())

    create_radiobuttons(my_tools.heart_score_criteria)

    """Next section chooses which frame to display"""

    if my_tools.item in my_tools.set_of_radiobutton_questions:
        upper_frame.grid_forget()
        lower_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=30)
    elif my_tools.item in my_tools.set_of_checkbox_questions:
        lower_frame.grid_forget()
        upper_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=30)


def open_new_window():
    my_tools.result_for_current_function = my_tools.get_result_for_current_function()

    my_tools.showtext = str(my_tools.result_text) + "\n\n" + my_tools.item + " is:  \n\n" + str(
        my_tools.result_for_current_function)

    new = Toplevel()
    new.title("Results")
    new.geometry('800x800')
    new.resizable(True, True)

    res_label = Label(new, text=my_tools.showtext, font=("Helvetica", 16),
                      wraplength=500, bg="aqua")
    res_label.grid(row=2, column=1, columnspan=3, pady=50)

    res_more_label = Label(new, text="", wraplength=500, justify='left')
    res_more_label.grid(row=5, column=1, columnspan=3)

    res_close_button = Button(new, text="Close", command=new.destroy)
    res_close_button.grid(row=4, column=3, pady=50)

    res_references = Button(new, text="References")
    res_references.grid(row=4, column=2, pady=50)

    res_more_button = Button(new, text="More", command=my_tools.more_button_command)
    res_more_button.grid(row=4, column=1, pady=50)

    res_more_label.config(text=my_tools.more_button_command())

    print("Show text in new window is:", my_tools.showtext)
    new.mainloop()


def new_command():
    pass


def cut_command():
    pass


def copy_command():
    pass


def paste_command():
    pass


checkbox_label = Label(upper_frame, text="Make entries:", font="Helvetica, 20", fg="blue")
checkbox_label.grid(row=0, column=0)

combo_label = Label(root, text="Select topic:", fg="blue", font="Helvetica, 24")
combo_label.grid(row=0, column=2, pady=10, padx=10)

# make a combo box of the topics list:

my_combo = ttk.Combobox(root, value=my_tools.combobox_options_list, state="readonly")
my_combo.current(0)
my_combo.grid(row=0, column=3, padx=10, pady=10)
my_combo.bind("<<ComboboxSelected>>", combo_call_back_func)

# intro_label = Label(root, text="<<Intro text will go here>>", font="Arial, 24", bg='gray', fg='yellow',
#                          relief='sunken')
# intro_label.grid(row=6, column=1, columnspan=3)

# result_button_checkboxes = Button(root, text="Enter Checkboxes Selections", font="Arial, 24", fg="red", padx=20,
#                        command=show_result_in_label)
# result_button_checkboxes.grid(row=8, column=1, padx=10, pady=50, columnspan=1)

result_button_radiobuttons = Button(text="Enter Selections", font="Arial, 24", fg="green", padx=20,
                                    command=show_result_in_label)
result_button_radiobuttons.grid(row=8, column=1, padx=10, pady=50, columnspan=3)

open_button = Button(root, text="Open new Results window", font="Helvetica, 24", fg="green",
                     command=open_new_window)
open_button.grid(row=18, column=1, columnspan=3, pady=50)

quit_button = Button(root, text="Exit", font="Helvetica, 24", fg="blue", command=quit)
quit_button.grid(row=22, pady=50, column=3)

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

root.mainloop()

""" Also probably needs some way to reset the global checkboxes dictionary if this function is run more than once.

"""
