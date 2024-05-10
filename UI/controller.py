import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        voli = self._model.getAeroportiDistanza(self._view._txtIn.value)

        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text("Ci sono ")) #  METTI QUANTI AEROPORTI CI SONO
        self._view._txt_result.controls.append(ft.Text(f"Ci sono {len(voli)} voli di connessione tra questi "
                                                       f"aeroporti"))
        for volo in voli:
            self._view._txt_result.controls.append(ft.Text(volo))

        self._view.update_page()

