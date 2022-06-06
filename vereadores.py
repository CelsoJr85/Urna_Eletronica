from tkinter import *



menu_vereadores = Tk()
menu_vereadores.title("URNA ELETRÔNICA")
menu_vereadores.geometry("500x300")

# Textos / Labels
label_titulo = Label(menu_vereadores,
                     text="Eleição - 2022",
                     font="Time 15",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=CENTER)

label_1 = Label(menu_vereadores,
                text="Você votou em: ",
                font="Arial 10",
                fg="#000000",
                width=20,
                height=2,
                anchor=CENTER)

label_2 = Label(menu_vereadores,
                text="Vote:",
                font="Arial 10",
                fg="#000000",
                width=5,
                height=2,
                anchor=CENTER)

label_3 = Label(menu_vereadores,
                text="Candidato",
                font="Arial 15",
                fg="#0000ff",
                bd=1,
                relief=GROOVE,
                padx=5,
                pady=5,
                anchor=CENTER)

# Nome candidatos a Vereador
label_4 = Label(menu_vereadores,
                text=" [1] - Piu Piu",
                font="Arial 8 bold",
                fg="#000000",
                width=12,
                height=1,
                anchor=W)

label_5 = Label(menu_vereadores,
                text=" [2] - Hector",
                font="Arial 8 bold",
                fg="#000000",
                width=12,
                height=2,
                anchor=W)

label_6 = Label(menu_vereadores,
                text=" [3] - Frajola",
                font="Arial 8 bold",
                fg="#000000",
                width=12,
                height=2,
                anchor=W)

label_7 = Label(menu_vereadores,
                text=" [4] - Vovó",
                font="Arial 8 bold",
                fg="#000000",
                width=12,
                height=2,
                anchor=W)

label_8 = Label(menu_vereadores,
                text=" [5] - Buldog",
                font="Arial 8 bold",
                fg="#000000",
                width=12,
                height=2,
                anchor=W)

label_9 = Label(menu_vereadores,
                text="[6] - Papa-Leguas",
                font="Arial 8 bold",
                fg="#000000",
                width=15,
                height=1,
                anchor=W)

label_10 = Label(menu_vereadores,
                 text="[7] - Coiote",
                 font="Arial 8 bold",
                 fg="#000000",
                 width=15,
                 height=2,
                 anchor=W)

label_11 = Label(menu_vereadores,
                 text="[8] - Ligeirinho",
                 font="Arial 8 bold",
                 fg="#000000",
                 width=15,
                 height=2,
                 anchor=W)

label_12 = Label(menu_vereadores,
                 text="[9] - Marvin",
                 font="Arial 8 bold",
                 fg="#000000",
                 width=15,
                 height=2,
                 anchor=W)

label_13 = Label(menu_vereadores,
                 text="[0] - Lola",
                 font="Arial 8 bold",
                 fg="#000000",
                 width=15,
                 height=2,
                 anchor=W)

# grid Textos
label_titulo.grid(row=0, column=1)
label_1.grid(row=1, column=1)
label_2.grid(row=1, column=3)
label_3.grid(row=3, column=1)

label_4.grid(row=1, column=6)
label_5.grid(row=3, column=6)
label_6.grid(row=4, column=6)
label_7.grid(row=5, column=6)
label_8.grid(row=6, column=6)
label_9.grid(row=1, column=7)
label_10.grid(row=3, column=7)
label_11.grid(row=4, column=7)
label_12.grid(row=5, column=7)
label_13.grid(row=6, column=7)



# Comandos
def botao_1():
    label_3['text'] = "Piu Piu"

def botao_2():
    label_3['text'] = "Hector"

def botao_3():
    label_3['text'] = "Frajola"

def botao_4():
    label_3['text'] = "Vovô"

def botao_5():
    label_3['text'] = "Buldog"

def botao_6():
    label_3['text'] = "Papa-Léguas"

def botao_7():
    label_3['text'] = "Coiote"

def botao_8():
    label_3['text'] = "Ligeirinho"

def botao_9():
    label_3['text'] = "Marvin"

def botao_10():
    label_3['text'] = "Lola"


# Botões / CMD
cmd_01 = Button(menu_vereadores,
                text=" 1 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_1())

cmd_02 = Button(menu_vereadores,
                text=" 2 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_2())

cmd_03 = Button(menu_vereadores,
                text=" 3 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_3())

cmd_04 = Button(menu_vereadores,
                text=" 4 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_4())

cmd_05 = Button(menu_vereadores,
                text=" 5 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_5())

cmd_06 = Button(menu_vereadores,
                text=" 6 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_6())

cmd_07 = Button(menu_vereadores,
                text=" 7 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_7())

cmd_08 = Button(menu_vereadores,
                text=" 8 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_8())

cmd_09 = Button(menu_vereadores,
                text=" 9 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_9())

cmd_10 = Button(menu_vereadores,
                text=" 0 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_10())

cmd_11 = Button(menu_vereadores,
                text="LIMPA",
                width=5,
                height=2,
                anchor=W,
                bg="#ffff00")

cmd_12 = Button(menu_vereadores,
                text="ENTER",
                width=5,
                height=2,
                anchor=W,
                bg="#00ff00")

# Botões Grid
cmd_01.grid(row=3, column=3)
cmd_02.grid(row=3, column=4)
cmd_03.grid(row=3, column=5)
cmd_04.grid(row=4, column=3)
cmd_05.grid(row=4, column=4)
cmd_06.grid(row=4, column=5)
cmd_07.grid(row=5, column=3)
cmd_08.grid(row=5, column=4)
cmd_09.grid(row=5, column=5)
cmd_10.grid(row=6, column=4)
cmd_11.grid(row=6, column=3)
cmd_12.grid(row=6, column=5)


menu_vereadores.mainloop()