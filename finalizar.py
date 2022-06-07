from tkinter import *

resultado_p = []
resultado_v = []

def finalizar():
    menu_inicial = Tk()
    menu_inicial.title("URNA ELETRÔNICA")
    menu_inicial.geometry("500x300")

    def bot_fin():
        print("Presidente: {}, Vereador {}.".format(resultado_p, resultado_v))

    label_unica = Label(menu_inicial,
                        text="FIM",
                        font="Time 20",
                        fg="#000000",
                        width=20,
                        height=2,
                        anchor=CENTER)
    label_unica.grid(row=1, column=3)

    cmd_unico = Button(menu_inicial,
                       text=" Clique aqui para finalizar",
                       width=20,
                       height=2,
                       anchor=CENTER,
                       command=lambda: bot_fin())
    cmd_unico.grid(row=2, column=3)

    menu_inicial.mainloop()
