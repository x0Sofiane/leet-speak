from test import *
from tkinter import *

dic = importDic('Niveau test.csv')

#############
# interface #
#############

window = Tk()
window.title("Convertisseur Leet Speak")
window.configure(bg='#9AA7B2')
window.columnconfigure(0, minsize=30)
window.rowconfigure(0, minsize=60)
window.columnconfigure(4, minsize=30)
window.rowconfigure(2, minsize=30)

top = Frame(window, bg='#9AA7B2')
titre = Label(top, text="Convertisseur Leet Speak", bg='#9AA7B2', font=("Helvetica", 20, 'bold'), fg='#5271FF')
top.grid(column=0, row=0, columnspan=5)
titre.pack()

left = Frame(window, bd=10, bg='#C7D0D8')
val = StringVar()
t1 = Label(left, text="Texte", bg='#C7D0D8', fg='#00C2CB', font=('Arial', 14, 'bold'))
e1 = Text(left, height=10, width=30)

left.grid(column=1, row = 1)
t1.pack()
e1.pack()

right = Frame(window, bd=10, bg='#C7D0D8')
t2 = Label(right, text="Traduction", bg='#C7D0D8', fg='#00C2CB', font=('Arial', 14, 'bold'))
e2 = Text(right, height=10, width=30)

right.grid(column=3, row = 1)
t2.pack()
e2.pack()

def trad(j): # Fonction de récupération du texte + conversion + affichage
   a = e1.get("1.0", "end-1c")
   if j == 1:
      a = leetToHuman(a, dic)
   else:
      a = humanToLeet(a, dic)
   e2.delete(1.0,"end")
   e2.insert(1.0, a)

middle = Frame(window, bd=10, bg='#C7D0D8', pady=70)
b1 = Button(middle, text='Convertir en langage normal', command= lambda:trad(1))
b2 = Button(middle, text='Convertir en Leet Speak', command= lambda:trad(2))
middle.grid(column=2, row=1)
b1.pack()
b2.pack()

window.mainloop()