from database.DAO import DAO

class Model:
    def __init__(self):
        self._aeroposrti = []
        self.loadAeroporti()
        self._grafo = None


    def loadAeroporti(self):
        nodi = DAO.getAllAeroporti()
        for nodo in nodi:
            self._aeroposrti.append(nodo)


    def buildGraphConDistanza(self, distanza):
        voli = DAO.getAllVoli(distanza)

        ADESSO COSTRUISCI IL GRAFO DI TUTTI GLI AEROPORTI COLLEGATI DA UN VOLO DISTANTE ALMENO "DISTANZA" MIGLIA




