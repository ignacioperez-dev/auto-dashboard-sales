import pandas as pd


def leer_archivos(archivo, filename):
    if filename.endswith((".xlsx", ".xls")):
        df = pd.read_excel(archivo)
        return df

    elif filename.endswith(".csv"):
        df = pd.read_csv(archivo)
        return df

    elif filename.endswith(".json"):
        df = pd.read_json(archivo)
        return df

    else:
        return None
