import tkinter as tk
from tkinter import ttk

# Categorías iniciales
categories = [
    "Espiritualidad y sentido de la vida",
    "Familia y relaciones",
    "Superación personal y autodisciplina",
    "Logro profesional y financiero",
    "Expresión artística y legado",
    "Placeres y experiencias",
]

# Progreso inicial de las categorías
progress_data = {category: 0 for category in categories}


# Función para actualizar el progreso de una categoría
def update_progress(category, increment=10):
    if progress_data[category] + increment <= 100:
        progress_data[category] += increment
        progress_bars[category]["value"] = progress_data[category]
    else:
        progress_data[category] = 100
        progress_bars[category]["value"] = 100


# Configuración de la ventana principal
root = tk.Tk()
root.title("Time Tracker")
root.geometry("600x400")

# Título principal
tk.Label(root, text="Time Tracker - Barras de progreso", font=("Helvetica", 16)).pack(
    pady=10
)

# Contenedor principal para las barras de progreso
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Diccionario para almacenar las barras de progreso
progress_bars = {}

# Crear barras de progreso para cada categoría
for category in categories:
    frame = tk.Frame(main_frame)
    frame.pack(fill=tk.X, pady=5)

    label = tk.Label(frame, text=category, width=30, anchor="w")
    label.pack(side=tk.LEFT)

    progress_bar = ttk.Progressbar(frame, length=300, maximum=100)
    progress_bar.pack(side=tk.LEFT, padx=10)

    # Botón para incrementar el progreso de prueba
    btn = tk.Button(frame, text="+10", command=lambda c=category: update_progress(c))
    btn.pack(side=tk.RIGHT)

    # Guardar referencia de la barra en el diccionario
    progress_bars[category] = progress_bar

# Botón de salida
exit_button = tk.Button(root, text="Salir", command=root.quit)
exit_button.pack(pady=10)

# Iniciar la aplicación
if __name__ == "__main__":
    try:
        root.mainloop()
    except tk.TclError as e:
        print(
            "Error: Asegúrese de tener instalado tkinter y las bibliotecas necesarias."
        )
        print(e)
