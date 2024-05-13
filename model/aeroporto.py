from dataclasses import dataclass

@dataclass
class Aeroporto:
    _ID: int
    _IATA_CODE: str
    _AEROPORTO: str


    @property
    def id(self):
        return self._ID

    @property
    def nomeAeroporto(self):
        return self._AEROPORTO

    def __hash__(self):
        return hash(self._ID)

    def __str__(self):
        return self._AEROPORTO

