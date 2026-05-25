import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from sklearn.neighbors import NearestNeighbors

import joblib

# ==========================================
# DATASET
# ==========================================

df = pd.read_excel(
    "Dataset_KNN_Videojuegos.xlsx"
)

# ==========================================
# FEATURES
# ==========================================

features = [

    "Action",
    "Adventure",
    "Role-Playing",
    "Shooter",
    "Sports",
    "Racing",
    "Puzzle",
    "Simulation",
    "Platform",
    "Misc",

    "multiplayer",
    "difficulty",
    "user_score"
]

X = df[features]

# ==========================================
# NORMALIZAR
# ==========================================

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# ==========================================
# MODELO
# ==========================================

model = NearestNeighbors(

    n_neighbors=10,

    metric="cosine"

)

model.fit(X_scaled)

# ==========================================
# GUARDAR
# ==========================================

joblib.dump(model, "knn_model.pkl")

joblib.dump(scaler, "scaler.pkl")

print("\nMODELO ENTRENADO")