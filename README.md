# 🚇 Sistema Inteligente de Rutas con A*

## 📌 Descripción

Este proyecto implementa un sistema inteligente capaz de encontrar la mejor ruta entre dos estaciones dentro de un sistema de transporte masivo.

El sistema utiliza técnicas de Inteligencia Artificial, específicamente:

- Representación del conocimiento mediante reglas lógicas
- Búsqueda heurística utilizando el algoritmo A* (A estrella)

Además, cuenta con una interfaz gráfica desarrollada en Tkinter para facilitar la interacción con el usuario.

---

## 🧠 Tecnologías utilizadas

- Python 3
- Tkinter (interfaz gráfica)
- heapq (cola de prioridad)

---

## ⚙️ Funcionamiento

El sistema está basado en:

1. *Base de conocimiento*  
   Representada como un conjunto de reglas que definen conexiones entre estaciones.

2. *Grafo de rutas*  
   Las reglas se transforman en un grafo bidireccional.

3. *Algoritmo A\**  
   Se utiliza para encontrar la mejor ruta combinando:
   - Costo real del camino
   - Función heurística (estimación al destino)

---

## ▶️ Ejecución del proyecto

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>Ingresar a la carpeta:
cd nombre-del-proyecto
Ejecutar la aplicación:
python app.py
