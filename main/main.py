import tkinter as tk
from model.model import Graph
from view.View import View
from controller.controller import Controller

if __name__ == "__main__":
    root = tk.Tk()

    model = Graph()
    for name in ["E_1", "E_2", "E_3", "E_4", "S_1", "S_2", "S_3", "S_4" , "O_1","O_2","O_3","O_4"]:
        model.add_node(name)
    model.add_edge("E_1", "S_1", 50, 3, 1)  # Ejemplo de atributos
    model.add_edge("E_2", "S_2", 20, 2, 0)
    model.add_edge("E_3", "S_3", 30, 4, 2)
    model.add_edge("E_4", "S_4", 40, 5, 1)
    model.add_edge("S_1", "O_1", 60, 6, 3)
    model.add_edge("S_2", "O_2", 60, 6, 3)
    model.add_edge("S_3", "O_3", 60, 6, 3)
    model.add_edge("S_4", "O_4", 60, 6, 3)

    controller = Controller(None, model)
    view = View(root, controller)
    controller.view = view

    root.mainloop()
