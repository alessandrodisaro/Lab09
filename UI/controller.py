import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        voli_distanza = self._model.buildGraphConDistanzaNormale(self._view._txtIn.value)

        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Ci sono {self._model._grafo.number_of_nodes()} aeroporti")) #  METTI QUANTI AEROPORTI CI SONO
        self._view._txt_result.controls.append(ft.Text(f"Ci sono {len(voli_distanza)} voli di connessione tra questi "
                                                       f"aeroporti"))
        for volo in voli_distanza:
            self._view._txt_result.controls.append(ft.Text(f"Volo da {volo[0]} a {volo[1]} con distanza: {volo[2]}"))

        self._view.update_page()

