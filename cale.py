import streamlit as st
from streamlit_calendar import calendar

# 👇 usar wide para permitir más espacio
st.set_page_config(layout="wide")

st.title("📅 Calendario Gobierno TI")

# -----------------------------
# 🎨 ESTILOS (CLAVE)
# -----------------------------
st.markdown("""
<style>

/* Centrar el calendario */
.block-container {
    max-width: 1050px;
    margin: auto;
}

/* Aumentar tamaño general */
.fc {
    font-size: 14px !important;
}

/* Título del mes */
.fc-toolbar-title {
    font-size: 20px !important;
}

/* Aumentar altura de cada celda */
.fc-daygrid-day {
    min-height: 120px !important;
}

/* 🔥 MOSTRAR TEXTO COMPLETO (IMPORTANTE) */
.fc-daygrid-event {
    white-space: normal !important;
    overflow: visible !important;
}

/* 🔥 Permitir múltiples líneas en eventos */
.fc-daygrid-event {
    white-space: normal !important;
    overflow: visible !important;
    display: block !important;
}

/* Evitar que corte con "..." */
.fc-event-title {
    white-space: normal !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 📌 EVENTOS
# -----------------------------
eventos = [
    {"title": "Registro esfuerzos", "start": "2026-05-04","color": "#23B9FF"},
    {"title": "Registro esfuerzos", "start": "2026-05-05","color": "#23B9FF"},
    {"title": "Registro esfuerzos", "start": "2026-05-06","color": "#23B9FF"},
    {"title": "Conciliación y glosas", "start": "2026-05-07","color": "#0695D6"},
    {"title": "Envío de facturas", "start": "2026-05-08","color": "#1A1FA7"},
    {"title": "Envío de facturas", "start": "2026-05-11","color": "#1A1FA7"},
    {"title": "Procesamiento FAC", "start": "2026-05-12","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-13","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-14","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-15","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-18","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-19","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-20","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-21","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-22","color": "#525053"},
    {"title": "Procesamiento FAC", "start": "2026-05-25","color": "#525053"},
]

# -----------------------------
# 📆 CONFIGURACIÓN
# -----------------------------
calendar_options = {
    "initialView": "dayGridMonth",
    "initialDate": "2026-05-01",
    "height": 650,  # 👈 más alto
    "contentHeight": 600,
    "editable": False,
    "selectable": False,
    "dayMaxEventRows": False,  # 👈 muestra todos los eventos
    "headerToolbar": {
        "left": "",
        "center": "title",
        "right": ""
    }
}

# -----------------------------
# 🎨 CALENDARIO
# -----------------------------
calendar(events=eventos, options=calendar_options)
