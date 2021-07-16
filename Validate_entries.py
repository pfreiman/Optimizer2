import tkinter as tk

root = tk.Tk()

root.title("Data Entry Screen")
root.geometry('1400x1400')
root.resizable(True, True)

error_message = "Not a valid entry.  Enter a number."


def validate_entry():
    print(my_entry.get())
    my_input = my_entry.get()
    print(my_input)
    print(type(my_input))
    try:
        my_input = float(my_input)
        my_label.config(text="Valid entry")
    except:
        print("input is not a well-formed number")
        my_label.config(text="Not a valid entry.  Enter a number.")


my_entry = tk.Entry(root)
my_entry.pack()

my_button = tk.Button(root, text='Validate', command=validate_entry)
my_button.pack()

my_label = tk.Label(root, text=error_message)
my_label.pack()

my_input = my_entry.get()

tk.mainloop()