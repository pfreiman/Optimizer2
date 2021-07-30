import tkinter as tk

from CardiologyToolkit import CardiologyToolkit

useful_tools = CardiologyToolkit()

root = tk.Tk()
root.title("Radio Button Entries")
root.geometry("500x800")


CHADS_list = ['CHF', 'HTN', 'AGE > 75', 'Diabetes', 'Stroke_hx']
post_code_list = ['Unwitnessed', 'Ongoing CPR', 'ROSC_> 30 minutes', 'pH < 7.2', 'Non-cardiac cause',
                  'Initial rhythm non-VF', 'lactate > 7', 'No bystander COR', 'Age > 85', 'ESRD']


top_label = tk.Label(text="Choose a diagnosis:")
top_label.pack(pady=10)

v1 = tk.StringVar()
v1.set(CHADS_list[0])
v2 = tk.StringVar()
v2.set(post_code_list[0])

def get_entries():
    print(v1.get())
    print(v2.get())

def ShowChoice():
    print(v1.get())

def ShowChoice2():
        print(v2.get())

chosen_list = CHADS_list
print(chosen_list)

for item in chosen_list:

    tk.Radiobutton(root,
       text=item,
       padx = 20,
       variable=v1,
       command=ShowChoice,
       indicatoron=0,
       value=item).pack(anchor=tk.W)

second_label = tk.Label(text="\n\nEnter one criterion:")
second_label.pack(pady= 20)

chosen_list = useful_tools.get_list()
print(chosen_list)

for item in chosen_list:

    tk.Radiobutton(root,
        text=item,
        padx = 20,
        variable=v2,
        command=ShowChoice2,
        indicatoron=0,
        value=item).pack(anchor=tk.W)


""" to place buttons horizontally, use:

buttons = []
vars = []
for idx, (text, mode) in enumerate(AANTAL):  # (AANTAL is list of tuples: text/value pairs. [(1, "1"), (2, "2")....etc.)
    vars.append(StringVar(value="1"))
    buttons.append(Radiobutton(Main,padx=20, pady=10,font=('arial', 20, "bold"), bd=4, text=text, variable=vars[-1], value=mode, indicatoron=0))
    buttons[-1].grid(row=0, column=idx) 
    
    """









#  Group 1
# s1r1=tk.Radiobutton(root,text="Red", variable=v1, value=4)
# s1r2=tk.Radiobutton(root,text="Green", variable=v1, value=2)
# s1r3=tk.Radiobutton(root,text="Blue", variable=v1, value=3)
# # Group 2
# s2r1=tk.Radiobutton(root,text="1", variable=v2, value="start")
# s2r2=tk.Radiobutton(root,text="2", variable=v2, value="middle")
# s2r3=tk.Radiobutton(root,text="3", variable=v2, value="end")
#
# s1r1.pack()
# s1r2.pack()
# s1r3.pack()
#
# s2r1.pack()
# s2r2.pack()
# s2r3.pack()
#
# get_button = tk.Button(root, text="get entries", command=get_entries).pack()
#
# dict = {}
# tuple = (v1.get()["text"], v1.get())
# print(tuple)


#
#



#
# v = tk.IntVar()
# v.set(1)

#
# languages = [("Python", 101),
#    	     ("Perl", 102),
#     	     ("Java", 103),
#              ("C++", 104),
#              ("C", 105)]
#
# def ShowChoice():
#     print(v.get())
#
# tk.Label(root,
#          text="""Choose your favourite
# programming language:""",
#          justify = tk.LEFT,
#          padx = 20).pack()
#
# for language, val in languages:
#     tk.Radiobutton(root,
#                    text=language,
#                    padx = 20,
#                    variable=v,
#                    command=ShowChoice,
#                    value=val).pack(anchor=tk.W)

# tk.Label(root,
#         text="""Choose a
# programming language:""",
#         justify = tk.LEFT,
#         padx = 20).pack()
#
# tk.Radiobutton(root,
#                text="Python",
#                padx = 20,
#                variable=v,
#                value=1,
#                indicatoron=0).pack(anchor=tk.W)
#
# tk.Radiobutton(root,
#                text="Perl",
#                padx = 20,
#                variable=v,
#                value=2).pack(anchor=tk.W)
#
# tk.Radiobutton(root,
#                text="C#",
#                padx = 20,
#                variable=v,
#                value=3).pack(anchor=tk.W)


root.mainloop()