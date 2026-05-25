
# 🎮 Sistema Inteligente de Recomendación de Videojuegos

Proyecto final de la materia de Inteligencia Artificial.

Este proyecto consiste en un sistema web de recomendación de videojuegos basado en Machine Learning utilizando el algoritmo KNN (K-Nearest Neighbors). El sistema aprende los gustos del usuario mediante rondas tipo VS entre videojuegos y posteriormente genera recomendaciones personalizadas.

---

#  Descripción del proyecto

El usuario interactúa con una interfaz visual donde debe escoger entre dos videojuegos en varias rondas VS.

Cada selección:
- aumenta pesos en el perfil del usuario,
- construye preferencias,
- y permite generar recomendaciones inteligentes basadas en similitud.

El sistema utiliza:
- Machine Learning,
- procesamiento de datos,
- perfiles dinámicos,
- y una interfaz web interactiva.

---

#  Tecnologías utilizadas

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- KNN (NearestNeighbors)
- MinMaxScaler

## Frontend
- HTML
- CSS

## Manejo de datos
- Pandas
- OpenPyXL

---

#  Estructura del proyecto

```bash
video_game_recommender/
│
├── app.py
├── train_model.py
├── knn_model.pkl
├── scaler.pkl
├── Dataset_KNN_Videojuegos.xlsx
├── Data_set_videojuegos_normalizado.xlsx
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── style.css
│   └── images/
│       └── default.jpg
│
└── README.md


---

#  Funcionamiento del sistema

##  Entrenamiento del modelo

El sistema utiliza un dataset numérico basado en características de videojuegos:

* géneros,
* dificultad,
* modo multijugador,
* puntuaciones,
* entre otros.

El modelo KNN aprende relaciones de similitud entre videojuegos utilizando distancia coseno.

---

##  Rondas VS

El usuario participa en 12 rondas donde selecciona entre dos videojuegos diferentes.

Cada elección:

* aumenta pesos en el perfil,
* registra preferencias,
* y construye un vector numérico del usuario.

---

## Recomendaciones

Al finalizar las rondas:

* el perfil se normaliza,
* el modelo KNN busca videojuegos similares,
* y el sistema muestra recomendaciones personalizadas.

---

#  Dataset

El proyecto utiliza dos datasets:

## Dataset visual

Contiene:

* nombres,
* imágenes,
* descripciones,
* géneros,
* información visual.

Columnas principales:

* NOMBRE
* GENERO
* Descripcion
* Imagen
* User_Score
* Plataforma

---

## Dataset KNN

Dataset completamente numérico utilizado por el modelo.

Columnas:

* Action
* Adventure
* Role-Playing
* Shooter
* Sports
* Racing
* Puzzle
* Simulation
* Platform
* Misc
* multiplayer
* difficulty
* user_score

---

#  Preprocesamiento de datos

Durante el desarrollo:

* se limpiaron columnas innecesarias,
* se eliminaron datos irrelevantes,
* y se transformaron características en valores numéricos.

También:

* se agregaron imágenes manualmente,
* se utilizaron scripts para automatizar parte del proceso,
* y se implementó una imagen por defecto para juegos sin imagen disponible.

---

#  Modelo utilizado

## KNN (K-Nearest Neighbors)

Se eligió KNN porque:

* funciona muy bien en problemas de similitud,
* es sencillo de implementar,
* y permite generar recomendaciones rápidas.

Configuración utilizada:

```python
model = NearestNeighbors(
    n_neighbors=10,
    metric="cosine"
)
```

---

#  Cómo ejecutar el proyecto

##  Crear entorno virtual

```bash
python -m venv venv
```

---

##  Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

---

##  Instalar dependencias

```bash
pip install flask pandas scikit-learn openpyxl joblib
```

---

##  Entrenar modelo

```bash
python train_model.py
```

---

## Ejecutar aplicación

```bash
python app.py
```

---

#  Acceder al sistema

Abrir en navegador:

```bash
http://127.0.0.1:5000
```

O desde otro dispositivo conectado a la misma red:

```bash
http://TU-IP:5000
```

---

#  Resultados obtenidos

El sistema logró:

* generar recomendaciones personalizadas,
* construir perfiles dinámicos,
* y mejorar precisión aumentando las rondas VS.

Inicialmente se utilizaban 5 rondas, pero posteriormente se aumentó a 12 rondas para obtener mejores resultados.

---

#  Mejoras futuras

Posibles mejoras:

* botón de “Saltar” en rondas VS,
* datasets más modernos,
* usuarios reales,
* almacenamiento de perfiles,
* recomendaciones híbridas,
* integración con APIs,
* redes neuronales,
* Deep Learning.

---

Materia:
Inteligencia Artificial

---

# 📚 Librerías principales

* Flask
* Pandas
* Scikit-learn
* Joblib
* OpenPyXL

```
```
