import streamlit as st
import pandas as pd

st.set_page_config(page_title="Viabilidad Económica – Planes de Gobierno 2025", layout="wide")

# ------------------ Datos base ------------------
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

# ------------------ Conclusiones largas ------------------
conclusiones = {
    "Rodrigo Paz (PDC)": (
        "Su propuesta combina regla fiscal estricta (déficit cero) y redistribución 50/50 que corrige el centralismo "
        "y puede mejorar la asignación del gasto. La secuencia de reformas (congelar EP deficitarias, nuevo orden "
        "tributario, digitalizar compras con blockchain) apunta a eficiencia y transparencia, lo que reduce riesgo país "
        "y puede “crowdear” inversión privada. El costo: alto capital político; sin pactos amplios, la reforma fiscal y "
        "judicial puede trabarse o diluirse. Si logra aprobar el paquete, el impacto en crecimiento y empleo formal sería "
        "gradual pero sostenido, con mejor sostenibilidad de deuda."
    ),
    "Manfred Reyes Villa (APB Súmate)": (
        "Plantea un ajuste rápido y visible: menos ministerios, recortes a propaganda, eliminación de subsidios a combustibles "
        "y cierre/privatización de EP deficitarias. Fiscalmente es eficaz a corto plazo, pero el shock puede contraer demanda si "
        "no se acompaña de medidas compensatorias. El plan carece de un mapa claro de financiamiento y gestión del conflicto social "
        "que inevitablemente generarán estas medidas. Si supera esa barrera, podría estabilizar cuentas; si no, corre riesgo de "
        "ingobernabilidad y reversión de reformas."
    ),
    "Samuel Doria Medina (Alianza Unidad)": (
        "Propone un “rescate” macro en 100 días basado en dólares externos y cambio de expectativas, junto a una agenda pro‑emprendimiento "
        "(1M emprendimientos) y transición energética. Económicamente es coherente: estabilizar primero, luego dinamizar. Pero depende de "
        "financiamiento multilateral significativo, capacidad administrativa para ejecutar rápido y un plan operativo detallado para la meta "
        "de emprendimientos. Si consigue los recursos y coordina bien, el efecto sobre PIB y empleo puede ser notable; si falla en la fase inicial, "
        "pierde credibilidad y margen fiscal."
    ),
    "Carlos E. del Castillo (MAS‑IPSP)": (
        "El enfoque es de continuidad social: mantener/expandir subsidios y programas con escaso ajuste estructural. Esto protege el ingreso de "
        "corto plazo, pero tensiona la sostenibilidad fiscal en un contexto de RIN bajas y déficit persistente. Las medidas productivas (becas, MIPYMES) "
        "son positivas pero poco cuantificadas; no compensan la carga de subsidios ni diversifican la matriz productiva rápidamente. En ausencia de una "
        "reforma al régimen de subsidios y al aparato estatal, el modelo depende de un shock externo positivo (commodities) o mayor endeudamiento."
    ),
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
        resumen = df.loc[df["Candidato"] == cand, "Lectura rápida"].iloc[0]
        st.markdown(f"**Lectura rápida:** {resumen}")
        st.markdown(f"**Conclusión (analista económico):** {conclusiones[cand]}")

st.caption(
    "Criterios (0–5): Sostenibilidad fiscal, Crecimiento & empleo, Institucionalidad/anticorrupción, "
    "Clima para productores, Justicia/seguridad jurídica, Claridad & ejecutabilidad. Total máx. 30."
)
