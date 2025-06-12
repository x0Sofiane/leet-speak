from fonctions import *
from tkinter import *

#############
# interface #
#############

# Création de la fenetre

window = Tk()
window.title("Convertisseur Leet Speak")
window.configure(bg='#4A4847')
window.columnconfigure(0, minsize=30)
window.rowconfigure(0, minsize=60)
window.columnconfigure(4, minsize=30)
window.rowconfigure(2, minsize=30)

# Zone du titre

top = Frame(window, bg='#4A4847')
titre = Label(top, text="Convertisseur Leet Speak", bg='#4B4948', font=("LeetSpeak", 20, 'italic', 'bold'), fg='#FFFFFF')
top.grid(column=0, row=0, columnspan=5)
titre.pack()

# Menu latéral

def trad(j): # Fonction de récupération du texte + conversion + affichage
   a = e1.get("1.0", "end-1c")
   if j == 1:
      a = leetToHuman(a, dic)
   else:
      a = humanToLeet(a, dic)
   e2.delete(1.0,"end")
   e2.insert(1.0, a)

dic = importDic("Niveau 1.csv")
def select(niv):
   global dic
   dic = importDic("Niveau " + str(niv) + ".csv")

left = Frame(window, bd=10, bg='#4A4847', pady=60)
left.grid(column=1, row=1)

t = Label(left, text="Sélection du niveau", bg="#4A4847", font=('Arial',9, 'bold', 'italic'), fg = '#FFFFFF')
value = StringVar()
value.set(1)
bouton1 = Radiobutton(left, text="Niveau 1", variable=value, value=1, bg="#4A4847", fg="white", activebackground="#4A4847", selectcolor = "#4A4847", activeforeground = "white", cursor = "hand2")
bouton2 = Radiobutton(left, text="Niveau 2", variable=value, value=2, bg="#4A4847", fg="white", activebackground="#4A4847", selectcolor = "#4A4847", activeforeground = "white", cursor = "hand2")
c = Button(left, text="Valider", command= lambda:select(value.get()), fg='black', cursor = "hand2")
t.pack()
bouton1.pack()
bouton2.pack()
c.pack()

b1 = Button(left, text='Convertir en langage normal', command= lambda:trad(1), cursor = "hand2")
b2 = Button(left, text='Convertir en Leet Speak', command= lambda:trad(2), cursor = "hand2")
t1 = Label(left, text="Traduire", bg="#4A4847", font=('Arial',9, 'bold', 'italic'), fg = '#FFFFFF')
t1.pack()
b1.pack()
b2.pack()

# Zone du texte à convertir

middle = Frame(window, bd=10, bg='#41403E')
val = StringVar()
t1 = Label(middle, text="Texte", bg='#41403E', fg='#FFFFFF', font=('Helvetica', 14, 'bold'))
e1 = Text(middle, height=10, width=30)

middle.grid(column=2, row = 1)
t1.pack()
e1.pack()

# Zone du texte traduit

right = Frame(window, bd=10, bg='#41403E')
t2 = Label(right, text="Traduction", bg='#41403E', fg='#FFFFFF', font=('Helvetica', 14, 'bold'))
e2 = Text(right, height=10, width=30)

right.grid(column=3, row = 1)
t2.pack()
e2.pack()

window.mainloop()