from pathlib import Path

import pandas as pd
import pytest

from src.helpers.carga_datos import leer_archivos

asset_path = Path("tests/assets")


@pytest.mark.parametrize("filename", ["ventas_test.csv", "ventas_test.xlsx", "ventas_test.json"])
def test_archivos_validos(filename):
    ubicacion = asset_path / filename
    with open(ubicacion, "rb") as archivo:
        df = leer_archivos(archivo, ubicacion.name)
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0


@pytest.mark.parametrize("filename", ["archivo.txt"])
def test_archivos_no_soportados(filename):
    ubicacion = asset_path / filename
    with open(ubicacion, "rb") as archivo:
        df = leer_archivos(archivo, ubicacion.name)
    assert df is None
