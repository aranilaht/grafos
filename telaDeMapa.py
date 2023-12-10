import tkinter

from tkinter import Frame, Button, LEFT, BOTH
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
        self.frameMapa.config(width=300, height=900)

        self.frameMapa.pack(side=LEFT)
        self.frameConfig.pack(side=LEFT, fill=BOTH, expand=True)

        self.mapa = TkinterMapView(self.frameMapa, width=900, height=900, corner_radius=0)
        self.mapa.pack()

        Button(self.frameConfig, text='Teste').pack()