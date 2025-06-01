# export_px.py
from pyaxis import pyaxis
import pandas as pd
import os

# DEFINIRAJ, KJE SO .PX in KAM SHRANIMO CSV
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DATA_PX    = os.path.join(BASE_DIR, "podatki")
DATA_CSV   = os.path.join(BASE_DIR, "podatki")

# Pretvori delo.PX → delo.csv
px_delo = pyaxis.parse(os.path.join(DATA_PX, "delo.PX"), encoding="windows-1250")
df_delo = pd.DataFrame(px_delo["DATA"])

# Po potrebi lahko tukaj v Jupyter-podobnem slogu dodaš že del predprocesiranja:
#   df_delo["YEAR"] = df_delo["MESEC"].str[:4]
#   df_delo["DATA"] = pd.to_numeric(df_delo["DATA"], errors="coerce")
#   df_delo = df_delo[df_delo["YEAR"] != df_delo["YEAR"].max()]
#   df_delo["date"] = pd.to_datetime(df_delo["MESEC"].str.replace("-", "") + "01", format="%Y%m%d")

# Shrani kot CSV
csv_delo = os.path.join(DATA_CSV, "delo.csv")
df_delo.to_csv(csv_delo, sep=";", index=False, encoding="utf-8")
print(f"Ustvarjen: {csv_delo}")

# Pretvori bdp.PX → bdp.csv
px_bdp = pyaxis.parse(os.path.join(DATA_PX, "bdp.PX"), encoding="windows-1250")
df_bdp = pd.DataFrame(px_bdp["DATA"])

# Podobno kot zgoraj, če želiš:
#   df_bdp["DATA"] = pd.to_numeric(df_bdp["DATA"], errors="coerce")
#   df_bdp = df_bdp[df_bdp["LETO"] != df_bdp["LETO"].max()]
#   df_bdp["date"] = pd.to_datetime(
#       df_bdp["LETO"].astype(str)
#       + ((df_bdp["CKVARTER"] - 1) * 3 + 1).astype(int).astype(str).str.zfill(2)
#       + "01", format="%Y%m%d"
#   )

csv_bdp = os.path.join(DATA_CSV, "bdp.csv")
df_bdp.to_csv(csv_bdp, sep=";", index=False, encoding="utf-8")
print(f"Ustvarjen: {csv_bdp}")

# --- 3) (Neobvezno) pretvori prebivalstvo.PX → prebivalstvo.csv ---
px_preb = pyaxis.parse(os.path.join(DATA_PX, "prebivalstvo.PX"), encoding="windows-1250")
df_preb = pd.DataFrame(px_preb["DATA"])
csv_preb = os.path.join(DATA_CSV, "prebivalstvo.csv")
df_preb.to_csv(csv_preb, sep=";", index=False, encoding="utf-8")
print(f"Ustvarjen: {csv_preb}")
