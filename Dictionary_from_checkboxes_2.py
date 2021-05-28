from tkinter import *

root = Tk()

root.title("CHADS VASc Entry Screen")
root.geometry('800x800')
root.resizable(True, True)

criteria_list = ['CHF', 'HTN', 'AGE', 'Diabetes', 'Stroke_hx']
#  criteria_list = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo','Foxtrot']
#  criteria_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print("Criteria list:", criteria_list)

checkboxes = {}
response_dict = {}
result_text = ""

""" First function puts the checkboxes on the GUI screen"""


def CreateCheckBoxes(criteria_list):
    Cbcolumn = 3
    Cbrow = 2
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
    result_label = Label(root, text=result_text, font="helvetica, 20", bg='green', fg='yellow', height=5,
                         relief='sunken')
    result_label.config(text=str(result_text) + "\n\n CHADS score is:  " + str(CHADS_VASc_score_dictionary_method(response_dict)))
    result_label.grid(row=16, pady=20, column=0, columnspan=4)
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


first_label = Label(root, text="Make entries:", font="Helvetica, 20", fg="blue")
first_label.grid(row=0, column=0)

print_cbox_button = Button(root, text='Print dictionary', height=5, width=20, fg="magenta", relief='ridge', command=CreateDictionary)
print_cbox_button.grid(row=10, pady=20, column=0, columnspan=4)

quit_button = Button(root, text="Exit", font="Helvetica, 20", fg="blue", command=quit)
quit_button.grid(row=18, pady=20, column=0, columnspan=4)

result_button = Button(root, text="Print Dictionary and Show CHADS Result", font="Helvetica, 20", fg="blue", command=show_result_in_label)
result_button.grid(row=17, pady=20, column=0, columnspan=4)

# show_label_button = Button(root, text= "Show response text", font="Helvetica, 20", fg="blue", command=show_response_text)
# show_label_button.grid(row=14, column=0, columnspan=4)

# CHADS_button = Button(root, text="Calculate CHADS score", fg="red", font="Helvetica, 20", command=CHADS_VASc_score_dictionary_method(response_dict))
# CHADS_button.grid(row=20, pady=20, column=0, columnspan=4)


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
