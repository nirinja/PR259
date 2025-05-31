import streamlit as st
import pandas as pd
import os


@st.cache(allow_output_mutation=True)
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "koda", "podatki")

    # 1) Naloži „delo.csv“ in pretvori MESEC → YEAR, DATE
    path_delo = os.path.join(DATA_DIR, "delo.csv")
    df_delo = pd.read_csv(path_delo, sep=";", encoding="utf-8")
    # Pretvorba "2010M01" → "2010-01"
    df_delo["MESEC"] = df_delo["MESEC"].str.replace("M", "-", regex=False)
    df_delo["YEAR"] = df_delo["MESEC"].str[:4].astype(int)
    df_delo["DATA"] = pd.to_numeric(df_delo["DATA"], errors="coerce")
    df_delo = df_delo[df_delo["YEAR"] != df_delo["YEAR"].max()]
    df_delo["date"] = pd.to_datetime(df_delo["MESEC"] + "-01", format="%Y-%m-%d")

    # Podmnožica samo “SLOVENIJA”
    if "STATISTIČNA REGIJA" in df_delo.columns:
        data_slovenia = df_delo[df_delo["STATISTIČNA REGIJA"] == "SLOVENIJA"].copy()
    else:
        data_slovenia = pd.DataFrame()

    # 2) Naloži „bdp.csv“ in pretvori YEAR/CKVARTER → DATE
    path_bdp = os.path.join(DATA_DIR, "bdp.csv")
    df_bdp = pd.read_csv(path_bdp, sep=";", encoding="utf-8")
    df_bdp["DATA"] = pd.to_numeric(df_bdp["DATA"], errors="coerce")
    df_bdp["LETO"] = df_bdp["LETO"].astype(int)
    df_bpd = df_bdp[df_bdp["LETO"] != df_bdp["LETO"].max()]
    if "CKVARTER" in df_bdp.columns:
        df_bdp["date"] = pd.to_datetime(
            df_bdp["LETO"].astype(str) + "-" +
            ((df_bdp["CKVARTER"] - 1) * 3 + 1).astype(int).astype(str).str.zfill(2) +
            "-01",
            format="%Y-%m-%d"
        )
    else:
        df_bdp["date"] = pd.to_datetime(df_bdp["LETO"].astype(str) + "-01-01", format="%Y-%m-%d")

    # 3) (Po želji) Prebivalstvo
    path_preb = os.path.join(DATA_DIR, "prebivalstvo.csv")
    if os.path.exists(path_preb):
        df_preb = pd.read_csv(path_preb, sep=";", encoding="utf-8")
        df_preb["DATA"] = pd.to_numeric(df_preb["DATA"], errors="coerce")
        df_preb["LETO"] = df_preb["LETO"].astype(int)
        df_preb = df_preb[df_preb["LETO"] != df_preb["LETO"].max()]
        df_preb["date"] = pd.to_datetime(df_preb["LETO"].astype(str) + "-01-01", format="%Y-%m-%d")
    else:
        df_preb = pd.DataFrame()

    return df_delo, data_slovenia, df_bdp, df_preb

st.set_page_config(
    page_title="Analiza delovno aktivnega prebivalstva in BDP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Analiza delovno aktivnega prebivalstva in BDP Slovenije")

df_delo, data_slovenia, df_bdp, df_preb = load_data()

# Sidebar navigacija
section = st.sidebar.radio(
    "Navigacija",
    ["Uvod", "Podatki", "Analiza", "Napoved"]
)

if section == "Uvod":
    st.header("Uvod")
    st.write(
        "Projekt analizira, kako demografski trendi in struktura BDP vplivajo "
        "na delovno aktivno prebivalstvo Slovenije. Uporabili smo odprte podatke "
        "o številu zaposlenih skozi čas ter letne komponente BDP, da odkrijemo "
        "časovne in regijske vzorce, učinke kriz (gospodarska kriza, COVID-19) "
        "ter pripravimo predhodne napovedi prihodnjih sprememb."
    )

elif section == "Podatki":
    st.header("Podatki")
    st.header("!!TUKI NEVEM KAJ BI DODALA, RECIMO PRESTAVITEV PODATKOV AL NEKI? LOH MAMO PA TUT SAM ANALIZA PA NAPOVED TAB-E!!")


elif section == "Analiza":
    st.header("Izvedena analiza")

    if not data_slovenia.empty:
        monthly_total = data_slovenia.groupby("MESEC")["DATA"].sum().reset_index()

        monthly_total["date"] = pd.to_datetime(monthly_total["MESEC"] + "-01", format="%Y-%m-%d")
        monthly_total["YEAR"] = monthly_total["date"].dt.year

        #Izračunamo letno povprečje 12 mesečnih vrednosti
        yearly_avg = (
            monthly_total.groupby("YEAR")["DATA"]
            .mean()
            .reset_index()
            .sort_values("YEAR")
        )

        #Interaktivni drsnik za obdobje
        leto_min = int(yearly_avg["YEAR"].min())
        leto_max = int(yearly_avg["YEAR"].max())
        izberimo_obdobje = st.slider(
            "Izberi obdobje let:", min_value=leto_min, max_value=leto_max,
            value=(leto_min, leto_max)
        )

        #Filtriramo in rišemo bar-graf
        filtirano = yearly_avg[
            yearly_avg["YEAR"].between(izberimo_obdobje[0], izberimo_obdobje[1])
        ].copy()
        filtirano = filtirano.set_index("YEAR")

        st.subheader("Povprečno delovno aktivno prebivalstvo v Sloveniji po letih")
        st.bar_chart(filtirano["DATA"])
    else:
        st.warning('Podatki za regijo "SLOVENIJA" niso na voljo.')

    st.markdown("---")

elif section == "Napoved":
    st.header("Napovedni model")
    st.header("model??")


# --- Footer ---
st.markdown("---")
st.caption("Avtorji: Nika Demšar, Urška Frelih Uhelj, Anja Klančar, Eva Müller | Vir podatkov: podatki.gov.si")
