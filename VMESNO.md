# **Analiza delovno aktivnega prebivalstva in BDP Slovenije**

*Vmesno poročilo projekta pri predmetu Podatkovno rudarjenje, skupina 9*

## Člani 
- Nika Demšar  
- Urška Frelih Uhelj  
- Anja Klančar  
- Eva Müller 

---

## Uvod in Opis problema

Projekt se osredotoča na analizo delovno aktivnega prebivalstva in strukture BDP v Sloveniji, pri čemer želimo razumeti, kako demografski trendi in gospodarski kazalniki vplivajo na dinamiko zaposlovanja. V tem vmesnem poročilu predstavljamo preliminarne rezultate analize delovno aktivnega prebivalstva in strukture BDP v Sloveniji. Analiza temelji na odprtih podatkih, ki vključujejo časovne serije o delovno aktivnem prebivalstvu in letne podatke o izdatkovni strukturi BDP. S tem pristopom želimo osvetliti sezonske vzorce, vpliv kriznih obdobij (kot so gospodarska kriza in pandemija COVID-19) ter izdelati napovedne modele za prihodnje spremembe.



##  Podatki

Analiza temelji na dveh glavnih virih odprtih podatkov Slovenije iz [podatki.gov.si](https://podatki.gov.si):

1. **Delovno aktivno prebivalstvo**  
   - **Vir:** [Delovno aktivno prebivalstvo](https://podatki.gov.si/dataset/surs0700992s)  
   - **Obdobje:** 2010–2024  
   - **Atributi:** Število delovno aktivnega prebivalstva, populacija, statistična regija, starostni razred in mesec  
   - **Namen:** spremljanje zaposlenosti in demografskih trendov. Podatki omogočajo analizo razdelitve po starostnih skupinah in regijah ter preučevanje sezonskih nihanj.

2. **Izdatkovna struktura BDP**  
   - **Vir:** [Izdatkovna struktura BDP](https://podatki.gov.si/dataset/surs0301935s?resource_id=8935a064-5888-4ab9-9066-0838f6f2743b)  
   - **Obdobje:** 1995–2024  
   - **Atributi:** Izdatkovna struktura BDP, vrednost v milijonih EUR oziroma odstotne točke ter leto  
   - **Namen:** Prikaz sprememb v sestavi BDP. Podatki omogočajo sledenje spremembam gospodarske aktivnosti in ugotavljanje vpliva na zaposlovanje.

## Izvedene analize

Za realizacijo analize smo najprej pripravili podatke z namenom čiščenja in standardizacije obeh zbirk. Sledi nekaj ključnih korakov in metod:

- **Čiščenje in priprava podatkov:**  
  Podatke smo uvozili v Python okolje, odstranili manjkajoče vrednosti in standardizirali formate dat. Pri tem smo poskrbeli, da so vsi atributi ustrezno kodirani za nadaljnjo analizo.

- **Časovna serijska analiza:**  
  Preučili smo mesečne trende delovno aktivnega prebivalstva z uporabo časovnih serij, kar je omogočilo identifikacijo sezonskih vzorcev in nenadnih odklonov (npr. v obdobju COVID-19).  
- graf?
- **Korelacijska analiza:**  
  Analizirali smo povezave med količino delovno aktivnega prebivalstva in letnimi vrednostmi BDP. Ta analiza je pripomogla k razumevanju, kako se spremembe na trgu dela odzivajo na gospodarske spremembe.  

- **Analiza vpliva zunanjih dejavnikov:**  
  Posebej smo preučili vpliv gospodarske krize in pandemije COVID-19. Z uporabo regresijskih modelov smo poskušali identificirati, v kolikšni meri sta ti dogodka vplivala na delovno aktivno prebivalstvo.

- **Napovedna analiza:**  
  Z uporabo časovnih modelov (npr. ARIMA model) smo izdelali preliminarne napovedi o prihodnjih trendih, kar je še predmet dodatnih analiz.

Pri vizualizaciji rezultatov smo uporabili grafe... moram dodat se grafe notr?

##  Glavne ugotovitve

Dosedanje analize prinašajo več pomembnih ugotovitev:
- **Spremembe demografske strukture:**  
  Vidno se povečuje delež starejših delovno aktivnih prebivalcev, medtem ko se delež mlajših zmanjšuje, kar kaže na proces staranja prebivalstva.

- **Sezonski vzorci:**  
  Opazimo jasna sezonska nihanja, ki so lahko posledica panog, specifičnih gospodarskih ciklov ali začasnih zaposlovanj, kar se posebej izraža v nekaterih regijah.

- **Vpliv kriznih obdobij:**  
  Analize kažejo na ostre padce števila zaposlenih med kriznimi obdobji, kot sta gospodarska kriza in pandemija COVID-19, s kasnejšim postopnim okrevanjem.

- **Povezava z gospodarskimi kazalniki:**  
  Statistična analiza potrjuje, da obstaja korelacija med številom delovno aktivnih oseb in letno vrednostjo BDP, kar nakazuje medsebojno povezavo med demografskimi trendi in gospodarskimi spremembami.


##  Uporabljena orodja
- Python, pandas, matplotlib, seaborn
- Jupyter Notebook
- pxwebreader (uvoz podatkov iz .px)

Celotna analiza se nahaja v [`koda/koda.ipynb`](koda/koda.ipynb).

## Zaključek in nadaljnji koraki

Dosedanji rezultati nakazujejo na pomembne demografske trende in povezanost med zaposlenostjo in gospodarskimi kazalniki v Sloveniji.  --plan za ostala uprasanja?
