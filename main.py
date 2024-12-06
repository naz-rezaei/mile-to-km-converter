from tkinter import *

def calculate():
    try:
        mile = float(entry.get())
        result = round(mile * 1.609344, 2) 
        result_label.config(text=str(result), fg="#4CAF50")
    except ValueError:
        result_label.config(text="Invalid input", fg="red") 

window = Tk()
window.minsize(600, 400)
window.config(padx=40, pady=40, bg="#f5f5f5")
window.title("Mile to Kilometer Converter")


title_label = Label(window, text="Mile to Kilometer Converter", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
title_label.grid(row=0, column=0, columnspan=3, pady=20)


mile_label = Label(window, text="Miles", font=("Arial", 12, "bold"), bg="#f5f5f5")
mile_label.grid(row=1, column=2)

equal_label = Label(window, text="is equal to", font=("Arial", 12, "bold"), bg="#f5f5f5")
equal_label.grid(row=2, column=0)

km_label = Label(window, text="Km", font=("Arial", 12, "bold"), bg="#f5f5f5")
km_label.grid(row=2, column=2)


entry = Entry(window, width=20, font=("Arial", 12), bd=2, relief="solid")
entry.grid(row=1, column=1, pady=20)
entry.focus()


result_label = Label(window, text="0", font=("Arial", 12, "bold"), bg="#f5f5f5")
result_label.grid(row=2, column=1)


my_button = Button(window, text="Calculate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=2, command=calculate)
my_button.grid(row=3, column=1, pady=20)

window.mainloop()
