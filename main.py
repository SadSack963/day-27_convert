import tkinter as tk


def mile_km():
    mile = float(mile_entry.get())
    result_text.config(text=str(round(mile * 1.60934, ndigits=3)))


master = tk.Tk()
master.title("Convert Miles to Kilometers")
master.minsize(width=200, height=100)
master.config(padx=30, pady=30)

mile_entry = tk.Entry(master, width=15, justify="center")
mile_entry.insert(tk.END, string="0")
mile_entry.focus()
mile_entry.grid(row=0, column=1)

mile_unit = tk.Label(master, text="Miles")
mile_unit.grid(row=0, column=2)

equals = tk.Label(master, text="is equal to")
equals.grid(row=1, column=0)

result_text = tk.Label(master, text="0", justify="center")
result_text.grid(row=1, column=1)

km_unit = tk.Label(master, text="Km")
km_unit.grid(row=1, column=2)

calc_button = tk.Button(master, text="Calculate", command=mile_km)
calc_button.grid(row=2, column=1)


master.mainloop()
