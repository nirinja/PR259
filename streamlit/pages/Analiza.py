import streamlit as st
import pandas as pd
from data_loader import load_data

st.header("Analiza")

df_delo, df_bdp = load_data()

# ----------------------------------
# Primerjava regij skozi leta
# ----------------------------------

st.subheader("Primerjava regij skozi leta")
st.write(
    """
    Tukaj primerjamo delovno aktivno prebivalstvo v različnih regijah skozi leta.
    Uporabnik lahko izbere regije, ki jih želi primerjati, ter način agregacije podatkov po letih:
    povprečje, vsota ali največja vrednost.
    """
)

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

# ----------------------------------
# Povprečno delovno aktivno prebivalstvo v Sloveniji po letih
# ----------------------------------

st.subheader("Povprečno delovno aktivno prebivalstvo v Sloveniji po letih")
st.write(
    """
    Prikazujemo povprečno število delovno aktivnih oseb v Sloveniji na letni ravni.
    Podatke lahko filtrirate po izbranem obdobju let z drsnikom.
    """
)

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

    st.bar_chart(filtrirano["DATA"])
else:
    st.warning('Podatki za regijo "SLOVENIJA" niso na voljo.')

# ----------------------------------
# Korelacija med BDP in zaposlenostjo
# ----------------------------------

st.subheader("Korelacija med BDP in zaposlenostjo")
st.write(
    """
    Tukaj analiziramo povezavo med bruto domačim proizvodom (BDP) in zaposlenostjo
    v izbrani regiji skozi leta.
    Izračunamo korelacijski koeficient, ki kaže, kako močno sta ti dve spremenljivki povezani.
    """
)

regija = st.selectbox("Izberi regijo za korelacijo:",
                      sorted(df_delo["STATISTIČNA REGIJA"].dropna().unique()),
                      index=0)

delo_regija = df_delo[df_delo["STATISTIČNA REGIJA"] == regija]
zaposlenost = delo_regija.groupby("YEAR")["DATA"].mean().reset_index()
zaposlenost.columns = ["LETO", "ZAPOSLENOST"]

bdp_skupno = df_bdp.groupby("LETO")["DATA"].mean().reset_index()
bdp_skupno.columns = ["LETO", "BDP"]

zdruzitev = pd.merge(zaposlenost, bdp_skupno, on="LETO", how="inner")

st.write("Pregled združenih podatkov:")
st.dataframe(zdruzitev)

korelacija = zdruzitev["ZAPOSLENOST"].corr(zdruzitev["BDP"])
st.write(f"Korelacijski koeficient med zaposlenostjo in BDP je {korelacija:.3f}.")

st.line_chart(zdruzitev.set_index("LETO")[["ZAPOSLENOST", "BDP"]])

# Interpretacija velikosti učinka
abs_r = abs(korelacija)
if abs_r < 0.1:
    interpretacija = "zelo šibka (zanemarljiva) povezanost"
elif abs_r < 0.3:
    interpretacija = "šibka povezanost"
elif abs_r < 0.5:
    interpretacija = "srednja povezanost"
else:
    interpretacija = "močna povezanost"

st.write(f"Velikost učinka (na podlagi korelacije): {interpretacija}.")
st.write(
    """
    Korelacijski koeficient meri linearno povezanost med zaposlenostjo in BDP-jem.
    Višja absolutna vrednost pomeni močnejšo povezanost: pozitivna vrednost kaže, da obe spremenljivki rasteta skupaj,
    negativna pa da ena pada, ko druga narašča.
    """
)

