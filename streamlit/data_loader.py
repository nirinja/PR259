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