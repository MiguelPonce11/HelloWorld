import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, time
import time
import json
from pathlib import Path
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo



# Configuración de página (PRIMER comando siempre)
st.set_page_config(page_title="Mi App Completa", layout="wide")

# Presentación
st.title("Mi Primera App de Streamlit")
st.write("¡Bienvenido a mi primera aplicación con Streamlit!")
st.write("Soy Miguel Ponce Zertuche - A01383176.")
st.write("Tengo novia y es Arantza Sofía Aguirre de la Fuente.")
st.write("Soy de Saltillo, Coahuila.")
st.write("Recuerda: lo importante es practicar y explorar.")

# Expander
with st.expander("¿De qué trata esta app?"):
    st.write("Esta aplicación demuestra múltiples widgets de Streamlit, así como su organización en pantalla.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)

# Botones interactivos
st.title("App con 3 botones interactivos")
st.write("Presiona cada botón para ver un mensaje diferente.")

if st.button("Botón 1: Frase de reflexión"):
    st.write("La vida no se trata de encontrarse a uno mismo, sino de crearse a uno mismo.")
else:
    st.write("Botón 1: ADIOS")

if st.button("Botón 2: Dato curioso"):
    st.write("Los pulpos tienen tres corazones y sangre azul.")
else:
    st.write("Botón 2: ADIOS")

if st.button("Botón 3: Recordatorio amable"):
    st.write("Tómate un momento para respirar y agradecer el presente.")
else:
    st.write("Botón 3: ADIOS")

# Sección de datos y gráficos
st.title("Uso de st.write con datos")
df = pd.DataFrame({
    'Nombre': ['Miguel', 'Arantza', 'Luis', 'Ana'],
    'Edad': [23, 22, 25, 21],
    'Ciudad': ['Saltillo', 'CDMX', 'Monterrey', 'Guadalajara']
})
st.write("Tabla con mis datos personalizados:")
st.write(df)

df_chart = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
chart = alt.Chart(df_chart).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write("Gráfico de dispersión generado aleatoriamente:")
st.write(chart)

# Sliders personalizados
st.title("Interacción con Sliders")
st.subheader("Edad")
edad = st.slider("¿Cuántos años tienes?", 0, 100, 21)
st.write("Edad seleccionada:", edad)

st.subheader("Nivel de satisfacción")
satisfaccion = st.slider("Califica tu satisfacción con esta app (0-10)", 0, 10, (3, 8))
st.write("Rango de satisfacción:", satisfaccion)

st.subheader("Inicio de proyecto")
inicio = st.slider("¿Cuándo comienzas tu nuevo proyecto?", value=datetime(2024, 8, 1, 9, 0),
                   format="MM/DD/YY - hh:mm")
st.write("Comienzas el:", inicio)

# Gráficos de línea
st.title("Visualización con Gráficos de Línea")
st.line_chart(pd.DataFrame({
    'Q1': [150], 'Q2': [200], 'Q3': [170], 'Q4': [220]
}).T.rename(columns={0: "Ventas (k USD)"}))

st.line_chart(pd.DataFrame({
    'Ene': [12.1], 'Feb': [13.5], 'Mar': [15.2], 'Abr': [18.0], 'May': [22.3], 'Jun': [25.6]
}).T.rename(columns={0: "Temperatura (°C)"}))

st.line_chart(pd.DataFrame({
    'Lun': [120], 'Mar': [135], 'Mié': [150], 'Jue': [160], 'Vie': [180], 'Sáb': [200], 'Dom': [140]
}).T.rename(columns={0: "Usuarios activos"}))

# Checkboxes
st.title("Selección de acciones con Checkboxes")
opciones = {
    "Enviar correos pendientes": "✔ Correos pendientes registrados.",
    "Revisar órdenes vencidas": "✔ Órdenes vencidas en proceso de revisión.",
    "Actualizar el tablero Kanban": "✔ El tablero Kanban ha sido actualizado.",
    "Escalar materiales críticos a XPAC": "✔ Escalada de materiales críticos realizada.",
    "Hacer seguimiento a facturas sin GRC": "✔ Seguimiento a facturas sin GRC en curso."
}
for label, resultado in opciones.items():
    if st.checkbox(label):
        st.write(resultado)

# File uploader (dos archivos)
st.title("Carga de Archivos: Marvel y Overwatch")
for nombre, key in [("MarvelUniverse.csv", "marvel"), ("Overwatch_edopic.csv", "overwatch")]:
    st.subheader(f"Subir archivo: {nombre}")
    archivo = st.file_uploader(f"Selecciona el archivo '{nombre}'", type=["csv"], key=key)
    if archivo is not None:
        df_arch = pd.read_csv(archivo)
        st.success(f"Archivo {nombre} cargado correctamente.")
        st.write("Vista previa:")
        st.write(df_arch.head())
        st.write("Estadísticas:")
        st.write(df_arch.describe(include='all'))
    else:
        st.info(f"Esperando archivo '{nombre}'...")

# Columnas layout
st.header("Distribución con columnas")
st.sidebar.header("Input")
user_name = st.sidebar.text_input("¿Cuál es tu nombre?")
user_emoji = st.sidebar.selectbox("Elige un emoji", ["", "😀", "😁", "😎", "🥳", "😢"])
user_food = st.sidebar.selectbox("¿Cuál es tu comida favorita?", ["", "Tacos", "Pizza", "Hamburguesa", "Lasagna", "Burrito"])

col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"👋 Hola **{user_name}**" if user_name else "📝 Por favor escribe tu nombre")
with col2:
    st.write(f"Tu emoji favorito es {user_emoji}" if user_emoji else "🔎 Elige un emoji")
with col3:
    st.write(f"Tu comida favorita es **{user_food}**" if user_food else "🍽️ Selecciona tu comida favorita")

# Paso 15: Barras de progreso a diferente velocidad
st.title("Simulación con 3 barras de progreso a diferente velocidad")
st.write("Esta sección muestra cómo tres barras de progreso avanzan a velocidades distintas.")
bar1 = st.progress(0, text="Velocidad rápida (x2)")
bar2 = st.progress(0, text="Velocidad media (x1)")
bar3 = st.progress(0, text="Velocidad lenta (x0.5)")

prog1 = prog2 = prog3 = 0
for i in range(101):
    if prog1 <= 100:
        bar1.progress(prog1, text=f"Rápida: {prog1}%")
        prog1 += 2
    if prog2 <= 100:
        bar2.progress(prog2, text=f"Media: {prog2}%")
        prog2 += 1
    if i % 2 == 0 and prog3 <= 100:
        bar3.progress(prog3, text=f"Lenta: {prog3}%")
        prog3 += 1
    time.sleep(0.05)

st.success("¡Todas las barras han llegado al 100%!")
st.balloons()

# Formulario
st.title("Encuesta con Formulario (st.form)")
with st.form("encuesta_10_preguntas"):
    st.subheader("Responde estas preguntas:")
    p1 = st.selectbox("1. ¿Color favorito?", ["Rojo", "Azul", "Verde", "Amarillo"])
    p2 = st.selectbox("2. ¿Bebida favorita?", ["Café", "Té", "Jugo", "Agua"])
    p3 = st.selectbox("3. ¿Pasatiempo?", ["Leer", "Música", "Ejercicio", "Ver películas"])
    p4 = st.selectbox("4. ¿Ciudad favorita?", ["CDMX", "Monterrey", "Guadalajara", "Cancún"])
    p5 = st.slider("5. ¿Edad?", 10, 70, 25)
    p6 = st.slider("6. ¿Horas de estudio diario?", 0, 12, 2)
    p7 = st.checkbox("7. ¿Te gusta Python?")
    p8 = st.radio("8. ¿Trabajas actualmente?", ["Sí", "No"])
    p9 = st.multiselect("9. ¿Qué apps usas?", ["WhatsApp", "Instagram", "TikTok", "Gmail"])
    p10 = st.date_input("10. ¿Fecha de inicio del semestre?")
    submitted = st.form_submit_button("Enviar encuesta")
    if submitted:
        st.success("¡Gracias por completar la encuesta!")


# Sidebar informativo
with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Día 27 - Streamlit Elements")
    st.write("Panel arrastrable con editor, gráfica y reproductores de video.")
    st.write("---")
    video_1 = st.text_input("🎥 Video 1 URL", value="https://www.youtube.com/watch?v=schtk917iRU")
    video_2 = st.text_input("🎥 Video 2 URL", value="https://www.youtube.com/watch?v=aKR-7k-AZQ4")

# Datos de ejemplo
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Layout del dashboard (3 filas, 4 tarjetas)
layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
    dashboard.Item("media1", 0, 3, 6, 3),
    dashboard.Item("media2", 6, 3, 6, 3),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Editor de código (JSON)
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="📝 Editor JSON", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                mui.Button("Aplicar cambios", onClick=sync())

        # Gráfico tipo Bump con Nivo
        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="📊 Gráfico de Posiciones", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={ "tickSize": 5, "tickPadding": 5, "tickRotation": 0 },
                    axisBottom={ "tickSize": 5, "tickPadding": 5, "tickRotation": 0 },
                    axisLeft={ "tickSize": 5, "tickPadding": 5, "tickRotation": 0, "legend": "ranking", "legendPosition": "middle", "legendOffset": -40 },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # Reproductor de Video 1
        with mui.Card(key="media1", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="🎬 Video 1", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=video_1, width="100%", height="100%", controls=True)

        # Reproductor de Video 2
        with mui.Card(key="media2", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="🎬 Video 2", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=video_2, width="100%", height="100%", controls=True)