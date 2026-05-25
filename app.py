from flask import Flask, render_template, redirect
import pandas as pd
import joblib

app = Flask(__name__)

# ==========================================
# CARGAR DATASET KNN
# ==========================================

df_knn = pd.read_excel(
    "Dataset_KNN_Videojuegos.xlsx"
)

# ==========================================
# CARGAR DATASET VISUAL
# ==========================================

df_info = pd.read_excel(
    "Data_set_videojuegos_normalizado.xlsx",
    sheet_name="Dataset "
)

# ==========================================
# LIMPIAR COLUMNAS
# ==========================================

df_info.columns = df_info.columns.str.strip()

df_info["GENERO"] = (
    df_info["GENERO"]
    .astype(str)
    .str.strip()
)

# ==========================================
# MODELO
# ==========================================

model = joblib.load("knn_model.pkl")

scaler = joblib.load("scaler.pkl")

# ==========================================
# VARIABLES GLOBALES
# ==========================================

games_shown = []

round_count = 0

MAX_ROUNDS = 12

# ==========================================
# PERFIL DEL USUARIO
# ==========================================

user_profile = {

    "Action": 0,
    "Adventure": 0,
    "Role-Playing": 0,
    "Shooter": 0,
    "Sports": 0,
    "Racing": 0,
    "Puzzle": 0,
    "Simulation": 0,
    "Platform": 0,
    "Misc": 0,

    "multiplayer": 0,
    "difficulty": 0,
    "user_score": 0
}

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    global games_shown
    global round_count
    global user_profile

    games_shown = []

    round_count = 0

    user_profile = {

        "Action": 0,
        "Adventure": 0,
        "Role-Playing": 0,
        "Shooter": 0,
        "Sports": 0,
        "Racing": 0,
        "Puzzle": 0,
        "Simulation": 0,
        "Platform": 0,
        "Misc": 0,

        "multiplayer": 0,
        "difficulty": 0,
        "user_score": 0
    }

    return redirect("/vs")

# ==========================================
# VS
# ==========================================

@app.route("/vs")
def vs():

    global round_count

    if round_count >= MAX_ROUNDS:
        return redirect("/results")

    available_games = df_info[
        ~df_info.index.isin(games_shown)
    ]

    # ==========================================
    # EVITAR MISMO GENERO
    # ==========================================

    while True:

        selected = available_games.sample(2)

        game1 = selected.iloc[0]
        game2 = selected.iloc[1]

        genre1 = str(game1["GENERO"]).strip()
        genre2 = str(game2["GENERO"]).strip()

        if genre1 != genre2:
            break

    games_shown.append(game1.name)
    games_shown.append(game2.name)

    game1_dict = game1.to_dict()
    game2_dict = game2.to_dict()

    game1_dict["row_id"] = game1.name
    game2_dict["row_id"] = game2.name

    # ==========================================
    # IMAGENES
    # ==========================================

    if pd.isna(game1_dict.get("Imagen")):
        game1_dict["Imagen"] = "/static/images/default.jpg"

    if pd.isna(game2_dict.get("Imagen")):
        game2_dict["Imagen"] = "/static/images/default.jpg"

    return render_template(

        "index.html",

        game1=game1_dict,

        game2=game2_dict,

        round=round_count + 1,

        total_rounds=MAX_ROUNDS
    )

# ==========================================
# CHOOSE
# ==========================================

@app.route("/choose/<int:row_id>")
def choose(row_id):

    global round_count

    game = df_info.iloc[row_id]

    # ==========================================
    # GENERO
    # ==========================================

    genre = str(game["GENERO"]).strip()

    if genre in user_profile:
        user_profile[genre] += 3

    # ==========================================
    # MULTIPLAYER
    # ==========================================

    try:

        mode = str(
            game["Modo de juego"]
        ).lower()

        if "multi" in mode:
            user_profile["multiplayer"] += 1

    except:
        pass

    # ==========================================
    # DIFICULTAD
    # ==========================================

    try:

        user_profile["difficulty"] += float(
            game["dificultad"]
        )

    except:
        pass

    # ==========================================
    # USER SCORE
    # ==========================================

    try:

        user_profile["user_score"] += float(
            game["User_Score"]
        )

    except:
        pass

    round_count += 1

    return redirect("/vs")

# ==========================================
# RESULTS
# ==========================================

@app.route("/results")
def results():

    # ==========================================
    # PERFIL NUMERICO
    # ==========================================

    profile = pd.DataFrame([{

        "Action": user_profile["Action"],
        "Adventure": user_profile["Adventure"],
        "Role-Playing": user_profile["Role-Playing"],
        "Shooter": user_profile["Shooter"],
        "Sports": user_profile["Sports"],
        "Racing": user_profile["Racing"],
        "Puzzle": user_profile["Puzzle"],
        "Simulation": user_profile["Simulation"],
        "Platform": user_profile["Platform"],
        "Misc": user_profile["Misc"],

        "multiplayer": (
            user_profile["multiplayer"]
            / MAX_ROUNDS
        ),

        "difficulty": (
            user_profile["difficulty"]
            / MAX_ROUNDS
        ),

        "user_score": (
            user_profile["user_score"]
            / MAX_ROUNDS
        )
    }])

    # ==========================================
    # NORMALIZAR
    # ==========================================

    profile_scaled = scaler.transform(profile)

    # ==========================================
    # KNN
    # ==========================================

    distances, indices = model.kneighbors(

        profile_scaled,

        n_neighbors=30
    )

    recommendations = []

    used_games = set()

    # ==========================================
    # RECOMENDACIONES
    # ==========================================

    for i in indices[0]:

        game = df_info.iloc[i]

        game_name = str(game["NOMBRE"])

        if game_name in used_games:
            continue

        recommendations.append(game)

        used_games.add(game_name)

        if len(recommendations) >= 6:
            break

    # ==========================================
    # IMAGENES
    # ==========================================

    final_recommendations = []

    for game in recommendations:

        game_dict = game.to_dict()

        if pd.isna(game_dict.get("Imagen")):
            game_dict["Imagen"] = "/static/images/default.jpg"

        final_recommendations.append(game_dict)

    return render_template(

        "results.html",

        recommendations=final_recommendations,

        profile=user_profile
    )

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)
 #   app.run(debug=True)