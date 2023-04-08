from tkinter import *


def calculate_kilometer():
    mile_value = float(input.get())
    converted_value = mile_value * 1.609
    label_kilometer.config(text=f"{converted_value}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10, text="Enter the Miles to be converted")
input.focus()
input.grid(column=1, row=0)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal_text = Label(text="Is Equal to")
label_equal_text.grid(column=0, row=1)

label_kilometer = Label()
label_kilometer.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_kilometer)
calculate_button.grid(column=1, row=3)

window.mainloop()
