import tkinter as tk
from tkinter import TOP, Label, Button, Toplevel, Entry, font

from strings import *


class TelaDeConfiguracoesDoBairro(object):
    def __init__(self, bairro, tela):
        self.bairro = bairro

        # Caso o tenha feito, cria uma nova janela.
        telaDeConfiguracoesDoBairro = Toplevel(tela)
        telaDeConfiguracoesDoBairro.title(self.bairro)
        telaDeConfiguracoesDoBairro.geometry("305x305")

        frameDeLabels = tk.Frame(telaDeConfiguracoesDoBairro)
        frameDeLabels.pack(side="top", pady=15)

        Label(frameDeLabels, text=bairroSelecionado + ": ").pack(side="left")
        Label(frameDeLabels, text=self.bairro, font=font.Font(weight="bold")).pack(side="left")
        Label(frameDeLabels, text=numeroERua).pack(side="left")

        frameDoCorpo = tk.Frame(telaDeConfiguracoesDoBairro)
        frameDoCorpo.pack()

        # Criação dos campos de entrada para RUA e NÚMERO.
        Label(frameDoCorpo, text=rua).pack()
        self.entRua = Entry(frameDoCorpo, text=digiteSuaRua)
        self.entRua.pack()

        Label(frameDoCorpo, text=numero).pack()
        self.entNumero = Entry(frameDoCorpo, text=digiteSeuNum)
        self.entNumero.pack()

        # Espaçamento entre os campos de entrada e os botões.
        Label(frameDoCorpo, text="").pack()

        # Cria os botões de ação na segunda janela.
        Button(frameDoCorpo, text=criarCasa, command=self.criaCasa).pack(ipadx=20, ipady=5)
        Label(frameDoCorpo, text="").pack()
        Button(frameDoCorpo, text=criarPoste, command=self.criaPoste).pack(ipadx=20, ipady=5)
        Label(frameDoCorpo, text="").pack()
        Button(frameDoCorpo, text=vermapa, command=self.verMapa).pack(ipadx=20, ipady=5)

    def pegarNumRua(self):
        return self.entNumero.get()

    def pegarNomeRua(self):
        return self.entRua.get()

    def criaCasa(self):
        self.rua = self.pegarNomeRua()
        self.numero = self.pegarNumRua()

    def criaPoste(self):
        self.rua = self.pegarNomeRua()
        self.numero = self.pegarNumRua()

    def verMapa(self):
        self.rua = self.pegarNomeRua()
        self.numero = self.pegarNumRua()
