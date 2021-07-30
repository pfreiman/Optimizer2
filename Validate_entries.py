""" code to validate entries """
from tkinter import messagebox
from CardiologyToolkit import CardiologyToolkit
my_tools = CardiologyToolkit()


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


""" code to validate numerical entries"""

my_entries = [4, 6, 7]
my_entries2 = ['abc', 'def', 'ghi']


def validate_numerical_entries(my_entries):
    for entries in my_entries:
        if not is_number(entries):
            print("At least one entry is not a number.")
        return


# validate_numerical_entries(my_entries2)


""" validate dictionary entries and screen for values with empty strings"""

sample_dictionary = {'First': 1, 'Second': "", 'Third': (3, 4, 5), 'Fourth': "test string"}
sample_dictionary2 = {}


def validate_dictionary(dict):  # invalidates entry if dictionary empty or values missing
    error_value = False
    error_dict = False
    if dict == {}:  # checks for empty dictionary
        print("Error.  At least one key entry is missing")
        messagebox.showerror(message="At least one key entry is missing.")
    for v in dict.values():  # checks for missing values
        if v == "" or None:
            error_value = True
            print("Error.  At least one value entry is missing.")
            messagebox.showerror(message="At least one value entry is missing.")
    if dict == {} or error_value == True:
        error_dict = True
    return error_dict

# validate_dictionary(sample_dictionary2)

def validate_multiple_topics(clicked_entry):
    print("my tools.item is:", my_tools.item)
    if clicked_entry != "":
        messagebox.showerror("Error", "May only run one query at at time.  Start over and enter new topic.")
        exit()
