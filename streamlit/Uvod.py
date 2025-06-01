#streamlit run Uvod.py
import streamlit as st

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


# Footer
st.markdown("---")
st.caption("Avtorice: Nika Demšar, Urška Frelih Uhelj, Anja Klančar, Eva Müller | Vir: podatki.gov.si")