import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from data_loader import load_data

st.header("Napovedni modeli")

df_delo, df_bdp = load_data()

def napoved_linearni(X, y, prihodnja_leta):
    model = LinearRegression()
    model.fit(X, y)
    napoved = model.predict(prihodnja_leta)
    return napoved

def napoved_polinomski(X, y, prihodnja_leta, stopnja=3):
    poly = PolynomialFeatures(degree=stopnja)
    X_poly = poly.fit_transform(X)
    prihodnja_poly = poly.transform(prihodnja_leta)
    model = LinearRegression()
    model.fit(X_poly, y)
    napoved = model.predict(prihodnja_poly)
    return napoved

def napoved_svr(X, y, prihodnja_leta):
    model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
    model.fit(X, y)
    napoved = model.predict(prihodnja_leta)
    return napoved

def prikazi_opis_modela(model):
    if model == "Linearni":
        return ("Linearni model predpostavlja linearno povezavo med časom in "
                "napovedano spremenljivko. Enostaven je za interpretacijo in "
                "dobro deluje, če je trend linearen.")
    elif model == "Polinomski (stopnja 3)":
        return ("Polinomski model omogoča zajemanje nelinearnih trendov s pomočjo "
                "polinomskih funkcij. Stopnja 3 pomeni, da je vključen kubični polinom.")
    elif model == "SVR":
        return ("Support Vector Regressor (SVR) je zmogljiv nelinearni model, ki "
                "najde najboljši kompromis med natančnostjo in kompleksnostjo "
                "modela z uporabo podpornih vektorjev.")
    else:
        return ""

# ----------------------------------
# Napoved delovno aktivnega prebivalstva
# ----------------------------------

st.subheader("Napoved delovno aktivnega prebivalstva")

data_slovenia = df_delo[df_delo["STATISTIČNA REGIJA"] == "SLOVENIJA"]
if not data_slovenia.empty:
    monthly_total = data_slovenia.groupby("MESEC")["DATA"].sum().reset_index()
    monthly_total["date"] = pd.to_datetime(monthly_total["MESEC"] + "-01", format="%Y-%m-%d")
    monthly_total["YEAR"] = monthly_total["date"].dt.year

    yearly_avg_delo = (
        monthly_total.groupby("YEAR")["DATA"]
        .mean()
        .reset_index()
        .sort_values("YEAR")
    )

    n_let_delo = st.slider("Koliko let napovedati za delovno aktivno prebivalstvo?", 1, 10, 5)

    model_delo_izbira = st.selectbox("Izberi model za napoved delovno aktivnega prebivalstva:",
                                     ["Linearni", "Polinomski (stopnja 3)", "SVR"])

    st.markdown(prikazi_opis_modela(model_delo_izbira))

    X = yearly_avg_delo["YEAR"].values.reshape(-1, 1)
    y = yearly_avg_delo["DATA"].values
    prihodnja_leta = np.arange(X[-1][0] + 1, X[-1][0] + 1 + n_let_delo).reshape(-1, 1)

    if model_delo_izbira == "Linearni":
        napoved_delo = napoved_linearni(X, y, prihodnja_leta)
    elif model_delo_izbira == "Polinomski (stopnja 3)":
        napoved_delo = napoved_polinomski(X, y, prihodnja_leta, stopnja=3)
    else:  # SVR
        napoved_delo = napoved_svr(X, y, prihodnja_leta)

    napoved_delo_zaokrozena = np.round(napoved_delo).astype(int)

    df_napoved_delo = pd.DataFrame({
        "YEAR": prihodnja_leta.flatten(),
        "Napoved": napoved_delo_zaokrozena
    }).set_index("YEAR")

    combined_delo = yearly_avg_delo.set_index("YEAR").copy()
    combined_delo["Napoved"] = np.nan
    combined_delo = pd.concat([combined_delo, df_napoved_delo])
    combined_delo = combined_delo.sort_index()

    st.line_chart(combined_delo[["DATA", "Napoved"]])

else:
    st.warning("Podatki za 'SLOVENIJA' niso na voljo v podatkih o delovni aktivnosti.")

# ----------------------------------
# Napoved BDP
# ----------------------------------

st.subheader("Napoved BDP")

df_bdp_slovenija = df_bdp[df_bdp["TERITORIALNA ENOTA"] == "SLOVENIJA"] if "TERITORIALNA ENOTA" in df_bdp.columns else df_bdp
df_bdp_slovenija = df_bdp_slovenija.copy()
df_bdp_slovenija["YEAR"] = df_bdp_slovenija["LETO"]

yearly_bdp = (
    df_bdp_slovenija.groupby("YEAR")["DATA"]
    .mean()
    .reset_index()
    .sort_values("YEAR")
)

n_let_bdp = st.slider("Koliko let napovedati za BDP?", 1, 10, 5, key="bdp_slider")

model_bdp_izbira = st.selectbox("Izberi model za napoved BDP:",
                               ["Linearni", "Polinomski (stopnja 3)", "SVR"], key="bdp_model")

st.markdown(prikazi_opis_modela(model_bdp_izbira))

X_bdp = yearly_bdp["YEAR"].values.reshape(-1, 1)
y_bdp = yearly_bdp["DATA"].values
prihodnja_leta_bdp = np.arange(X_bdp[-1][0] + 1, X_bdp[-1][0] + 1 + n_let_bdp).reshape(-1, 1)

if model_bdp_izbira == "Linearni":
    napoved_bdp = napoved_linearni(X_bdp, y_bdp, prihodnja_leta_bdp)
elif model_bdp_izbira == "Polinomski (stopnja 3)":
    napoved_bdp = napoved_polinomski(X_bdp, y_bdp, prihodnja_leta_bdp, stopnja=3)
else:  # SVR
    napoved_bdp = napoved_svr(X_bdp, y_bdp, prihodnja_leta_bdp)

napoved_bdp_zaokrozena = np.round(napoved_bdp).astype(int)

df_napoved_bdp = pd.DataFrame({
    "YEAR": prihodnja_leta_bdp.flatten(),
    "Napoved": napoved_bdp_zaokrozena
}).set_index("YEAR")

combined_bdp = yearly_bdp.set_index("YEAR").copy()
combined_bdp["Napoved"] = np.nan
combined_bdp = pd.concat([combined_bdp, df_napoved_bdp])
combined_bdp = combined_bdp.sort_index()

st.line_chart(combined_bdp[["DATA", "Napoved"]])

st.write("Opazimo, da je za napoved delovno aktivnega prebivalstva najbolj primeren linearni model, medtem ko je za napoved BDP-ja najboljši polinomski model.")
