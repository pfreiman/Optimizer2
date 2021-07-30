"""make labels and entry boxes, enter values and make response_dict_numerical"""

import tkinter as tk

from Validate_entries import *

# response_list_numerical = []
# response_dict_numerical = {}

criteria_list_numerical_entries = [
    "Enter Age:", "Enter Hemoglobin:", "Enter QT interval:", "Enter Heart Rate:"
]

root = tk.Tk()
root.title("Data Entry Screen")
root.geometry('1000x1000')
root.resizable(True, True)


# Validation function
# def is_number(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False


# make labels for numerical entry boxes

def make_labels_numerical(question_list):
    rowcount = 0
    for name in question_list:
        lbl_name = tk.Label(root, text=name, font=("Arial", 16))
        lbl_name.grid(column=0, row=rowcount)
        rowcount += 1


make_labels_numerical(criteria_list_numerical_entries)


# make Entry boxes

def make_entry_boxes():
    global my_entries
    my_entries = []  # list of entrybox objects. Each individual box is called "entry"

    # Row loop
    for y in range(len(criteria_list_numerical_entries)):
        entry = tk.Entry(root, bd=4, fg="red", bg="aqua")
        entry.grid(row=y, column=1, pady=20, padx=5)
        my_entries.append(entry)
        print(my_entries)  # debug
    return my_entries


make_entry_boxes()


def get_responses():
    response_list = []  # list of user entries in order
    print("Entry list:", my_entries)

    for entries in my_entries:

        if not is_number(entries.get()):
            print("Entry is not a number.  ")
            lbl_show.config(text="Some entries are not numbers.  Re-enter values and try again")
            break
        response_list.append(float(entries.get()))
        lbl_show.config(text=response_list)

        print("Here is the response_list", response_list)

    return response_list


def create_dictionary_numerical_entries():
    question_list = criteria_list_numerical_entries
    response_list = get_responses()

    print("\n\nQuestion list;", question_list)
    print("\nFinal response list:", response_list)
    response_dict_numerical = dict(zip(question_list, response_list))

    """ needs code to validate entries and screen for values with empty strings"""

    print("\nResponse dictionary numerical:", response_dict_numerical)
    #  my_tools.result_text = "Selected responses:", my_tools.response_dict
    return response_dict_numerical


btn_click = tk.Button(root, text="Enter Selections:", font=("Arial", 16),
                      fg="magenta",
                      command=create_dictionary_numerical_entries)
btn_click.grid(row=6, column=0, pady=20)

lbl_show = tk.Label(root, text="")
lbl_show.grid(row=7, column=0, pady=20)

tk.mainloop()
