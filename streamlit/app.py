import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Analiza delovno aktivnega prebivalstva in BDP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Title ---
st.title("Analiza delovno aktivnega prebivalstva in BDP Slovenije")

# --- Sidebar navigation ---
section = st.sidebar.radio(
    "Navigacija",
    ["Uvod", "Podatki", "Analiza", "Napoved"]
)

# --- Placeholder functions ---
def load_data():
    # TODO: naloži podatke iz PX/CSV
    return None

def preprocess_data(df):
    # TODO: predprocesiranje (datum, filtriranje)
    return df

# --- Sections ---
if section == "Uvod":
    st.header("Uvod")
    st.write(
        "Projekt analizira, kako demografski trendi in struktura BDP vplivajo na delovno aktivno prebivalstvo Slovenije. Uporabili smo odprte podatke o številu zaposlenih skozi čas ter letne komponente BDP, da odkrijemo časovne in regijske vzorce, učinke kriz (gospodarska kriza, COVID-19) ter pripravimo predhodne napovedi prihodnjih sprememb."
    )

elif section == "Podatki":
    st.header("Podatki")
    st.write(
        "V tej sekciji bomo naložili surove podatke in prikazali vzorec."
    )
    # data = load_data()
    # df = preprocess_data(data)
    st.info("Tu bo funkcija `load_data()` za uvoz PX/CSV datotek.")

elif section == "Analiza":
    st.header("Izvedena analiza")
    st.write(
        "Interaktivni grafi trendov zaposlenosti in BDP ter dodatna raziskovalna vprašanja."
    )
    # primer: st.line_chart(...)
    st.info("Sem bomo prikazali graf časovne serije, korelacijski diagram in sezonsko dekompozicijo.")

elif section == "Napoved":
    st.header("Napovedni model")
    st.write(
        "Uporabnik lahko izbere napovedni horizont in zažene preprost ARIMA/Prophet model."
    )
    # horizon = st.slider(...)
    # if st.button(...):
    #     show forecast
    st.info("Zavihek za drsnik in gumb za izračun napovedi.")

# --- Footer ---
st.markdown("---")
st.caption("Avtorji: Nika Demšar, Urška Frelih Uhelj, Anja Klančar, Eva Müller | Vir podatkov:  podatki.gov.si")
