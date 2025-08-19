import streamlit as st

from src.helpers.carga_datos import leer_archivos


def cargar_archivo():
    archivo = st.file_uploader("📄 Subí tu archivo de ventas", type=["xlsx", "xls", "csv", "json"])

    if archivo is not None:
        try:
            df = leer_archivos(archivo, archivo.name)

            if df is not None:
                st.success("✅ Archivo cargado satisfactoriamente")
                st.dataframe(df.head())
                return df
            else:
                st.error("❌ Tipo de archivo no soportado\nPor favor intentar con otro archivo")
                st.stop()

        except Exception as e:
            st.error(f"❌ Error al procesar el archivo: {str(e)}")

    return None
