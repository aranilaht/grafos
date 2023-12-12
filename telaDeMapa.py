import os
import random
import tkinter

from tkinter import *

import pandas as pd
from tkintermapview import TkinterMapView
from assets import *


class Mapa(object):
    def __init__(self):

        self.mainFrame = Frame(telaTk, width=1200, height=900)
        self.mainFrame.pack(fill=BOTH)

        self.frameMapa = Frame(self.mainFrame)
        self.frameMapa.config(width=900, height=900)

        self.frameConfig = Frame(self.mainFrame)
        self.frameConfig.config(width=300, height=900)

        self.frameMapa.pack(side=LEFT)
        self.frameConfig.pack(fill=BOTH, expand=True)

        self.mapa = TkinterMapView(self.frameMapa, width=900, height=900, corner_radius=0)

        self.mapa.pack()

        self.redefinirMapa()

        self.maiorDistancia = 0

        # add postes
        xPostTitle = Label(self.frameConfig, text='Coordenada X Poste')
        xPostTitle.grid(row=0, column=0, padx=20, pady=(300, 0))
        self.xPostEntry = Entry(self.frameConfig, width=12)
        self.xPostEntry.grid(row=0, column=1, pady=(300, 0))

        yPostTitle = Label(self.frameConfig, text='Coordenada Y Poste')
        yPostTitle.grid(row=1, column=0, pady=(10, 0))
        self.yPostEntry = Entry(self.frameConfig, width=12)
        self.yPostEntry.grid(row=1, column=1, pady=(10, 0))

        addPostButton = Button(self.frameConfig, text='Adicionar poste', command=self.adicionarPoste)
        addPostButton.grid(row=2, column=0, padx=(120, 0), pady=(10, 0))

        # espaçamento
        Label(self.frameConfig, text="", width=16).grid(row=3, pady=(50, 0))

        # add casa
        xHouseTitle = Label(self.frameConfig, text='Coordenada X Casa')
        xHouseTitle.grid(row=4, column=0, pady=(50, 0))
        self.xHouseEntry = Entry(self.frameConfig, width=12)
        self.xHouseEntry.grid(row=4, column=1, pady=(50, 0))

        yHouseTitle = Label(self.frameConfig, text='Coordenada Y Casa')
        yHouseTitle.grid(row=5, column=0, pady=(10, 0))
        self.yHouseEntry = Entry(self.frameConfig, width=12)
        self.yHouseEntry.grid(row=5, column=1, pady=(10, 0))

        addHouseButton = Button(self.frameConfig, text='Adicionar Casa')
        addHouseButton.grid(row=6, column=0, padx=(120, 0), pady=(10, 0))

        self.maiorDistanciaLabel = Label(self.frameConfig, text=f'Maior distância entre pontos:\n{self.maiorDistancia}')
        self.maiorDistanciaLabel.grid(row=7, padx=(50, 0), pady=(50, 0))

        self.mapa.add_left_click_map_command(self.left_click_event)

        self.gerarGrafoBase()

        self.marcadorTemporario = None

    def redefinirMapa(self):
        self.mapa.set_position(-3.740432, -38.540242)
        self.mapa.set_zoom(14)

    def left_click_event(self, coordinates_tuple):
        self.xPostEntry.delete(0, END)
        self.yPostEntry.delete(0, END)
        self.xPostEntry.insert(0, coordinates_tuple[0])
        self.yPostEntry.insert(0, coordinates_tuple[1])

        if self.marcadorTemporario is not None:
            self.mapa.canvas_marker_list.remove(self.marcadorTemporario)
            self.marcadorTemporario.delete()

        self.marcadorTemporario = self.mapa.set_marker(coordinates_tuple[0], coordinates_tuple[1],
                                                       marker_color_circle="blue", marker_color_outside="#C5542D")

    def adicionarPoste(self):
        """
        lat = float(self.xPostEntry.get())
        lon = float(self.yPostEntry.get())

        csv = pd.read_csv(os.getcwd() + '\\MST_Benfica.csv')

        inicio = csv.iloc[0].Poste_Origem
        shortest_vertex, minDistance = dijkstra(grafo, inicio, lat, lon)

        #Poste_Origem, Poste_Destino, Distancia, Lat_Poste_Origem, Lon_Poste_Origem, Lat_Poste_Destino, Lon_Poste_Destino

        shortest_vertexData = csv[csv["Poste_Origem"] == shortest_vertex]
        if shortest_vertexData.__str__() == 'Empty DataFrame':
            shortest_vertexData = csv[csv["Poste_Destino"] == shortest_vertex]
        print(shortest_vertex, shortest_vertexData)
        x = safe_float(shortest_vertexData["Lat_Poste_Origem"].iloc[-1])
        y = safe_float(shortest_vertexData["Lon_Poste_Origem"].iloc[-1])

        print(shortest_vertex, minDistance)

        self.mapa.set_path([(x, y), (lat, lon)])
    """
        pass

    def gerarGrafoBase(self):
        if len(self.mapa.canvas_marker_list) == 0:
            textset = set()
            csv = pd.read_csv(os.getcwd() + '\\MST_Benfica.csv')

            for index, (posteO, latO, lonO, posteD, latD, lonD, distancia) in csv[['Poste_Origem', 'Lat_Poste_Origem',
                                                                                   'Lon_Poste_Origem', 'Poste_Destino',
                                                                                   'Lat_Poste_Destino',
                                                                                   'Lon_Poste_Destino',
                                                                                   'Distancia']
            ].iterrows():

                if posteO not in textset:
                    self.mapa.set_marker(latO, lonO)
                    textset.add(posteO)
                if posteD not in textset:
                    self.mapa.set_marker(latD, lonD)
                    textset.add(posteD)

                self.mapa.set_path([(latO, lonO), (latD, lonD)], color='blue', width=2)
                # color = random.choice(['#9f0000', '#3f00ff', '#54ff9f', '#fce97d']),

                if distancia > self.maiorDistancia:
                    self.maiorDistancia = round(distancia, 2)

                edge = EdgeNDForMap(
                    point1=posteO,
                    point2=posteD,
                    weight=distancia,
                    latPoint1=latO,
                    lonPoint1=lonO,
                    latPoint2=latD,
                    lonPoint2=lonD,
                )
                grafo.append(edge)

            self.maiorDistanciaLabel.config(text=f'Maior distância entre pontos:\n{self.maiorDistancia} metros')

        print(self.maiorDistancia)

    def deletarGrafoAtual(self):
        try:
            self.mapa.delete_all_path()
            self.mapa.delete_all_marker()
        except:
            pass


if __name__ == '__main__':
    telaTk = Tk()
    telaTk.geometry("1200x900")
    Mapa()
    telaTk.mainloop()
