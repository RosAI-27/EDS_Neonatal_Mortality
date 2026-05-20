import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# ============================================
# CONFIGURATION DE LA PAGE
# ============================================
st.set_page_config(
    page_title="Prédiction Mortalité Néonatale",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS PERSONNALISÉ
# ============================================
custom_css = """
<style>
    /* Fond général */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Header */
    .header-container {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        text-align: center;
        color: white;
    }

    .header-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        font-weight: 300;
    }

    /* Cartes */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        border-left: 5px solid #2a5298;
        transition: transform 0.2s;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }

    .card-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e3c72;
        margin-bottom: 0.8rem;
    }

    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }

    /* Bouton prédire */
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3);
        transition: all 0.3s;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(238, 90, 36, 0.4);
        background: linear-gradient(90deg, #ee5a24 0%, #ff6b6b 100%);
    }

    /* Résultats */
    .result-high {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3);
        animation: pulse 2s infinite;
    }

    .result-low {
        background: linear-gradient(135deg, #26de81 0%, #20bf6b 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(32, 191, 107, 0.3);
    }

    @keyframes pulse {
        0% { box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3); }
        50% { box-shadow: 0 4px 25px rgba(238, 90, 36, 0.5); }
        100% { box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3); }
    }

    /* Métrique personnalisée */
    .metric-box {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #2a5298;
    }

    .metric-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.3rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
        color: #666;
        font-size: 0.85rem;
        border-top: 1px solid #eee;
    }

    /* Progress bar custom */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #26de81 0%, #ee5a24 50%, #ff6b6b 100%);
    }

    /* Info box */
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }

    /* Warning box */
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ============================================
# CHARGEMENT DU MODÈLE
# ============================================
@st.cache_resource
def load_model():
    return joblib.load('best_neonatal_model.pkl')

try:
    model = load_model()
    model_loaded = True
except Exception as e:
    st.error(f"❌ Erreur chargement modèle : {e}")
    model_loaded = False

# ============================================
# HEADER AVEC IMAGE
# ============================================

st.markdown("""
    <div class="header-container">
        <div class="header-title">🩺 Prédiction du Risque de Mortalité Néonatale</div>
        <div class="header-subtitle">EDS Cameroun 2018 — Modèle Machine Learning XGBoost</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# LAYOUT PRINCIPAL
# ============================================
col1, col2 = st.columns([1, 1.5])

# ============================================
# SIDEBAR / PANNEAU GAUCHE — INPUTS
# ============================================
with col1:
    st.markdown("<div class='card'><div class='card-title'>📋 Caractéristiques de la Mère</div></div>", 
                unsafe_allow_html=True)

    maternal_age = st.slider("Âge maternel (ans)", 15, 49, 25, 
                             help="Âge de la mère au moment de l'accouchement")

    parity = st.slider("Parité (nombre d'enfants)", 1, 15, 3,
                       help="Nombre total d'enfants nés de la mère")

    sex_child = st.selectbox("Sexe de l'enfant", 
                             ["Masculin", "Feminin"],
                             help="Le sexe masculin présente un risque légèrement supérieur")

    st.markdown("<div class='card'><div class='card-title'>🏠 Contexte Socio-économique</div></div>", 
                unsafe_allow_html=True)

    education = st.selectbox("Niveau d'éducation", 
                             ["Aucun", "Primaire", "Secondaire", "Superieur"])

    wealth = st.selectbox("Quintile de richesse", 
                          ["Poorest", "Poorer", "Middle", "Richer", "Richest"])

    residence = st.selectbox("Milieu de résidence", 
                             ["Urbain", "Rural"])

    region = st.selectbox("Région", 
                          ["Adamawa", "Centre", "Douala", "East", "Far-North",
                           "Littoral", "North", "North-West", "West", 
                           "South", "South-West", "Yaounde"])

    st.markdown("<div class='card'><div class='card-title'>👶 Caractéristiques de la Grossesse</div></div>", 
                unsafe_allow_html=True)

    baby_size = st.selectbox("Taille perçue du bébé", 
                             ["Tres gros", "Plus gros", "Normal", "Petit", "Tres petit"],
                             help="⚠️ 'Très petit' est le facteur de risque le plus important")

    birth_interval = st.selectbox("Intervalle inter-génésique", 
                                  ["Premiere", "<24 mois", "24-35 mois", ">=36 mois"],
                                  help="Intervalle depuis la naissance précédente")

    anc_visits = st.selectbox("Visites prénatales (ANC)", 
                              ["Aucune", "1-3", "4-7", "8+", "Missing"])

# ============================================
# PANNEAU DROIT — RÉSULTATS
# ============================================
with col2:
    st.markdown("<div class='card'><div class='card-title'>🔮 Prédiction du Risque</div></div>", 
                unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        💡 <b>Comment ça marche ?</b><br>
        Remplissez les caractéristiques à gauche, puis cliquez sur <b>"Analyser le Risque"</b>. 
        Le modèle XGBoost (AUC-ROC = 0,695) évalue la probabilité de décès néonatal.
    </div>
    """, unsafe_allow_html=True)

    # Bouton de prédiction
    predict_btn = st.button("🔍 Analyser le Risque", use_container_width=True)

    if predict_btn and model_loaded:
        # Création du dataframe d'input
        input_data = pd.DataFrame({
            'maternal_age': [maternal_age],
            'maternal_age_sq': [maternal_age ** 2],
            'parity': [parity],
            'sex_child': [sex_child],
            'education': [education],
            'wealth': [wealth],
            'residence': [residence],
            'region': [region],
            'baby_size': [baby_size],
            'birth_interval': [birth_interval],
            'anc_visits': [anc_visits]
        })

        # Prédiction
        prediction = int(model.predict(input_data)[0])
        probability = float(model.predict_proba(input_data)[0, 1])

        # Affichage résultat
        st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 1px solid #eee;'>", 
                    unsafe_allow_html=True)

        if prediction == 1:
            st.markdown(f"""
            <div class="result-high">
                ⚠️ RISQUE ÉLEVÉ DE MORTALITÉ NÉONATALE<br>
                <span style="font-size: 1rem; opacity: 0.9;">Surveillance immédiate recommandée</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-low">
                ✅ RISQUE FAIBLE DE MORTALITÉ NÉONATALE<br>
                <span style="font-size: 1rem; opacity: 0.9;">Surveillance standard suffisante</span>
            </div>
            """, unsafe_allow_html=True)

        # Métriques en colonnes
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{probability:.1%}</div>
                <div class="metric-label">Probabilité de décès</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            # CONVERSION EXPLICITE en float Python natif
            prob_float = float(probability)
            if prob_float > 0.5:
                risk_level = "🔴 ÉLEVÉ"
            elif prob_float > 0.3:
                risk_level = "🟠 MODÉRÉ"
            else:
                risk_level = "🟢 FAIBLE"
    
        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value" style="font-size: 1.2rem; padding-top: 0.5rem;">{risk_level}</div>
                <div class="metric-label">Niveau de risque</div>
            </div>
            """, unsafe_allow_html=True)
        

        with m3:
            # CONVERSION EXPLICITE en str Python natif
            baby_size_str = str(baby_size)
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{baby_size_str}</div>
                <div class="metric-label">Taille du bébé</div>
            </div>
            """, unsafe_allow_html=True)
    
        # Barre de progression
        st.markdown("<br>", unsafe_allow_html=True)
        st.progress(min(probability * 10, 1.0))
        st.caption("Échelle de risque relative (×10 pour lisibilité)")

        # Recommandations contextuelles
        if probability > 0.05:
            st.markdown("""
            <div class="warning-box">
                🚨 <b>Recommandations urgentes :</b><br>
                • Incubation / réanimation néonatale immédiate<br>
                • Monitorage cardiorespiratoire continu<br>
                • Bilan infectieux et glycémique rapide
            </div>
            """, unsafe_allow_html=True)
        elif baby_size == "Tres petit":
            st.markdown("""
            <div class="warning-box">
                ⚠️ <b>Attention particulière :</b><br>
                La taille "Très petit" est le facteur de risque le plus discriminant du modèle. 
                Malgré une probabilité modérée, une surveillance renforcée est conseillée.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-box">
                ✅ <b>Surveillance standard :</b><br>
                Aucun facteur de risque majeur identifié. Protocole de soins néonatals habituel.
            </div>
            """, unsafe_allow_html=True)

        # Facteurs de risque identifiés
        st.markdown("<div class='card'><div class='card-title'>📊 Facteurs de Risque Identifiés</div></div>", 
                    unsafe_allow_html=True)

        risk_factors = []
        if baby_size == "Tres petit":
            risk_factors.append(("🔴", "Taille très petite", "OR = 1,82"))
        if parity >= 6:
            risk_factors.append(("🟠", f"Parité élevée ({parity})", "Risque cumulatif"))
        if birth_interval == "<24 mois":
            risk_factors.append(("🟠", "Intervalle court <24 mois", "Taux : 4,7%"))
        if sex_child == "Masculin":
            risk_factors.append(("🟡", "Sexe masculin", "OR = 1,22"))
        if education == "Aucun":
            risk_factors.append(("🟡", "Aucune éducation", "Effet socio-économique"))
        if region in ["North", "Far-North", "Adamawa"]:
            risk_factors.append(("🟡", f"Région : {region}", "Contexte sanitaire"))

        if risk_factors:
            for emoji, factor, detail in risk_factors:
                st.markdown(f"""
                <div style="display: flex; align-items: center; padding: 0.5rem; 
                            background: white; border-radius: 8px; margin-bottom: 0.5rem;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">{emoji}</span>
                    <div>
                        <div style="font-weight: 600; color: #333;">{factor}</div>
                        <div style="font-size: 0.85rem; color: #666;">{detail}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Aucun facteur de risque majeur identifié dans ce profil.")

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    🏥 <b>EDS Cameroun 2018</b> — Modèle XGBoost entraîné sur 33 988 naissances<br>
    <i>Cet outil est destiné à l'aide à la décision médicale et ne remplace pas l'examen clinique.</i><br>
    Développé dans le cadre de l'analyse des facteurs de mortalité néonatale pour le cours de Statistique Multivariée Master 1 Data Science 2026 à l'université Saint Jean Ingénieur.
</div>
""", unsafe_allow_html=True)
