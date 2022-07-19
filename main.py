from tkinter import Tk, Text, Label

tk = Tk()

tk.geometry("1000x400")

text_window = Text(tk, height=8, width=100)
text_label = Label(tk, text="Don't stop.")

text_label.config(font=("Courier", 14))

text_label.pack()
text_window.pack()

tk.mainloop()
