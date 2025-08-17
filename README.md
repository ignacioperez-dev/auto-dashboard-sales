# 📊 AutoDashboard de Ventas
> Transforma tus datos de ventas en insights accionables de forma automática y al instante.

---

## 🚀 Acerca del Proyecto

**AutoDashboard de Ventas** es una aplicación web diseñada para simplificar el análisis de datos de ventas. En lugar de complejos procesos manuales, la herramienta permite a cualquier usuario subir un archivo de ventas (CSV, XLSX o JSON) y obtener automáticamente un dashboard con los **KPIs clave**, **gráficos interactivos** e **insights valiosos**.

El objetivo es democratizar el análisis de datos, proporcionando una solución rápida y visual para que negocios de todos los tamaños puedan entender mejor su rendimiento y comportamiento de clientes.

---

## ✅ Funcionalidades y Roadmap

Este proyecto se desarrolla en fases, comenzando con un **Producto Mínimo Viable (MVP)** que ya está operativo.

### **Versión 1: MVP (Funcionalidades Actuales)**

- **Carga de Archivos:** Sube fácilmente archivos de ventas en formatos `.csv`, `.xlsx` y `.json`.
- **Vista Previa de Datos:** Muestra una tabla con los datos crudos para una verificación rápida.
- **KPIs Clave:** Calcula y visualiza métricas esenciales como:
    - **Total de ventas**
    - **Promedio de ventas por cliente**
    - **Cantidad de productos únicos vendidos**
- **Gráficos Dinámicos:** Genera visualizaciones interactivas con **Plotly** para:
    - **Ventas por día** (gráfico de barras)
    - **Ventas por producto** (gráfico de barras o circular)
- **Persistencia en DB:** Guarda la metadata de cada carga y el archivo subido en una base de datos **Neon (Postgres)** para su posterior análisis.

### **Versión 2: Análisis Avanzado**

*Funcionalidades planificadas para proporcionar una comprensión más profunda del negocio.*

- **Segmentación de Clientes:** Clasifica a los clientes en grupos como "Frecuentes", "Esporádicos" y "Nuevos".
- **Análisis de Tendencias:** Visualiza el rendimiento de ventas a lo largo del tiempo (mensual, semanal).
- **Proyección de Ventas:** Realiza una proyección simple de ventas futuras basada en promedios históricos.

### **Versión 3: Modo "Analista de Producto"**

*Funcionalidades avanzadas para generar insights estratégicos y narrativas automáticas.*

- **Co-compra de Productos:** Identifica qué productos se compran juntos con mayor frecuencia.
- **Narrativa Automática:** Genera resúmenes en lenguaje natural de los datos, por ejemplo: *"El producto Z se vende un 30% más los lunes"* o *"Juan no ha realizado una compra en los últimos 40 días"*.
- **Panel de Usuario:** Un dashboard personalizado con el historial de todos los archivos cargados.

---

## 🛠️ Stack Tecnológico

- **Python:** El lenguaje de programación principal.
- **Streamlit:** Framework para la creación rápida de la interfaz web.
- **Pandas:** Biblioteca esencial para la manipulación y el análisis de datos.
- **Plotly:** Para la creación de gráficos dinámicos e interactivos.
- **Neon (Postgres):** Base de datos relacional para la persistencia de datos.

---

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para levantar el proyecto en tu entorno local:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/        AutoDashboard-de-Ventas
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configura las variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto y añade tu URL de conexión a la base de datos de Neon.
    ```
    DATABASE_URL="postgresql://[tu_usuario]:[tu_contraseña]@[tu_host]/[tu_db]?sslmode=require"
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

 ## 📸 Demo de la Aplicación

![Captura de pantalla o GIF del dashboard](assets/dashboard_demo.gif)
*[Reemplaza esta línea con una imagen o GIF del proyecto en funcionamiento]*

---

## 🤝 Contribuciones y Contacto

¡Este proyecto está en constante evolución! Si tienes ideas o sugerencias, no dudes en contactarme.

- **Autor:** Ignacio Pérez
- **LinkedIn:** [\[Enlace a tu perfil de LinkedIn\]](https://www.linkedin.com/in/ignacio-rafael-p%C3%A9rez-rodriguez-9b9304266/)
- **Correo Electrónico:** ignaciop9517@gmail.com
