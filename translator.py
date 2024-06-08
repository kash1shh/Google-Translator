from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Source_txt.get(1.0, END).strip()
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='Blue')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="Blue")
lab_txt.place(x=100, y=20, height=50, width=300)

lab_src_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="White", bg="Blue")
lab_src_txt.place(x=100, y=80, height=20, width=300)

Source_txt = Text(root, font=("Times New Roman", 14), wrap=WORD, highlightthickness=2, highlightbackground="black", highlightcolor="black")
Source_txt.place(x=10, y=110, height=100, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text, font=("Times New Roman", 12))
comb_sor.place(x=10, y=230, height=40, width=150)
comb_sor.set("English")

button_change = Button(root, text="Translate", relief=RAISED, font=("Times New Roman", 14, "bold"), bg="white", fg="black", command=data)
button_change.place(x=170, y=230, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text, font=("Times New Roman", 12))
comb_dest.place(x=330, y=230, height=40, width=150)
comb_dest.set("Hindi")

lab_dest_txt = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="White", bg="Blue")
lab_dest_txt.place(x=100, y=300, height=20, width=300)

dest_txt = Text(root, font=("Times New Roman", 14), wrap=WORD, highlightthickness=2, highlightbackground="black", highlightcolor="black")
dest_txt.place(x=10, y=330, height=100, width=480)

root.mainloop()
