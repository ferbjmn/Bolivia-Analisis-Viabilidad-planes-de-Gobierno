import streamlit as st
import pandas as pd

st.set_page_config(page_title="Viabilidad Económica – Planes de Gobierno 2025", layout="wide")

st.title("¿Quién es más viable económicamente? (visión de economista)")

# -------- Datos --------
data = [
    ["Rodrigo Paz (PDC)",            4.5, 4.0, 4.5, 4.0, 3.5, 4.0, 24.5,
     "Plan 50/50: regla déficit cero, congelar EP deficitarias; reformas amplias pero requiere pactos."],
    ["Manfred Reyes Villa (APB Súmate)", 4.0, 3.5, 3.5, 4.0, 3.0, 4.0, 22.0,
     "Recorte de ministerios, eliminar subsidio combustibles; fuerte ajuste, riesgo político alto."],
    ["Samuel Doria Medina (Alianza Unidad)", 3.5, 4.0, 3.5, 4.0, 3.0, 3.5, 21.5,
     "Ajuste integral + dólares vía multilaterales, 1M emprendimientos; depende de financiamiento externo."],
    ["Carlos E. del Castillo (MAS‑IPSP)", 2.0, 3.0, 2.0, 2.0, 2.5, 2.5, 14.0,
     "Continuismo social con pocos cambios estructurales; presión fiscal/subsidios sin fuente clara."]
]

cols = ["Candidato","Fiscal","Crec-Empleo","Institucionalidad","Productores","Justicia","Claridad",
        "Total","Lectura rápida"]
df = pd.DataFrame(data, columns=cols)

# -------- Tabla principal --------
st.subheader("Ranking (0–30 puntos)")
st.dataframe(df.style.format({"Total":"{:.1f}"}), use_container_width=True)

# Botón descargar
st.download_button("Descargar CSV", df.to_csv(index=False), "ranking_viabilidad.csv", "text/csv")

# -------- Detalle por candidato --------
st.markdown("---")
st.subheader("Detalle del análisis")

with st.expander("Rodrigo Paz Pereira – PDC"):
    st.markdown("""
**Fiscal:** Redistribución 50/50 con regla de déficit cero y congelar empresas públicas deficitarias.  
**Institucionalidad/Justicia:** Profesionalización estatal y reforma judicial meritocrática.  
**Productores/Comercio:** Liberalizar exportaciones y reordenar impuestos (nuevo orden tributario).  
**Riesgos:** Alto costo político para reconfigurar coparticipación; necesita gran consenso.
""")

with st.expander("Manfred Reyes Villa – APB Súmate"):
    st.markdown("""
**Fiscal:** Reducir ministerios de 17 a 14 (ahorro inmediato) y recortar propaganda.  
**Subsidios:** Eliminar subvención a combustibles tras transparentar costos.  
**Empresas públicas:** Privatización selectiva / cierre de deficitarias.  
**Riesgos:** Conflicto social por quitar subsidios y privatizaciones.
""")

with st.expander("Samuel Doria Medina – Alianza Unidad"):
    st.markdown("""
**100 días / ajuste macro:** Ajuste fiscal, controlar inflación y flexibilizar tipo de cambio (“devolver dólares”).  
**EP deficitarias:** Cierre / reestructuración con apoyo multilaterales (≈USD 3.500 MM).  
**Emprendimiento:** Meta 1 millón de emprendimientos + agencia nacional.  
**Energía/Transición:** 45% renovables 2030 y “Ley de Prosumidores”.  
**Riesgos:** Dependencia de financiamiento externo y tiempos cortos para estabilizar expectativas.
""")

with st.expander("Carlos Eduardo del Castillo – MAS‑IPSP"):
    st.markdown("""
**Social:** Mantener/incrementar subsidios y programas (bonos, SUS).  
**Empleo:** Programas específicos sin reforma estructural laboral.  
**Innovación:** Becas e innovación MIPYMES, sin metas fiscales claras.  
**Riesgos:** No aborda déficit/subsidios de base; continuidad con RIN bajas presiona sostenibilidad.
""")

st.caption("Escala: 0–5 por criterio. Total 0–30 (más alto = más viable). Evaluación cualitativa experta.")
