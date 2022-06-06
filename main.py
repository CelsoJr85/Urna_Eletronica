from tkinter import *

menu_inicial = Tk()
menu_inicial.title("URNA ELETRÔNICA")
menu_inicial.geometry("500x300")

presidente = []

# Textos / Labels
label_titulo = Label(menu_inicial,
                text="Eleição - 2022",
                font="Time 15",
                fg="#000000",
                width=15,
                height=2,
                anchor=CENTER)

label_1 = Label(menu_inicial,
                text="Você votou em: ",
                font="Arial 10",
                fg="#000000",
                width=20,
                height=2,
                anchor=CENTER)

label_2 = Label(menu_inicial,
                text="Vote:",
                font="Arial 10",
                fg="#000000",
                width=5,
                height=2,
                anchor=CENTER)

label_3 = Label(menu_inicial,
                text="                 ",
                font="Arial 20",
                fg="#0000ff",
                bd=1,
                relief=GROOVE,
                padx=5,
                pady=5,
                anchor=CENTER)

label_4 = Label(menu_inicial,
                text="[1] - Pernalonga",
                font="Arial 10",
                fg="#000000",
                width=15,
                height=2,
                anchor=CENTER)

label_5 = Label(menu_inicial,
                text="[2] - Patolino",
                font="Arial 10",
                fg="#000000",
                width=15,
                height=2,
                anchor=CENTER)

# grid Textos
label_titulo.grid(row=0, column=1)
label_1.grid(row=1, column=1)
label_2.grid(row=1, column=3)
label_3.grid(row=3, column=1)
label_4.grid(row=3, column=6)
label_5.grid(row=4, column=6)


# Comandos
def botao_1():
    label_3['text'] = "Pernalonga"
    presidente.append(label_3["text"])

def botao_2():
    label_3['text'] = "  Patolino   "
    presidente.append(label_3["text"])

def botao_3():
    for texto in label_3["text"]:
        vereadores.py()

# Botões / CMD
cmd_01 = Button(menu_inicial,
                text=" 1 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_1())

cmd_02 = Button(menu_inicial,
                text=" 2 ",
                width=5,
                height=2,
                anchor=W,
                command=lambda: botao_2())

cmd_03 = Button(menu_inicial,
                text=" 3 ",
                width=5,
                height=2,
                anchor=W)

cmd_04 = Button(menu_inicial,
                text=" 4 ",
                width=5,
                height=2,
                anchor=W)

cmd_05 = Button(menu_inicial,
                text=" 5 ",
                width=5,
                height=2,
                anchor=W)

cmd_06 = Button(menu_inicial,
                text=" 6 ",
                width=5,
                height=2,
                anchor=W)

cmd_07 = Button(menu_inicial,
                text=" 7 ",
                width=5,
                height=2,
                anchor=W)

cmd_08 = Button(menu_inicial,
                text=" 8 ",
                width=5,
                height=2,
                anchor=W)

cmd_09 = Button(menu_inicial,
                text=" 9 ",
                width=5,
                height=2,
                anchor=W)

cmd_10 = Button(menu_inicial,
                text=" 0 ",
                width=5,
                height=2,
                anchor=W)

cmd_11 = Button(menu_inicial,
                text="LIMPA",
                width=5,
                height=2,
                anchor=W,
                bg="#ffff00")

cmd_12 = Button(menu_inicial,
                text="ENTER",
                width=5,
                height=2,
                anchor=W,
                bg="#00ff00",
                command=lambda: botao_3())

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


menu_inicial.mainloop()