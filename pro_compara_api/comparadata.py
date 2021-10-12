class Grafo:
    def __init__(self, nodos, enlaces):
        self.nodos = nodos
        self.enlaces = enlaces


class ComparaGraph:
    def __init__(self, grafoG, grafoH, MCS, ged, image):
        self.grafoG = grafoG
        self.grafoH = grafoH
        self.MCS = MCS
        self.ged = ged
        self.image = image