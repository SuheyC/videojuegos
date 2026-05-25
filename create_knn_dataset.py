import pandas as pd

# ==========================================
# CARGAR DATASET ORIGINAL
# ==========================================

df = pd.read_excel(
    "Data_set_videojuegos_normalizado.xlsx",
    sheet_name="Dataset "
)

# ==========================================
# LIMPIAR COLUMNAS
# ==========================================

df.columns = df.columns.str.strip()

# ==========================================
# GENEROS
# ==========================================

genres = [

    "Action",
    "Adventure",
    "Role-Playing",
    "Shooter",
    "Sports",
    "Racing",
    "Puzzle",
    "Simulation",
    "Platform",
    "Misc"
]

# ==========================================
# CREAR COLUMNAS
# ==========================================

for genre in genres:

    df[genre] = 0

# ==========================================
# MARCAR GENEROS
# ==========================================

for i, row in df.iterrows():

    game_genre = str(row["GENERO"]).strip()

    if game_genre in genres:

        df.at[i, game_genre] = 1

# ==========================================
# MULTIPLAYER
# ==========================================

df["multiplayer"] = 0

for i, row in df.iterrows():

    mode = str(row["Modo de juego"]).lower()

    if "multi" in mode:

        df.at[i, "multiplayer"] = 1

# ==========================================
# DIFICULTAD
# ==========================================

df["difficulty"] = pd.to_numeric(

    df["dificultad"],

    errors="coerce"

).fillna(1)

# ==========================================
# USER SCORE
# ==========================================

df["user_score"] = pd.to_numeric(

    df["User_Score"],

    errors="coerce"

).fillna(5)

# ==========================================
# DATASET FINAL
# ==========================================

final_df = df[

    genres +

    [

        "multiplayer",

        "difficulty",

        "user_score"

    ]

]

# ==========================================
# GUARDAR
# ==========================================

final_df.to_excel(

    "Dataset_KNN_Videojuegos.xlsx",

    index=False

)

print("\nDATASET KNN CREADO")