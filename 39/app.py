from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles To KM Converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

converted_label = Label(text="Is Equal To")
converted_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calc_btn = Button(text="Calculate", command=miles_to_km)
calc_btn.grid(column=1, row=2)


window.mainloop()
