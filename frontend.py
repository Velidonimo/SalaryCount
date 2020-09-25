import tkinter as tk
import backend as be

root = tk.Tk()


# Actions =============
def close():
    root.destroy()
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
oops = 'Oops, wrong index'
vars_dol = [oops]
for i in range(1, 6):
    vars_dol.append(tk.StringVar())

entries_dol = [oops]
for i in range(1, 6):
    entries_dol.append(tk.Entry(root, width=10, textvariable=vars_dol[i], font=('Times', 20)))
    entries_dol[i].grid(row=1, column=i)

vars_rub = [oops]
for i in range(1, 6):
    vars_rub.append(tk.StringVar())

entries_rub = [oops]
for i in range(1, 6):
    entries_rub.append(tk.Entry(root, width=10, textvariable=vars_rub[i], font=('Times', 20)))
    entries_rub[i].grid(row=2, column=i)
# =====================

# Buttons =============
btn_convert = tk.Button(root, text='Convert', font=('Times', 20), width=30, bg='#ababab')
btn_convert.grid(row=3, column=2, columnspan=3)

btn_close = tk.Button(root, text='Close', font=('Times', 15), bg='#ababab', command=close)
btn_close.grid(row=4, column=5)
# =====================

root.mainloop()
