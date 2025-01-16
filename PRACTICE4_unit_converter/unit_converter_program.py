import pandas as pd

# Funcion que se encarga de convertir la unidades de medida de los muebles.
def cm_to_in(cm):
    return cm / 2.54

# Leer el archivo excel.
# Debe ser el mismo nombre del Excel creado.
df = pd.read_excel('forniture_units.xlsx')

# Añadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de c / 2.54
# Los nombres deben coincidir con los nombres de las columnas creadas en el archivo Excel.
df['Inches'] = df['Centimeters'].apply(cm_to_in)

# Archivo Excel con las unidades de medida convertidas (cm a in).
df.to_excel('converted_forniture_units.xlsx', index = False)

print("Conversión completada y guardada en un nuevo archivo llamado 'converted_forniture_units.xlsx'")