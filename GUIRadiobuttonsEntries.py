""" Make an input screen of radiobuttons from a dictionary of questions and possible answers,
    using HEART score as an example"""

import tkinter as tk


class GUIShell:

    def __init__(self):

        self.__heart_score_criteria = {
            'History': ('Slightly suspicious', 'Moderately suspicious', 'Highly suspicious'),
            'EKG': ('No changes', 'Non-specific repolarization abnormality', 'Significant ST deviation'),
            'Age': ('<45', '45-64', '>=65'),
            'Risk factors': ('None', '1-2 risk factors', '>=3 risk factors'),
            'Troponin': ('Normal', '1-3 x normal', '> 3x normal')
        }

        root = tk.Tk()
        root.title("Data Entry Screen")
        root.geometry('1000x1000')
        root.resizable(True, True)



        # var = tk.StringVar()


        def show_choice():   # function to get value of checked radiobutton

            print("here is the value stored in var:", var.get())
            print(" debug---- WHY WON''T THIS PRINT THE VALUE OF VAR????")
            print("Program says current var is:", var)


         # creates frames, labels and radiobutton choices from dictionary

        #  def create_radiobuttons(self):

        counter = 0  # counts number of questions/frames to make
        frame = "frame"

        for question, options in self.__heart_score_criteria.items():  # gets frames and labels from initial dictionary
            print("\n\n Current Question and choice options:", question, options)
            frame_name = (frame + str(counter))
            print("\n Current frame:", frame_name)

            frame_name = tk.Frame(root, width=800, height=100, bd=5, bg="aqua", relief="sunken")
            frame_name.grid(row=counter)
            counter += 1

            label = tk.Label(frame_name, text=question, font=("Arial", 16), fg="blue", bg="silver", pady=10)
            label.grid(row=0, sticky="W")

            """ make the radiobutton entry fields for each frame"""
            """ this is a nested loop to create the radiobuttons"""

            # var1 = tk.StringVar()
            # var2 = tk.StringVar()
            # var3 = tk.StringVar()
            # var4 = tk.StringVar()
            # var5 = tk.StringVar()
            #
            # temp = [var1, var2, var3, var4, var5]  # list of temp var variables to use for radiobuttons



            idx = 0  # sets index of columns(response options) to zero
            #
            # var = temp[idx]  # sets var to current iteration

            var = tk.StringVar()

            print("\n\n current var is:", var)  # debug

            for item in options:

                new_buttons = tk.Radiobutton(frame_name,
                                             text=item,
                                             font=("Arial, 16"), fg="red",
                                             padx=20, width=30,
                                             variable=var,
                                             indicatoron=0,
                                             command=show_choice,
                                             value=item)
                new_buttons.grid(row=1, column=idx)


                idx += 1

        tk.mainloop()

GUIShell()
