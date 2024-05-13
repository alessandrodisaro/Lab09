from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._aeroporti = []
        self._grafo = nx.Graph()
        self._idMap = {}
        self.loadAeroporti()


    def loadAeroporti(self):
        nodi = DAO.getAllAeroporti()
        for nodo in nodi:
            self._aeroporti.append(nodo)
            self._idMap[nodo.id] = nodo


    # COSTRUENDO IL GRAFO PRIMA
    def buildGraph(self):
        voli = DAO.getAllVoli(0)
        for flight in voli:
            self._grafo.add_edge(self._idMap[flight.nomePart], self._idMap[flight.nomeArr], distanza=flight.distanza)

    # COSTRUENDO IL GRAFO PRIMA DI VISITARLO
    def findFlights(self, distance):
        visitati = []
        for u, v in self._grafo.edges():
            if self._grafo[u][v] > distance:
                visitati.append((u, v))
        return visitati




    #  SENZA COSTRUIRE IL GRAFO PRIMA
    def buildGraphConDistanzaNormale(self, distance):
        self._grafo.add_nodes_from(self._aeroporti)
        voli = DAO.getAllVoli(distance)
        results = []
        # archi
        for vol in voli:
            self._grafo.add_edge(vol.nomePart, vol.nomeArr, distanza=vol.distanza)

        for arco in self._grafo.edges:
            dist = self._grafo[arco[0]][arco[1]]
            results.append((self._idMap[arco[0]].nomeAeroporto, self._idMap[arco[1]].nomeAeroporto, dist))
        return results





