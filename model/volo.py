# from aeroporto import Aeroporto
from dataclasses import dataclass

@dataclass
class Volo:
    _id: int
    _aeroportoP: str
    _aeroportoA: str
    _distanza: int

    @property
    def id(self):
        return self._id

    @property
    def nomePart(self):
        return self._aeroportoP

    @property
    def nomeArr(self):
        return self._aeroportoA

    @property
    def distanza(self):
        return self._distanza

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"Volo id: {self._id} da {self._aeroportoP} a {self._aeroportoA} ; distanza: {self._distanza}"


