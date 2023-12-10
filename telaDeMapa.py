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
 
        Entry(self.frameConfig, width = 10).pack()
        Entry(self.frameConfig, width = 10).pack()
        Button(self.frameConfig, text='Adicionar poste').pack()

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
