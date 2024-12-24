import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.db_manager import read_categories, update_time_log

import tkinter as tk
from tkinter import ttk
from db.db_manager import read_categories, update_time_log

class CronometrosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetros Independientes")

        self.categorias = [
            (1, 'Espiritualidad y sentido de la vida.'),
            (2, 'Superación personal y autodisciplina'),
            (3, 'Familia y relaciones'),
            (4, 'Logro profesional y financiero'),
            (5, 'Expresión artística y legado'),
            (6, 'Placeres y experiencias')
        ]

        self.tiempos = {categoria[0]: 0 for categoria in self.categorias}  # Tiempo en segundos
        self.activos = {categoria[0]: False for categoria in self.categorias}  # Estado del cronómetro
        self.labels_tiempo = {}  # Almacenar referencias a los labels de tiempo

        self.create_ui()

    def create_ui(self):
        for i, (id_categoria, nombre_categoria) in enumerate(self.categorias):
            tk.Label(self.root, text=nombre_categoria).grid(row=i, column=0, padx=10, pady=5)

            # Label para mostrar el tiempo
            label_tiempo = tk.Label(self.root, text="00:00:00")
            label_tiempo.grid(row=i, column=1, padx=10, pady=5)
            self.labels_tiempo[id_categoria] = label_tiempo

            # Botones de control
            tk.Button(self.root, text="Iniciar", command=lambda id=id_categoria: self.iniciar(id)).grid(row=i, column=2, padx=5)
            tk.Button(self.root, text="Pausar", command=lambda id=id_categoria: self.pausar(id)).grid(row=i, column=3, padx=5)
            tk.Button(self.root, text="Resetear", command=lambda id=id_categoria, label=label_tiempo: self.resetear(id, label)).grid(row=i, column=4, padx=5)

    def iniciar(self, id_categoria):
        if not self.activos[id_categoria]:
            self.activos[id_categoria] = True
            self.actualizar_tiempo(id_categoria)

    def pausar(self, id_categoria):
        self.activos[id_categoria] = False

    def resetear(self, id_categoria, label_tiempo):
        self.activos[id_categoria] = False
        self.tiempos[id_categoria] = 0
        label_tiempo.config(text="00:00:00")

    def actualizar_tiempo(self, id_categoria):
        if self.activos[id_categoria]:
            self.tiempos[id_categoria] += 1
            horas, resto = divmod(self.tiempos[id_categoria], 3600)
            minutos, segundos = divmod(resto, 60)
            self.labels_tiempo[id_categoria].config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            self.root.after(1000, self.actualizar_tiempo, id_categoria)

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometrosApp(root)
    root.mainloop()