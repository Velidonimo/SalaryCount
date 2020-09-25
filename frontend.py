import tkinter as tk
import backend as be

root = tk.Tk()


# Actions =============
def close():
    root.destroy()
# =====================


# Labels ==============
lbl_per = tk.Label(root, text='Per', font=('Times', 20))
lbl_per.grid(row=0, column=0)

lbl_hour = tk.Label(root, text='hour:', font=('Times', 20))
lbl_hour.grid(row=0, column=1)

lbl_day = tk.Label(root, text='day:', font=('Times', 20))
lbl_day.grid(row=0, column=2)

lbl_week = tk.Label(root, text='week:', font=('Times', 20))
lbl_week.grid(row=0, column=3)

lbl_mo = tk.Label(root, text='month:', font=('Times', 20))
lbl_mo.grid(row=0, column=4)

lbl_year = tk.Label(root, text='year:', font=('Times', 20))
lbl_year.grid(row=0, column=5)

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
