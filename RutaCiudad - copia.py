import heapq
import tkinter as tk
from tkinter import messagebox

# -----------------------------------
# BASE DE CONOCIMIENTO
# -----------------------------------
reglas = [
    ("Niquia", "Bello", 3),
    ("Bello", "Madera", 2),
    ("Madera", "Acevedo", 2),
    ("Acevedo", "Tricentenario", 3),
    ("Tricentenario", "Caribe", 2),
    ("Caribe", "Universidad", 2),
    ("Universidad", "Hospital", 3),
    ("Hospital", "Prado", 2),
    ("Prado", "ParqueBerrio", 2),
    ("ParqueBerrio", "SanAntonio", 1),
    ("SanAntonio", "Alpujarra", 2),
    ("Alpujarra", "Exposiciones", 2),
    ("Exposiciones", "Industriales", 2),
    ("Industriales", "Poblado", 3),
    ("Poblado", "Aguacatala", 3),
    ("Aguacatala", "Ayura", 2),
    ("Ayura", "Envigado", 2),
    ("Envigado", "Itagui", 3),
    ("Itagui", "Sabaneta", 2),
    ("Sabaneta", "LaEstrella", 3),

    ("Acevedo", "Hospital", 6),
    ("SanAntonio", "Industriales", 4),
    ("Bello", "Acevedo", 5),
    ("Poblado", "Envigado", 5),
]

heuristica = {
    "Niquia": 20, "Bello": 18, "Madera": 17, "Acevedo": 15,
    "Tricentenario": 14, "Caribe": 13, "Universidad": 12,
    "Hospital": 11, "Prado": 10, "ParqueBerrio": 9,
    "SanAntonio": 8, "Alpujarra": 7, "Exposiciones": 6,
    "Industriales": 5, "Poblado": 4, "Aguacatala": 3,
    "Ayura": 2, "Envigado": 1, "Itagui": 1,
    "Sabaneta": 0, "LaEstrella": 0
}

# -----------------------------------
# GRAFO
# -----------------------------------
def construir_grafo(reglas):
    grafo = {}
    for o, d, c in reglas:
        grafo.setdefault(o, []).append((d, c))
        grafo.setdefault(d, []).append((o, c))
    return grafo

# -----------------------------------
# A*
# -----------------------------------
def a_estrella(grafo, inicio, fin):
    cola = [(0, 0, inicio, [])]
    visitados = set()

    while cola:
        f, g, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == fin:
            return g, camino

        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                g_nuevo = g + costo
                h = heuristica.get(vecino, 0)
                heapq.heappush(cola, (g_nuevo + h, g_nuevo, vecino, camino))

    return None

# -----------------------------------
# INTERFAZ
# -----------------------------------
grafo = construir_grafo(reglas)
estaciones = list(grafo.keys())
normalizadas = {e.lower(): e for e in estaciones}

def calcular():
    inicio = entry_inicio.get().strip().lower()
    fin = entry_fin.get().strip().lower()

    if inicio not in normalizadas or fin not in normalizadas:
        messagebox.showerror("Error", "Estación no válida")
        return

    inicio_real = normalizadas[inicio]
    fin_real = normalizadas[fin]

    resultado = a_estrella(grafo, inicio_real, fin_real)

    if resultado:
        costo, camino = resultado
        resultado_texto.set(
            f"Ruta: {' ➜ '.join(camino)}\nCosto: {costo}\nEstaciones: {len(camino)}"
        )
    else:
        resultado_texto.set("No se encontró ruta")

# -----------------------------------
# VENTANA
# -----------------------------------
ventana = tk.Tk()
ventana.title("Sistema Inteligente de Transporte")
ventana.geometry("500x400")

tk.Label(ventana, text="Sistema de Rutas (A*)", font=("Arial", 16)).pack(pady=10)

tk.Label(ventana, text="Inicio:").pack()
entry_inicio = tk.Entry(ventana)
entry_inicio.pack()

tk.Label(ventana, text="Destino:").pack()
entry_fin = tk.Entry(ventana)
entry_fin.pack()

tk.Button(ventana, text="Calcular Ruta", command=calcular).pack(pady=10)

resultado_texto = tk.StringVar()
tk.Label(ventana, textvariable=resultado_texto, wraplength=400).pack(pady=20)

tk.Label(ventana, text="Estaciones disponibles:", font=("Arial", 10, "bold")).pack()

lista = tk.Text(ventana, height=8)
lista.pack()

for e in sorted(estaciones):
    lista.insert(tk.END, e + "\n")

lista.config(state="disabled")

ventana.mainloop()