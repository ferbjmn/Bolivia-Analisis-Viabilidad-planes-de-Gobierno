import streamlit as st
import pandas as pd

st.set_page_config(page_title="Viabilidad Económica – Planes de Gobierno 2025", layout="wide")

# ------------------ Datos ------------------
cols = ["Candidato","Fiscal","Crec-Empleo","Institucionalidad","Productores","Justicia","Claridad","Total","Lectura rápida"]
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
df = pd.DataFrame(data, columns=cols)

conclusiones = {
    "Rodrigo Paz (PDC)": (
        "Combina regla fiscal estricta y redistribución 50/50 para corregir el centralismo. "
        "Congela EP deficitarias y digitaliza compras públicas (blockchain), mejorando eficiencia y transparencia. "
        "El riesgo central es político: sin pactos amplios, las reformas pueden frenarse. "
        "Si se aprueban, el crecimiento y el empleo formal se consolidan gradualmente con deuda más sostenible."
    ),
    "Manfred Reyes Villa (APB Súmate)": (
        "Ajuste fiscal rápido: menos ministerios, fin de subsidios a combustibles y cierre/privatización de EP deficitarias. "
        "Esto mejora el déficit en el corto plazo, pero puede generar conflicto social si no hay compensaciones. "
        "Faltan detalles de financiamiento y de gestión del conflicto. Viable en números, frágil en gobernabilidad."
    ),
    "Samuel Doria Medina (Alianza Unidad)": (
        "Propone un ‘rescate’ macro en 100 días con dólares externos y cambio de expectativas, junto con una gran apuesta al emprendimiento y la transición energética. "
        "Es coherente, pero depende de financiamiento multilateral y de una ejecución muy fina. "
        "Si la fase inicial falla, pierde credibilidad; si funciona, impulsa PIB y empleo de forma relevante."
    ),
    "Carlos E. del Castillo (MAS‑IPSP)": (
        "Mantiene subsidios y programas sociales sin reformas estructurales profundas. "
        "Protege ingresos de corto plazo pero presiona déficit y deuda en un contexto de RIN bajas. "
        "Las medidas productivas son positivas pero poco cuantificadas. Sin reformar subsidios y el aparato estatal, la sostenibilidad depende de mejores precios externos o más deuda."
    )
}

# ------------------ UI ------------------
st.title("¿Quién es más viable económicamente? (visión de economista)")

with st.expander("Glosario"):
    st.markdown("""
**EP:** Empresa Pública (empresa estatal).  
**Déficit fiscal:** Cuando el Estado gasta más de lo que ingresa en un año.  
**RIN:** Reservas Internacionales Netas (dólares del Banco Central).  
""")

st.subheader("Ranking (0–30 puntos)")
st.dataframe(df.style.format({"Total": "{:.1f}"}), use_container_width=True)

st.download_button(
    "Descargar CSV",
    df.to_csv(index=False),
    "ranking_viabilidad.csv",
    "text/csv"
)

st.markdown("---")
st.subheader("Detalle del análisis y conclusiones")

for cand in df["Candidato"]:
    with st.expander(cand):
        # texto corto de la tabla
        resumen = df[df["Candidato"] == cand]["Lectura rápida"].iloc[0]
        st.markdown(f"**Lectura rápida:** {resumen}")
        # conclusión elaborada
        st.markdown(f"**Conclusión (analista económico):** {conclusiones[cand]}")

st.caption("Criterios (0–5): Sostenibilidad fiscal, Crecimiento & empleo, Institucionalidad/anticorrupción, Clima para productores, Justicia/seguridad jurídica, Claridad & ejecutabilidad. Total máx. 30.")
