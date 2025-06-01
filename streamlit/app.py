import numpy as np
import streamlit as st
import pandas as pd
import os


@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "..", "podatki")

    # Delo
    path_delo = os.path.join(DATA_DIR, "delo.csv")
    df_delo = pd.read_csv(path_delo, sep=";", encoding="utf-8")
    df_delo["MESEC"] = df_delo["MESEC"].str.replace("M", "-", regex=False)
    df_delo["YEAR"] = df_delo["MESEC"].str[:4].astype(int)
    df_delo["DATA"] = pd.to_numeric(df_delo["DATA"], errors="coerce")
    df_delo = df_delo[df_delo["YEAR"] != df_delo["YEAR"].max()]
    df_delo["date"] = pd.to_datetime(df_delo["MESEC"] + "-01", format="%Y-%m-%d")

    # BDP
    path_bdp = os.path.join(DATA_DIR, "bdp.csv")
    df_bdp = pd.read_csv(path_bdp, sep=";", encoding="utf-8")
    df_bdp["DATA"] = pd.to_numeric(df_bdp["DATA"], errors="coerce")
    df_bdp["LETO"] = df_bdp["LETO"].astype(int)
    df_bdp = df_bdp[df_bdp["LETO"] != df_bdp["LETO"].max()]
    if "CKVARTER" in df_bdp.columns:
        df_bdp["date"] = pd.to_datetime(
            df_bdp["LETO"].astype(str) + "-" +
            ((df_bdp["CKVARTER"] - 1) * 3 + 1).astype(int).astype(str).str.zfill(2) + "-01",
            format="%Y-%m-%d"
        )
    else:
        df_bdp["date"] = pd.to_datetime(df_bdp["LETO"].astype(str) + "-01-01", format="%Y-%m-%d")

    return df_delo, df_bdp


# Konfiguracija
st.set_page_config(
    page_title="Analiza zaposlenosti in BDP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Analiza delovno aktivnega prebivalstva in BDP v Sloveniji")

df_delo, df_bdp = load_data()

# Navigacija
section = st.sidebar.radio("Navigacija", ["Uvod", "Analiza", "Napoved"])

if section == "Uvod":
    st.title("Uvod")

    st.markdown("""
    Cilj te analize je preučiti, kako se spreminja delovno aktivno prebivalstvo v Sloveniji in kakšna je njegova povezanost z bruto domačim proizvodom (BDP).

    **Avtorice:**
    - Nika Demšar
    - Urška Frelih Uhelj
    - Anja Klančar
    - Eva Müller

    ## Podatki

    Analiza temelji na treh glavnih virih odprtih podatkov Slovenije iz [podatki.gov.si](https://podatki.gov.si):

    Iz podatkov o zaposlenosti smo izločile leto 2025, ker so podatki nereprezentativni, saj se leto še ni končalo in bi pokvarilo povprečja. Podatke za ostala leta smo združile po letih, da smo vizualno predstavile spremembe v delovno aktivnem prebivalstvu skozi čas.

    ### Viri:

    - [**Delovno aktivno prebivalstvo**](https://podatki.gov.si/dataset/surs0700992s)  
      **Obdobje:** 2010–2025  
      **Atributi:** Število delovno aktivnega prebivalstva, populacija, statistična regija, starostni razred, mesec  
      **Namen:** Spremljanje zaposlenosti in demografskih trendov. Podatki omogočajo analizo razdelitve po starostnih skupinah in regijah ter preučevanje sezonskih nihanj.

    - [**Izdatkovna struktura BDP**](https://podatki.gov.si/dataset/surs0301935s?resource_id=8935a064-5888-4ab9-9066-0838f6f2743b)  
      **Obdobje:** 1995–2025  
      **Atributi:** Število delovno aktivnih prebivalcev, površina (km²), delež prebivalcev, gostota naseljenosti, živorojeni, naravni prirast, skupni selitveni prirast  
      **Namen:** Prikaz sprememb v sestavi BDP. Podatki omogočajo sledenje spremembam gospodarske aktivnosti in ugotavljanje vpliva na zaposlovanje.

    - [**Prebivalstvo po statističnih regijah**](https://podatki.gov.si/dataset/surs2640005s)  
      **Obdobje:** 2008–2025  
      **Atributi:** Število delovno aktivnega prebivalstva, populacija, statistična regija, starostni razred  
      **Namen:** Primerjava podatkov na ravni celotne populacije ter analiza sestave prebivalstva.
    """)


elif section == "Analiza":
    st.header("Analiza")

    st.header("Primerjava regij skozi leta")
    regije = sorted(df_delo["STATISTIČNA REGIJA"].dropna().unique())
    izbrane_regije = st.multiselect("Izberi regije za primerjavo:", regije, default=["SLOVENIJA"])

    metrika = st.radio("Agregacija po letu:", ["Povprečje", "Vsota", "Največ"])
    df_filter = df_delo[df_delo["STATISTIČNA REGIJA"].isin(izbrane_regije)].copy()

    if metrika == "Povprečje":
        agregirano = df_filter.groupby(["YEAR", "STATISTIČNA REGIJA"])["DATA"].mean().unstack()
    elif metrika == "Vsota":
        agregirano = df_filter.groupby(["YEAR", "STATISTIČNA REGIJA"])["DATA"].sum().unstack()
    else:
        agregirano = df_filter.groupby(["YEAR", "STATISTIČNA REGIJA"])["DATA"].max().unstack()

    st.line_chart(agregirano)

    data_slovenia = df_delo[df_delo["STATISTIČNA REGIJA"] == "SLOVENIJA"]

    if not data_slovenia.empty:
        monthly_total = data_slovenia.groupby("MESEC")["DATA"].sum().reset_index()
        monthly_total["date"] = pd.to_datetime(monthly_total["MESEC"] + "-01", format="%Y-%m-%d")
        monthly_total["YEAR"] = monthly_total["date"].dt.year

        yearly_avg = (
            monthly_total.groupby("YEAR")["DATA"]
            .mean()
            .reset_index()
            .sort_values("YEAR")
        )

        leto_min = int(yearly_avg["YEAR"].min())
        leto_max = int(yearly_avg["YEAR"].max())
        izberimo_obdobje = st.slider(
            "Izberi obdobje let:",
            min_value=leto_min,
            max_value=leto_max,
            value=(leto_min, leto_max)
        )

        filtrirano = yearly_avg[
            yearly_avg["YEAR"].between(izberimo_obdobje[0], izberimo_obdobje[1])
        ].copy()
        filtrirano = filtrirano.set_index("YEAR")

        st.subheader("Povprečno delovno aktivno prebivalstvo v Sloveniji po letih")
        st.bar_chart(filtrirano["DATA"])
    else:
        st.warning('Podatki za regijo "SLOVENIJA" niso na voljo.')

    st.header("Korelacija med BDP in zaposlenostjo")

    regija = st.selectbox("Izberi regijo za korelacijo:", sorted(df_delo["STATISTIČNA REGIJA"].dropna().unique()),
                          index=0)
    delo_regija = df_delo[df_delo["STATISTIČNA REGIJA"] == regija]
    zaposlenost = delo_regija.groupby("YEAR")["DATA"].mean().reset_index()
    zaposlenost.columns = ["LETO", "ZAPOSLENOST"]

    bdp_skupno = df_bdp.groupby("LETO")["DATA"].mean().reset_index()
    bdp_skupno.columns = ["LETO", "BDP"]

    zdruzitev = pd.merge(zaposlenost, bdp_skupno, on="LETO", how="inner")
    st.write("Pregled združenih podatkov:")
    st.dataframe(zdruzitev)

elif section == "Napoved":
    st.header("Napovedni model")

    data_slovenia = df_delo[df_delo["STATISTIČNA REGIJA"] == "SLOVENIJA"]

    if not data_slovenia.empty:
        monthly_total = data_slovenia.groupby("MESEC")["DATA"].sum().reset_index()
        monthly_total["date"] = pd.to_datetime(monthly_total["MESEC"] + "-01", format="%Y-%m-%d")
        monthly_total["YEAR"] = monthly_total["date"].dt.year

        yearly_avg = (
            monthly_total.groupby("YEAR")["DATA"]
            .mean()
            .reset_index()
            .sort_values("YEAR")
        )

        leto_min = int(yearly_avg["YEAR"].min())
        leto_max = int(yearly_avg["YEAR"].max())

        st.subheader("Nastavitve napovedi")

        izbrano_obdobje = (leto_min, leto_max)

        n_let_napoved = st.number_input(
            "Za koliko let v prihodnost napovedati?",
            min_value=1,
            max_value=10,
            value=5,
            step=1
        )

        model_izbira = st.selectbox(
            "Izberi model napovedi:",
            options=["Linearna regresija", "Drseče povprečje"]
        )

        # Filtriraj podatke glede na izbrano obdobje
        data_model = yearly_avg[
            yearly_avg["YEAR"].between(izbrano_obdobje[0], izbrano_obdobje[1])
        ].copy()

        X = data_model["YEAR"].values.reshape(-1, 1)
        y = data_model["DATA"].values

        prihodnja_leta = np.arange(X[-1][0] + 1, X[-1][0] + 1 + n_let_napoved).reshape(-1, 1)

        if model_izbira == "Linearna regresija":
            from sklearn.linear_model import LinearRegression

            model = LinearRegression()
            model.fit(X, y)
            prihodnje_napovedi = model.predict(prihodnja_leta)

        elif model_izbira == "Drseče povprečje":
            # Drseče povprečje: povprečje zadnjih N točk
            window = min(3, len(y))  # okno 3 ali manj če je premalo podatkov
            zadnja_povprecja = np.convolve(y, np.ones(window)/window, mode='valid')
            zadnja_vrednost = zadnja_povprecja[-1] if len(zadnja_povprecja) > 0 else y[-1]
            prihodnje_napovedi = np.full(shape=(n_let_napoved,), fill_value=zadnja_vrednost)

        # Zaokroži napovedi na cela števila
        prihodnje_napovedi_zaokrozene = np.round(prihodnje_napovedi).astype(int)

        napoved_df = pd.DataFrame({
            "YEAR": prihodnja_leta.flatten(),
            "Napovedana DATA": prihodnje_napovedi_zaokrozene
        })

        st.subheader(f"Napoved za prihodnjih {n_let_napoved} let (model: {model_izbira})")

        combined_df = data_model.copy()
        combined_df = combined_df.set_index("YEAR")
        combined_df["Napoved"] = np.nan

        napoved_df = napoved_df.set_index("YEAR")
        combined_df = pd.concat([combined_df, napoved_df.rename(columns={"Napovedana DATA": "Napoved"})])

        combined_df = combined_df.sort_index()

        st.line_chart(combined_df[["DATA", "Napoved"]])

    else:
        st.warning('Podatki za regijo "SLOVENIJA" niso na voljo.')



# Footer
st.markdown("---")
st.caption("Avtorice: Nika Demšar, Urška Frelih Uhelj, Anja Klančar, Eva Müller | Vir: podatki.gov.si")