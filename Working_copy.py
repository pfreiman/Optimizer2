from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Validate_entries import *
from CardiologyToolkit import CardiologyToolkit

my_tools = CardiologyToolkit()

root = Tk()

root.title("Data Entry Screen")
root.geometry('1600x1600')
root.resizable(True, True)

frm_checkboxes = LabelFrame(root, text="Select entries:", font=("Arial", 24), fg="red",
                            width=800, height=300, bd=5, bg="aqua", relief="sunken")
frm_radiobuttons = LabelFrame(root, text="Select entries:", font=("Arial", 24), fg="red",
                              width=800, height=300, bd=5, bg="aqua", relief="sunken")
frm_numerical_entry = LabelFrame(root, text="Select entries:", font=("Arial", 24), fg="red",
                                 width=800, height=300, bd=5, bg="aqua", relief="sunken")

""" First function creates the checkboxes in checkbox frame (frm_checkboxes)"""

checkboxes = {}


def create_checkboxes(criteria_list):
    Cbcolumn = 3
    Cbrow = 6

    for checkbox in range(len(criteria_list)):

        name = criteria_list[checkbox]
        current_var = IntVar()

        current_box = Checkbutton(frm_checkboxes, text=name, font="Arial,16", height=2, width=20, bg="aqua", fg="blue",
                                  variable=current_var)  # current_box is the checkbutton object
        current_box.var = current_var
        current_box.grid(row=Cbrow, column=Cbcolumn)
        checkboxes[
            current_box] = name  # makes checkbutton dictionary with checkbutton object as key and "name" string as value
        if Cbcolumn == 5:
            Cbcolumn = 3
            Cbrow += 1
        else:
            Cbcolumn += 1


def checkboxesclear():
    global checkboxes
    checkboxes = {}


""" Next function creates the dictionary of responses from checkboxes"""


def create_dictionary_checkboxes():
    kl = []  # key list
    vl = []  # value list

    for box in checkboxes:
        key = str(checkboxes[box])
        value = int(box.var.get())

        kl.append(key)
        vl.append(value)

        my_tools.response_dict_checkboxes = dict(zip(kl, vl))

    print("Dictionary of checkbox responses is:", my_tools.response_dict_checkboxes)  # debug
    my_tools.result_text = "Selected responses:", my_tools.response_dict_checkboxes
    return my_tools.response_dict_checkboxes


""" Section puts radiobuttons in radiobutton frame and builds response dictionary """

key_list = []
response_list = []
# response_dict_radiobuttons = {}

var_list = [StringVar() for i in range(0, 16)]

"""creates labels and radiobutton choices from question:choices dictionary"""


def create_radiobuttons(questions_dict):
    counter = 0  # counts row to display each question

    questions_dict = my_tools.get_current_questions_dict()

    for question in questions_dict:  # sets up labels and builds key_list from initial dictionary
        label_question = Label(frm_radiobuttons, text=question, font=("Arial", 20), fg="red", bg="white", height=2,
                               pady=10)
        label_question.grid(row=counter, column=0)
        key_list.append(question)

        counter += 1

    """ puts the radiobutton entry fields in radiobutton frame (frm_radiobuttons)"""

    idx = 0  # sets index of columns(response options) to zero
    rowcount = 0  # counts the number of rows of response options to display

    for key, choices in questions_dict.items():

        var = var_list[rowcount]
        for item in choices:
            new_buttons = Radiobutton(frm_radiobuttons,
                                      text=item,
                                      font=("Arial, 20"), fg="blue",
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


def create_dictionary_radiobuttons():  # creates the response dictionary from responses

    response_list = []

    for response in range(len(key_list)):
        response_list.append(var_list[response].get())

    print("\n\n rb Key list;", key_list)
    print("\nFinal rb response list:", response_list)
    my_tools.response_dict_radiobuttons = dict(zip(key_list, response_list))

    """ needs code to validate entries and screen for values with empty strings"""

    print("\nResponse dictionary from rb entries:", my_tools.response_dict_radiobuttons)
    my_tools.result_text = "Selected responses:", my_tools.response_dict_radiobuttons
    return my_tools.response_dict_radiobuttons


"""Next section makes entry boxes from a list of questions."""


# make labels for numerical entry boxes

def create_labels_numerical(question_list):
    rowcount = 0
    for name in question_list:
        lbl_name = Label(frm_numerical_entry, text=name, font=("Arial", 16))
        lbl_name.grid(column=0, row=rowcount)
        rowcount += 1


# create_labels_numerical()(my_tools.get_current_criteria_list())


# make Entry boxes

def create_entry_boxes_numerical():
    global my_entries
    my_entries = []  # list of entrybox objects. Each individual box is called "entry"

    # Row loop
    for y in range(len(my_tools.get_current_criteria_list())):
        entry = Entry(frm_numerical_entry, bd=4, fg="blue", bg='lemon chiffon')
        entry.grid(row=y, column=1, pady=20, padx=5)
        my_entries.append(entry)

    return my_entries


def get_responses_numerical():
    response_list_numerical = []  # list of user entries in order

    for entries in my_entries:

        # if not is_number(entries.get()):
        #     lbl_show.config(text="Some entries are not numbers.  Re-enter values and try again")
        #     break
        print("? is it a number?", is_number(entries.get()))

        if not is_number(entries.get()):
            messagebox.showinfo(title="Entry error", message="Some entries are not numbers.  "
                                                             "Re-enter values and try again.")
        response_list_numerical.append(float(entries.get()))
        # lbl_show.config(text=response_list_numerical)

    return response_list_numerical


response_dict_numerical = {}


def create_dictionary_numerical_entries():
    question_list = my_tools.get_current_criteria_list()
    response_list = get_responses_numerical()

    print("\n\nQuestion list numerical entries:", question_list)
    print("\nFinal response list numerical entries:", response_list)
    my_tools.response_dict_numerical = dict(zip(question_list, response_list))

    print("\nResponse dictionary numerical:", my_tools.response_dict_numerical)

    return my_tools.response_dict_numerical


# btn_click = Button(frm_numerical_entry, text="Enter Selections:", font=("Arial", 16),
#                    fg="magenta",
#                    command=create_dictionary_numerical_entries)
# btn_click.grid(row=6, column=0, pady=20)
#
# lbl_show = Label(frm_numerical_entry, text="")
# lbl_show.grid(row=7, column=0, pady=20)


def show_result_in_label():
    print("Selected combo item is:", my_tools.item)  # debug

    """ next section selects which frame(s) to display,
    creates and validates the response dictionaries"""

    if my_tools.item in my_tools.set_of_checkbox_questions:
        a = create_dictionary_checkboxes()
        validation_fails = validate_dictionary(a)
        if validation_fails:
            return

    if my_tools.item in my_tools.set_of_radiobutton_questions:
        b = create_dictionary_radiobuttons()
        validation_fails = validate_dictionary(b)
        if validation_fails:
            return

    if my_tools.item in my_tools.set_of_numerical_input_questions:
        c = create_dictionary_numerical_entries()
        validation_fails = validate_dictionary(c)
        if validation_fails:
            return

    my_tools.result_for_current_function = my_tools.get_result_for_current_function()  # returns result of current function

    lbl_result = Label(root, text="", font="Arial, 24", bg='lemon chiffon', fg='black',
                       wraplength=500, relief='sunken')
    lbl_result["text"] = my_tools.item + " is: \n\n " + str(my_tools.result_for_current_function) + "\n"
    lbl_result.grid(row=10, column=1, columnspan=2)

    btn_open_results_window.grid(row=18, column=1, columnspan=2, pady=50)


def combo_call_back_func(event):
    # This section prevents user from multiple topic choices for each program execution

    if my_tools.item != "":
        messagebox.showerror("Error", "May only run one query at at time.  Start over and enter new topic.")
        exit()

    if my_tools.item in my_tools.combobox_scores_options_list:
        my_tools.item = combo_scores_and_calculators.get()
    if my_tools.item in my_tools.combobox_clinical_scenarios_options_list:
        my_tools.item = combo_clinical_scenarios.get()
    print("Combo item is:", my_tools.item)

    checkboxesclear()

    create_checkboxes(my_tools.get_current_criteria_list())

    create_radiobuttons(my_tools.get_current_questions_dict())

    create_labels_numerical(my_tools.get_current_criteria_list())

    create_entry_boxes_numerical()

    """Next section displays the intro message for each selection."""

    if my_tools.item == "CHADS score":
        lbl_intro.config(text="The CHADS and CHADS-VASc scores are used to evaluate "
                              "the need for long-term anti-coagulation in atrial fibrillation")
    elif my_tools.item == "CHADS-VASc score":
        lbl_intro.config(text="The CHADS and CHADS-VASc scores are used to evaluate "
                              "the need for long-term anti-coagulation in atrial fibrillation")
    elif my_tools.item == "Post-code algorithm":
        lbl_intro.config(text="Post-code algorithm is used to assess the advisability of "
                              "immediate coronary angiography following cardiac arrest and resusitation.")
    elif my_tools.item == "HAS-BLED score":
        lbl_intro.config(text="The HAS-BLED score is used to assess the risk of bleeding from long-term"
                              "anticoagulation.  Used with the CHADS or CHADS-VASc score, it is used to "
                              "judge the risks vs. benefits of anticoagulation")
    elif my_tools.item == "HEART score":
        lbl_intro.config(text="The HEART score is used to evaluate the need for urgent hospitalization "
                              "in patients with acute chest pain.")
    elif my_tools.item == "Pre-op evaluation":
        lbl_intro.config(text="In patients with known or suspected coronary artery disease, "
                              "pre-op risk assessment is based on clinical and surgical factors")
    elif my_tools.item == "QTc interval":
        lbl_intro.config(text="The corrected QT interval (QTc) is useful in evaluating the EKG "
                              "and making decisions about specific therapies.")

    lbl_intro.grid(row=2, column=1, columnspan=2, pady=30)

    btn_enter_selections.grid(row=8, column=1, padx=10, pady=50, columnspan=2)

    """Next section chooses which frame to display"""

    if my_tools.item in my_tools.set_of_checkbox_questions:
        frm_checkboxes.grid(row=4, column=1, columnspan=2, padx=20, pady=30)
        # frm_radiobuttons.grid_forget()
    if my_tools.item in my_tools.set_of_radiobutton_questions:
        # frm_checkboxes.grid_forget()
        frm_radiobuttons.grid(row=5, column=1, columnspan=2, padx=20, pady=30)
    if my_tools.item in my_tools.set_of_numerical_input_questions:
        frm_numerical_entry.grid(row=6, column=1, columnspan=2, padx=20, pady=30)


def open_results_window():
    my_tools.result_for_current_function = my_tools.get_result_for_current_function()

    my_tools.showtext = str(my_tools.result_text) + "\n\n" + my_tools.item + " is:  \n\n" + str(
        my_tools.result_for_current_function)
    global win_results
    win_results = Toplevel(root)
    win_results.title("Results")
    win_results.geometry('1000x1000')
    win_results.resizable(True, True)

    lbl_brief_results = Label(win_results, text=my_tools.showtext, font=("Arial", 16),
                              wraplength=500, bg='lemon chiffon')
    lbl_brief_results.grid(row=2, column=1, columnspan=3, pady=50)

    lbl_long_results = Label(win_results, text="", wraplength=500, justify='left')
    lbl_long_results.grid(row=5, column=1, columnspan=3)

    btn_res_details_button = Button(win_results, text="Additional details", command=open_details_window)
    btn_res_details_button.grid(row=6, column=1, padx=10, pady=30)

    btn_res_references = Button(win_results, text="References")
    btn_res_references.grid(row=6, column=2, padx=10, pady=30)

    btn_res_close = Button(win_results, text="Close", command=win_results.destroy)
    btn_res_close.grid(row=6, column=3, padx=10, pady=30)

    lbl_long_results.config(text=my_tools.long_button_command())  # displays "display_long_text"  in long text label

    win_results.mainloop()


def open_details_window():
    win_details = Toplevel(win_results)
    win_details.title("Additional details")
    win_details.geometry('800x800')
    win_details.resizable(True, True)

    lbl_detailed_text = Label(win_details, text="<<detailed text goes here>>", font=("Arial", 16),
                              wraplength=500, bg='lemon chiffon', fg="black")
    lbl_detailed_text.grid(row=2, column=1, pady=50, padx=10)

    win_details.mainloop()


def new_command():
    pass


def cut_command():
    pass


def copy_command():
    pass


def paste_command():
    pass


def open_differential_diagnosis_frame():
    pass


lbl_checkbox = Label(frm_checkboxes, text="Choose all that apply:", font="Arial, 20", fg="blue")
lbl_checkbox.grid(row=0, column=0)

lbl_combo = Label(root, text="Scores and Calculators:", fg="blue", font="Arial, 24")
lbl_combo.grid(row=0, column=0, pady=10, padx=10)

lbl_combo_clinical_scenarios = Label(root, text="Clinical scenarios:", fg="blue", font="Arial, 24")
lbl_combo_clinical_scenarios.grid(row=0, column=2, pady=10, padx=10)

lbl_intro = Label(root, text="", font="Arial, 24", bg='lemon chiffon', fg='black',
                  wraplength=600, relief='sunken')

# make a combo box of the topics list:

combo_scores_and_calculators = ttk.Combobox(root, value=my_tools.combobox_scores_options_list, state="readonly")
combo_scores_and_calculators.current(0)
combo_scores_and_calculators.grid(row=1, column=0, padx=10, pady=10)
combo_scores_and_calculators.bind("<<ComboboxSelected>>", combo_call_back_func)

combo_clinical_scenarios = ttk.Combobox(root, value=my_tools.combobox_clinical_scenarios_options_list, state="readonly")
combo_clinical_scenarios.current(0)
combo_clinical_scenarios.grid(row=1, column=2, padx=10, pady=10)
combo_clinical_scenarios.bind("<<ComboboxSelected>>", combo_call_back_func)

btn_enter_selections = Button(root, text="Enter Selections", font="Arial, 24", fg="green", padx=20,
                              command=show_result_in_label)
btn_enter_selections.grid(row=8, column=1, padx=10, pady=50, columnspan=3)
btn_enter_selections.grid_forget()

btn_open_results_window = Button(root, text="Open Results Window", font="Arial, 24", fg="green",
                                 command=open_results_window)
btn_open_results_window.grid(row=18, column=1, columnspan=2, pady=50)
btn_open_results_window.grid_forget()

btn_quit = Button(root, text="Exit", font="Arial, 24", fg="green", command=quit)
# btn_quit.grid(row=22, pady=50, column=3)

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

diff_dx_menu = Menu(my_menu)
my_menu.add_cascade(label="Differential diagnoses", menu=diff_dx_menu)
diff_dx_menu.add_command(label="Open DDx window", command=open_differential_diagnosis_frame)

root.mainloop()


