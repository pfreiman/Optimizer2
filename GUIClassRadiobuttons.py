""" Make an input screen of radiobuttons from a dictionary of questions(keys) and possible answers(selection options
provided as tuples), using HEART score as an example"""

import tkinter as tk

from CardiologyToolkit import CardiologyToolkit
my_tools = CardiologyToolkit()


class GUIRadiobuttons:

    def __init__(self):

        self.__heart_score_criteria = {
            'History': ('Slightly suspicious', 'Moderately suspicious', 'Highly suspicious'),
            'EKG': ('No changes', 'Non-specific repolarization abnormality', 'Significant ST deviation'),
            'Age': ('<45', '45-64', '>=65'),
            'Risk factors': ('None', '1-2 risk factors', '>=3 risk factors'),
            'Troponin': ('Normal', '1-3 x normal', '> 3 x normal')
        }

        self.__test_criteria_dictionary = {
            'Person': ('Washington', 'Jefferson', 'Adams', 'Franklin'),
            'Place': ('Virginia', 'Philadelphia', 'NY'),
            'Year': ('1776', '1793')

        }

        root = tk.Tk()
        root.title("Data Entry Screen")
        root.geometry('1200x1000')
        root.resizable(True, True)

        key_list = []
        response_list = []
        response_dict = {}

        alert_text = ""

        var0 = tk.StringVar()
        var1 = tk.StringVar()
        var2 = tk.StringVar()
        var3 = tk.StringVar()
        var4 = tk.StringVar()
        var5 = tk.StringVar()
        var6 = tk.StringVar()
        var7 = tk.StringVar()
        var8 = tk.StringVar()
        var9 = tk.StringVar()
        var10 = tk.StringVar()
        var11 = tk.StringVar()
        var12 = tk.StringVar()
        var13 = tk.StringVar()
        var14 = tk.StringVar()
        var15 = tk.StringVar()

        var_list = [var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14,
                    var15]


         # creates frame, labels and radiobutton choices from dictionary

        counter = 1  # counts number of rows of questions to make

        for question, options in self.__heart_score_criteria.items():  # sets up labels and builds key-list from initial dictionary

            #  for question, options in self.__test_criteria_dictionary.items():
            #  print("\n\n Current Question and choice options:", question, options)

            frame2 = tk.Frame(root, width=1200, height=100, bd=5, bg="aqua", relief="sunken")
            frame2.grid()

            label = tk.Label(frame2, text=question, font=("Arial", 16), fg="blue", bg="silver", pady=10)
            label.grid(row=counter, column=0)

            key_list.append(question)

            counter += 1

            """ make the radiobutton entry fields """
            """ set the variables used to store clicked values"""




        idx = 0  # sets index of columns(response options) to zero
        rowcount = 0  # counts the number of rows of response options to display

        for key, options in self.__heart_score_criteria.items():
        #  for key, options in self.__test_criteria_dictionary.items():
            var = var_list[rowcount]
            for item in options:

                new_buttons = tk.Radiobutton(root,
                                             text=item,
                                             font=("Arial, 16"), fg="red",
                                             padx=20, width=30,
                                             variable=var,
                                             indicatoron=0,
                                             #command=show_choice,
                                             value=item)
                new_buttons.grid(row=rowcount, column=idx+1)
                #  print("Current var is:", var)

                idx += 1
            idx = 0  # resets column counter to zero
            rowcount += 1


        def create_dictionary():   # creates the response dictionary from responses

            response_list = []

            for response in range(len(key_list)):
                response_list.append(var_list[response].get())

            print("\n\nKey list;", key_list)
            print("\nFinal response list:", response_list)
            response_dict = dict(zip(key_list, response_list))


            """ check the response list for empty strings.  Activate button only if all entries
                        are completed"""

            # print("Current RL:", response_list)
            #
            # for entry in response_list:
            #     print("checking response list...")
            #     print('Entry is;', entry)
            #     if entry == "":
            #         alert_text = "Complete all entries before building dictionary"
            #         print(alert_text)
            #     else:
            #         continue

            print("\nResponse dictionary:", response_dict)
            return response_dict


        button_dict = tk.Button(text="Create Dictionary", font="Arial, 32", fg="green", command=create_dictionary)
        button_dict.grid(row=16, columnspan=4, pady=30, sticky='S')

        alert_label = tk.Label(text="alert_text goes here")
        alert_label.grid(row=15, columnspan=4, sticky='S')

        tk.mainloop()

radiobutton_form = GUIRadiobuttons()
