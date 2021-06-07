""" takes a list of fields and produces a gui with field labels and entry boxes.  Then retrieves entries
 in the boxes and builds a dictionary"""


import tkinter as tk

import Criteria_list_constants

fields = 'Last Name', 'First Name', 'Job', 'Country'   # tuple
fields = Criteria_list_constants.cl_CHADS_VASc  # example where we pull in list from a saved list of constants
resp_dict = {}

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


def fetch(entries):
    text_list = []

    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print(text)
        #  print(type(text))
        text_list.append(text)
        print('%s: "%s"' % (field, text))
    print(text_list)
    resp_dict = dict(zip(fields, text_list))
    display_label.config(text="Response dictionary is:\n\n" + str(resp_dict))
    print("Dictionary of responses:", resp_dict)
    return resp_dict


if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Show dictionary',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    print(resp_dict)

    display_label = tk.Label(root, text= "", bg="aqua", fg="blue")
    display_label.pack(side = tk.BOTTOM, padx = 5, pady=10)


    root.mainloop()

