from tkinter import messagebox, TOP, Label, OptionMenu, Button, BOTTOM, StringVar, Tk, Frame

from strings import *
from telaDeConfiguracoes import TelaDeConfiguracoesDoBairro

telaTK = Tk()
telaTK.geometry("300x300")

variable = StringVar(telaTK)
variable.set(listaDeBairros[0])


class EscolhaDeBairro(object):
    def __init__(self):
        tela = Frame(telaTK)
        tela["width"] = 45
        tela["height"] = 45
        tela.pack(side=TOP)

        msg = Label(tela, text=selecioneUmBairro)
        msg["font"] = ("Verdana", "15")
        msg.pack(ipadx=50, ipady=50, side=TOP)

        # Componente de dropdown com as opções de bairros.
        opcoes = OptionMenu(tela, variable, *listaDeBairros)
        opcoes["width"] = 15
        opcoes.pack(ipadx=20, ipady=10, side=TOP)

        # Espaçamento entre os componentes.
        Label(tela, text="").pack()

        # Botão de selecionar o bairro.
        self.proximoBt = Button(tela, text=proximo, command=self.abrirTelaDeConfiguracoesDoBairro)
        self.proximoBt["width"] = 10

        self.proximoBt.pack(ipadx=20, ipady=10, side=BOTTOM)

    def abrirTelaDeConfiguracoesDoBairro(self):
        self.bairro = variable.get()
        #
        # Validação para saber se o usuário selecionou corretamente um bairro.
        if self.bairro == selecioneOpcao:
            messagebox.showinfo(tituloPaginaDeErro, mensagemDeErro)
        else:
            TelaDeConfiguracoesDoBairro(self.bairro, telaTK)


# Início da tela de selação.
EscolhaDeBairro()
telaTK.mainloop()
