import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viabilidad Económica – Planes de Gobierno 2025", layout="wide")

# ------------------------------------------------------
# 1. DATOS BASE DEL RANKING
# ------------------------------------------------------
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

# ------------------------------------------------------
# 2. CONCLUSIONES LARGAS
# ------------------------------------------------------
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

# ------------------------------------------------------
# 3. RESUMEN ESTRUCTURADO (TABLAS POR CANDIDATO)
# ------------------------------------------------------
resumen_cols = [
    "Candidato","Eje","Propuesta / Acción","Instrumento sugerido",
    "Horizonte","Objetivo declarado","Observaciones (claridad/viabilidad)"
]

resumen_rows = [
    # Samuel Doria Medina
    ["Samuel Doria Medina","Macroeconomía / Cambiario",
     "“Devolver los dólares al país” y cambiar expectativas sobre el dólar",
     "Plan de 100 días con apoyo internacional","100 días iniciales",
     "Normalizar oferta de divisas y combustibles",
     "Falta detalle del mecanismo concreto (incentivos, control, deuda, acuerdos)."],
    ["Samuel Doria Medina","Reforma política",
     "Eliminar la reelección en todas sus formas mediante referendo",
     "Reforma constitucional vía referendo","Corto plazo (posreferendo)",
     "Estabilidad política y evitar “apropiación del Estado”",
     "Requiere pactos políticos y viabilidad legal/procedimental."],
    ["Samuel Doria Medina","Descentralización fiscal",
     "Autonomías económicas; coparticipación equitativa entre gobernaciones y gobierno central",
     "Cambios en régimen de coparticipación","Mediano plazo",
     "Mayor autonomía y eficiencia en gasto",
     "Debe definirse fórmula de reparto e impactos fiscales."],
    ["Samuel Doria Medina","Medio ambiente",
     "“Mano dura” contra incendiarios y contaminadores (mercurio)",
     "Fiscalización y sanciones penales/administrativas","Continuo",
     "Reducir incendios y contaminación",
     "Necesita institucionalidad y recursos de control; no define incentivos positivos."],
    ["Samuel Doria Medina","Modelo productivo",
     "Nuevo modelo basado en economía privada",
     "Reformas regulatorias / clima de inversión","Largo plazo",
     "Dinamizar inversión privada",
     "Concepto amplio; falta detalle sectorial."],
    ["Samuel Doria Medina","Emprendimiento / empleo",
     "1 millón de nuevos emprendimientos en 5 años",
     "Programas de apoyo, financiamiento, simplificación","5 años",
     "Generar empleo y dinamizar economía",
     "Número ambicioso; requiere plan operativo y financiamiento."],
    ["Samuel Doria Medina","Cultura política",
     "Presidente que “resuelva problemas” y se retire tras 5 años",
     "Cambio cultural + reglas de reelección","5 años de gestión",
     "Gestión pragmática, no caudillismo",
     "Declaración de principios; medir impacto es difícil."],

    # Manfred Reyes Villa
    ["Manfred A. A. Reyes Villa (APB – Súmate)","Empleo / Formalización",
     "Incentivos económicos, subsidio a aportes sociales, trabajo por hora/teletrabajo; programa universal de cuidado infantil",
     "Leyes y programas de apoyo directo a MIPYMES y familias","Corto–mediano plazo",
     "Aumentar empleo formal y participación de mujeres/jóvenes",
     "Requiere financiamiento sostenido y ajustes normativos laborales."],
    ["Manfred A. A. Reyes Villa (APB – Súmate)","Salud pública",
     "Reestructurar el Ministerio de Salud con nuevos viceministerios según perfil epidemiológico",
     "Reingeniería institucional del ministerio","Mediano plazo",
     "Mejorar eficiencia y resiliencia del sistema de salud",
     "Cambios orgánicos complejos; depende de reformas administrativas."],
    ["Manfred A. A. Reyes Villa (APB – Súmate)","Seguridad / Orden público",
     "Guardias autonómicas, sanciones agravadas a avasallamientos, sistema inteligente de seguridad ciudadana",
     "Reformas legales y creación de sistemas integrados de seguridad","Continuo",
     "Restablecer Estado de Derecho y protección de propiedad",
     "Alto requerimiento de coordinación multi-nivel y recursos."],
    ["Manfred A. A. Reyes Villa (APB – Súmate)","Paradiplomacia / Desarrollo regional",
     "Transferir competencia de paradiplomacia a gobiernos departamentales; crear marco jurídico y estratégico",
     "Ley/es marco y coordinación intergubernamental","Mediano plazo",
     "Potenciar inserción internacional y diversificar alianzas",
     "Riesgo de conflicto competencial con Cancillería."],
    ["Manfred A. A. Reyes Villa (APB – Súmate)","Gobierno digital / Burocracia",
     "Plataforma “YoGobierno”, identificaciones digitales, e-Gobierno, uso de software libre",
     "Transformación digital y normativa TIC","Progresivo",
     "Reducir burocracia y aumentar participación ciudadana",
     "Exige inversión tecnológica e interoperabilidad real."],

    # Rodrigo Paz Pereira
    ["Rodrigo Paz Pereira (PDC)","Economía / Modelo 50/50",
     "Recomponer precios de combustibles, liberalizar exportaciones, nuevo orden tributario",
     "Reformas fiscales y legales (nuevo marco tributario)","Mediano plazo",
     "Reducir desbalances fiscales y dinamizar economía",
     "Claridad alta; falta cronograma e impactos cuantificados."],
    ["Rodrigo Paz Pereira (PDC)","Institucionalidad del Estado",
     "Profesionalización y digitalización de la AP; nuevo sistema de administración y control",
     "Leyes de carrera pública y modernización normativa","Mediano plazo",
     "Estado eficiente y meritocrático",
     "Requiere consenso político amplio."],
    ["Rodrigo Paz Pereira (PDC)","Justicia",
     "Comisión de Reforma Judicial meritocrática; digitalización de la justicia",
     "Comisión especial + reformas legales/procesales","Mediano plazo",
     "Reconfigurar sistema judicial y reducir impunidad",
     "Instrumentos claros, sin plazos específicos."],
    ["Rodrigo Paz Pereira (PDC)","Educación (calidad internacional)",
     "Currícula con estándares internacionales, sistema trilingüe, ISO 21001, digitalización",
     "Reformas curriculares y acreditación","≈5 años",
     "Elevar calidad educativa y vincularla al sector productivo",
     "Metas claras; falta presupuesto estimado."],
    ["Rodrigo Paz Pereira (PDC)","Salud",
     "Mejorar acceso a salud de calidad bajo Agenda 50/50",
     "Programas y reasignación fiscal","Mediano plazo",
     "Cobertura y calidad en salud",
     "Detalle operativo limitado."],

    # Carlos E. del Castillo
    ["Carlos E. del Castillo (MAS–IPSP)","Lucha contra pobreza y desigualdad",
     "Mantener e incrementar acceso a educación, salud, vivienda, subsidios y seguridad social",
     "Continuidad y ampliación de políticas sociales existentes","Continuo",
     "Reducir exclusión y desigualdad",
     "Enfoque amplio; pocos detalles operativos nuevos."],
    ["Carlos E. del Castillo (MAS–IPSP)","Ciencia, tecnología e innovación",
     "Becas de posgrado, retorno de talento, innovación en MIPYMES, redes científicas",
     "Programas de becas, fondos de innovación y redes","Mediano plazo",
     "Fortalecer capacidades científicas y tecnológicas",
     "Instrumentos listados, sin metas de inversión (% PIB)."],
    ["Carlos E. del Castillo (MAS–IPSP)","Educación (quinquenio de calidad)",
     "Elevar logros de aprendizaje en 5 años; reforma de planificación/evaluación; ampliar Bono Juancito Pinto",
     "Reformas educativas y ajustes presupuestarios","5 años",
     "Mejorar calidad y equidad educativa",
     "Define plazo (5 años); requiere recursos y gestión."]
]

df_resumen = pd.DataFrame(resumen_rows, columns=resumen_cols)

# ------------------------------------------------------
# 4. HELPERS DE ESTILO
# ------------------------------------------------------
def preparar_ranking(df_in):
    df_rank = df_in.copy()
    df_rank["Rank"] = df_rank["Total"].rank(ascending=False, method="min").astype(int)
    df_rank["% del máximo"] = (df_rank["Total"] / df_rank["Total"].max() * 100).round(1)
    df_rank = df_rank.sort_values("Total", ascending=False)[
        ["Rank","Candidato","Total","% del máximo","Fiscal","Crec-Empleo",
         "Institucionalidad","Productores","Justicia","Claridad","Lectura rápida"]
    ]
    return df_rank

def estilo_ranking(df_rank):
    cmap = "Greens"
    sty = (df_rank.style
           .hide(axis="index")
           .format({"Total":"{:.1f}","% del máximo":"{:.1f}%"})
           .bar(subset=["Total"], color="#4CAF50", vmin=0, vmax=df_rank["Total"].max())
           .background_gradient(subset=["Fiscal","Crec-Empleo","Institucionalidad",
                                        "Productores","Justicia","Claridad"],
                                cmap=cmap, vmin=0, vmax=5)
           .set_table_styles([
               {"selector":"th","props":"background-color:#f0f2f6; text-align:center;"},
               {"selector":"td","props":"text-align:center; font-size:14px;"},
           ])
          )
    return sty

def estilo_resumen(df_in):
    return (df_in.style.hide(axis="index")
                 .set_table_styles([
                     {"selector":"th","props":"background-color:#f0f2f6; text-align:center;"},
                     {"selector":"td","props":"text-align:left; font-size:13px; vertical-align:top;"},
                 ]))

# ------------------------------------------------------
# 5. UI
# ------------------------------------------------------
st.title("¿Quién es más viable económicamente? (visión de economista)")

with st.expander("Glosario"):
    st.markdown("""
**EP:** Empresa Pública (empresa estatal).  
**Déficit fiscal:** Cuando el Estado gasta más de lo que ingresa en un año.  
**RIN:** Reservas Internacionales Netas (dólares del Banco Central).  
""")

# Ranking
st.subheader("Ranking (0–30 puntos)")
df_rank = preparar_ranking(df)
st.write(estilo_ranking(df_rank))

st.download_button(
    "Descargar CSV (ranking)",
    df_rank.to_csv(index=False),
    "ranking_viabilidad.csv",
    "text/csv"
)

# Métricas rápidas Top 3
st.markdown("### Top 3")
top3 = df_rank.head(3)
cols_m = st.columns(len(top3))
for col, (_, row) in zip(cols_m, top3.iterrows()):
    with col:
        st.metric(label=row["Candidato"], value=f"{row['Total']:.1f}/30", delta=f"Rank {row['Rank']}")

# Conclusiones
st.markdown("---")
st.subheader("Detalle del análisis y conclusiones")
for cand in df["Candidato"]:
    with st.expander(cand):
        resumen = df.loc[df["Candidato"] == cand, "Lectura rápida"].iloc[0]
        st.markdown(f"**Lectura rápida:** {resumen}")
        st.markdown(f"**Conclusión (analista económico):** {conclusiones[cand]}")

# Resumen estructurado por candidato
st.markdown("---")
st.subheader("Resumen estructurado de propuestas (por candidato)")

tabs = st.tabs(df_resumen["Candidato"].unique().tolist())
for tab, cand in zip(tabs, df_resumen["Candidato"].unique().tolist()):
    with tab:
        sub = df_resumen[df_resumen["Candidato"] == cand].copy()
        st.dataframe(estilo_resumen(sub), use_container_width=True)
        st.download_button(
            f"Descargar CSV – {cand}",
            sub.to_csv(index=False),
            file_name=f"resumen_{cand.replace(' ','_')}.csv",
            mime="text/csv"
        )

st.caption(
    "Criterios (0–5): Sostenibilidad fiscal, Crecimiento & empleo, Institucionalidad/anticorrupción, "
    "Clima para productores, Justicia/seguridad jurídica, Claridad & ejecutabilidad. Total máx. 30."
)
