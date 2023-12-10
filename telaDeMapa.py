import tkinter

from tkinter import Frame, Button, LEFT, RIGHT, Y, BOTH, Entry, Label, Scrollbar, Listbox, END
from tkintermapview import TkinterMapView

class Mapa(object):
    def __init__(self, bairro, telaTk: tkinter.Tk):
        telaTk.winfo_children()[0].pack_forget()
        telaTk.geometry('1200x900')

        self.mainFrame = Frame(telaTk, width=1200, height=900, bg='red', )
        self.mainFrame.pack(fill=BOTH)

        self.frameMapa = Frame(self.mainFrame)
        self.frameMapa.config(width=900, height=900)

        self.frameConfig = Frame(self.mainFrame, bg='blue')
        self.frameConfig.config(width=300, height=900)

        self.frameMapa.pack(side=LEFT)
        self.frameConfig.pack(side=LEFT, fill=BOTH, expand=True)

        self.mapa = TkinterMapView(self.frameMapa, width=900, height=900, corner_radius=0)
        self.mapa.pack()

        self.redefinirMapa()

        # add postes
        xPostTitle = Label(self.frameConfig, text= 'Coordenada X Poste')
        xPostTitle.grid(row=0, column=0)
        xPostEntry = Entry(self.frameConfig, width = 12)
        xPostEntry.grid(row=0, column=1)

        yPostTitle = Label(self.frameConfig, text= 'Coordenada Y Poste')
        yPostTitle.grid(row=1, column=0)
        yPostEntry = Entry(self.frameConfig, width = 12)
        yPostEntry.grid(row=1, column=1)

        addPostButton = Button(self.frameConfig, text='Adicionar poste')
        addPostButton.grid(row=2, column=0)

        # espaçamento
        Label(self.frameConfig, text="", width=16).grid(row=3)

        #add casa
        xHouseTitle = Label(self.frameConfig, text= 'Coordenada X Casa')
        xHouseTitle.grid(row=4, column=0)
        xHouseEntry = Entry(self.frameConfig, width = 12)
        xHouseEntry.grid(row=4, column=1)

        yHouseTitle = Label(self.frameConfig, text= 'Coordenada Y Casa')
        yHouseTitle.grid(row=5, column=0)
        yHouseEntry = Entry(self.frameConfig, width = 12)
        yHouseEntry.grid(row=5, column=1)

        addHouseButton = Button(self.frameConfig, text='Adicionar Casa')
        addHouseButton.grid(row=6, column=0)

        self.listaDeMarcadores = []
        self.listaDeCaminhos = []
        self.bairro = bairro

    def redefinirMapa(self):
        self.mapa.set_position(-3.752396, -38.532785)
        self.mapa.set_zoom(14)

    def gerarNovoGrafo(self):
        self.redefinirMapa()

    def deletarGrafoAtual(self):
        try:
            self.mapa.delete_all_path()
            self.listaDeMarcadores.clear()
            self.mapa.delete_all_marker()
            self.listaDeCaminhos.clear()
        except:
            pass
