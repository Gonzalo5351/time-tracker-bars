import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.db_manager import read_categories, create_goal

import tkinter as tk
from tkinter import ttk

def configurar_metas():
    def guardar_meta():
        try:
            for i, categoria in enumerate(categorias_nombres):
                horas = float(entries_horas[i].get())
                minutos = float(entries_minutos[i].get())
                total_horas = horas + minutos / 60
                inicio = entry_inicio.get()
                fin = entry_fin.get()

                # Obtener el ID de la categoría
                categoria_id = {nombre: id for id, nombre in categorias}[categoria]

                # Llamar a create_goal con todos los argumentos necesarios
                create_goal(categoria_id, total_horas, 5, inicio, fin)
            label_estado.config(text="Meta guardada exitosamente")
        except Exception as e:
            label_estado.config(text=f"Error: {e}")

    categorias = [
        (1, 'Espiritualidad y sentido de la vida.'),
        (2, 'Superación personal y autodisciplina'),
        (3, 'Familia y relaciones'),
        (4, 'Logro profesional y financiero'),
        (5, 'Expresión artística y legado'),
        (6, 'Placeres y experiencias')
    ]
    categorias_nombres = [nombre for _, nombre in categorias]

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Configuración de Metas Semanales")

    # Título
    tk.Label(root, text="Configuración de Metas Semanales", font=("Arial", 16)).grid(row=0, columnspan=5, pady=10)

    # Tabla de categorías y metas
    tk.Label(root, text="Categoría", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text="Meta (Horas:Minutos)", font=("Arial", 12, "bold")).grid(row=1, column=1, columnspan=4, padx=10, pady=5)

    # Crear entradas para cada categoría
    entries_horas = []
    entries_minutos = []
    for i, categoria in enumerate(categorias_nombres):
        tk.Label(root, text=categoria, anchor="w").grid(row=i+2, column=0, padx=10, pady=5)
        entry_horas = tk.Entry(root, width=5)
        entry_horas.grid(row=i+2, column=1, padx=(5, 0))
        tk.Label(root, text="H").grid(row=i+2, column=2, padx=(0, 2))
        entry_minutos = tk.Entry(root, width=5)
        entry_minutos.grid(row=i+2, column=3, padx=(2, 0))
        tk.Label(root, text="Min").grid(row=i+2, column=4, padx=(0, 5))
        entries_horas.append(entry_horas)
        entries_minutos.append(entry_minutos)

    # Semana
    tk.Label(root, text="Semana:").grid(row=len(categorias_nombres)+2, column=0, padx=10, pady=10)
    entry_inicio = tk.Entry(root, width=10)
    entry_inicio.grid(row=len(categorias_nombres)+2, column=1, padx=5)
    tk.Label(root, text="a").grid(row=len(categorias_nombres)+2, column=2)
    entry_fin = tk.Entry(root, width=10)
    entry_fin.grid(row=len(categorias_nombres)+2, column=3, padx=5)

    # Botones
    tk.Button(root, text="Guardar", command=guardar_meta).grid(row=len(categorias_nombres)+3, column=1, pady=10)
    tk.Button(root, text="Volver", command=root.quit).grid(row=len(categorias_nombres)+3, column=2, pady=10)

    # Label de estado
    label_estado = tk.Label(root, text="")
    label_estado.grid(row=len(categorias_nombres)+4, columnspan=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    configurar_metas()