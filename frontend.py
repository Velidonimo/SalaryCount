import tkinter as tk
import backend as be

root = tk.Tk()
active_entry = None

# Actions =============
def close():
    """
    Close the program
    """
    root.destroy()


def show_notification(notify):
    """
    Shows notification if can't connect to exchange rates server
                        or
                        if input data are wrong
    """
    if notify == 'ErrorURL':
        var_notify.set("Can't connect to 'openexchangerates.org'")
    else:
        var_notify.set('Wrong values!')


def lighten_entries():
    for entry in entries_dol:
        entry.config(bg='#fff')
    for entry in entries_rub:
        entry.config(bg='#fff')


def darken_entries(event):
    """
    Darken and cleaning unfocused cells
    """
    #first make all default
    lighten_entries()

    for i in range(len(entries_dol)):
        entry = entries_dol[i]
        var = vars_dol[i]
        if entry != entry.focus_get():
            entry.config(bg='#d4d4d4')
            var.set('')
        entry = entries_rub[i]
        var = vars_rub[i]
        if entry != entry.focus_get():
            entry.config(bg='#d4d4d4')
            var.set('')


def enable_entries():
    pass


def convert():
    """
    Sending the data to and retrieving back from backend
    """

    # deleting notifications
    var_notify.set('')

    # absorb values
    values_dol = list(map(lambda x: x.get(), vars_dol))
    values_rub = list(map(lambda x: x.get(), vars_rub))
    # send values
    values_to_set = be.convert_salary(values_dol, values_rub)

    # if error returned
    if isinstance(values_to_set, str):
        show_notification(values_to_set)
        return

    # fill the entries
    for i in range(len(values_to_set[0])):
        vars_dol[i].set(values_to_set[0][i])
        vars_rub[i].set(values_to_set[1][i])
# =====================


# Labels ==============
titles = 'Per', 'hour:', 'day:', 'week:', 'month:', 'year:'
column = 0
for i in range(6):
    lbl = tk.Label(root, text=titles[column], font=('Times', 20))
    lbl.grid(row=0, column=column)
    column += 1

lbl_dol = tk.Label(root, text='$', font=('Times', 20))
lbl_dol.grid(row=1, column=0)

lbl_rub = tk.Label(root, text='₽', font=('Times', 20))
lbl_rub.grid(row=2, column=0)

var_notify = tk.StringVar()
lbl_notify = tk.Label(root, textvariable=var_notify)
lbl_notify.grid(row=4, column=0, columnspan=2)
# =====================

# Entries =============
vars_dol = []
for i in range(5):
    vars_dol.append(tk.StringVar())

entries_dol = []
for i in range(5):
    entries_dol.append(tk.Entry(root, width=10, textvariable=vars_dol[i], font=('Times', 20)))
    entries_dol[i].grid(row=1, column=i+1)

vars_rub = []
for i in range(5):
    vars_rub.append(tk.StringVar())

entries_rub = []
for i in range(5):
    entries_rub.append(tk.Entry(root, width=10, textvariable=vars_rub[i], font=('Times', 20)))
    entries_rub[i].grid(row=2, column=i+1)

# binding entries
for entry in entries_dol:
    entry.bind('<Key>', darken_entries)
for entry in entries_rub:
    entry.bind('<Key>', darken_entries)
# =====================

# Buttons =============
btn_convert = tk.Button(root, text='Convert', font=('Times', 20), width=30, bg='#ababab', command=convert)
btn_convert.grid(row=3, column=2, columnspan=3)

btn_close = tk.Button(root, text='Close', font=('Times', 15), bg='#ababab', command=close)
btn_close.grid(row=4, column=5)
# =====================

root.mainloop()
