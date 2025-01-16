import pandas as pd

# Dataframe es la información básica con el nombre de las piezas y centímetros para poder armar el Excel
data = {
    "Pieces": ["Leg", "Board", "Door", "Shelf", "Side Panel", "Window"],
    "Centimeters": [40, 120, 60, 30, 180, 150],
}
# Guardar el DataFrame en un archivo Excel
df = pd.DataFrame(data)
df.to_excel("furniture_units.xlsx", index=False)
