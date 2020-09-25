import tkinter as tk
import backend as be

root = tk.Tk()


# Actions =============
def close():
    """
    Close the program
    """
    root.destroy()


def error_connection():
    """
    Shows notification if can't connect to exchange rates server
    """
    print('URL error')


def wrong_data():
    """
    Shows notification if input data are wrong
    """
    print('Wrong data')


def convert():
    """
    Sending the data to and retrieving back from backend
    """

    # absorb values
    values_dol = list(map(lambda x: x.get(), vars_dol))
    values_rub = list(map(lambda x: x.get(), vars_rub))
    # send values
    values_to_set = be.convert_salary(values_dol, values_rub)

    # check incoming data
    if values_to_set == 'ErrorURL':
        error_connection()
        return
    elif values_to_set == 'ErrorIncome':
        wrong_data()
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
# =====================

# Buttons =============
btn_convert = tk.Button(root, text='Convert', font=('Times', 20), width=30, bg='#ababab', command=convert)
btn_convert.grid(row=3, column=2, columnspan=3)

btn_close = tk.Button(root, text='Close', font=('Times', 15), bg='#ababab', command=close)
btn_close.grid(row=4, column=5)
# =====================

root.mainloop()
