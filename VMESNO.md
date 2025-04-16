# Analiza delovno aktivnega prebivalstva in BDP Slovenije

*Vmesno poročilo projekta pri predmetu Podatkovno rudarjenje, skupina 9*

## Člani 
- Nika Demšar  
- Urška Frelih Uhelj  
- Anja Klančar  
- Eva Müller 

## Uvod in opis problema

Projekt se osredotoča na analizo delovno aktivnega prebivalstva in strukture BDP v Sloveniji, pri čemer želimo razumeti, kako demografski trendi in gospodarski kazalniki vplivajo na dinamiko zaposlovanja. V tem vmesnem poročilu predstavljamo preliminarne rezultate analize, ki temelji na odprtih podatkih in časovnih serijah o delovno aktivnem prebivalstvu ter letnih podatkih o izdatkovni strukturi BDP. S tem pristopom želimo osvetliti sezonske vzorce, vpliv kriznih obdobij (kot so gospodarska kriza in pandemija COVID-19) ter izdelati napovedne modele za prihodnje spremembe.

## Podatki

Analiza temelji na dveh glavnih virih odprtih podatkov Slovenije, ki smo jih pridobile preko [podatki.gov.si](https://podatki.gov.si):

1. **Delovno aktivno prebivalstvo**  
   - **Vir:** [Delovno aktivno prebivalstvo](https://podatki.gov.si/dataset/surs0700992s)  
   - **Obdobje:** 2010–2024  
   - **Atributi:** Število delovno aktivnega prebivalstva, populacija, statistična regija, starostni razred in mesec  
   - **Namen:** Spremljanje zaposlenosti in demografskih trendov. Podatki omogočajo analizo razdelitve po starostnih skupinah in regijah ter preučevanje sezonskih nihanj.

2. **Izdatkovna struktura BDP**  
   - **Vir:** [Izdatkovna struktura BDP](https://podatki.gov.si/dataset/surs0301935s?resource_id=8935a064-5888-4ab9-9066-0838f6f2743b)  
   - **Obdobje:** 1995–2024  
   - **Atributi:** Izdatkovna struktura BDP, vrednost v milijonih EUR oziroma odstotne točke ter leto  
   - **Namen:** Prikaz sprememb v sestavi BDP in sledenje gospodarskim trendom, ki vplivajo na zaposlovanje.

## Izvedene analize

Za realizacijo analize smo najprej odstranile nereprezentativne podatke z namenom priprave na nadaljnje analize. Sledile so naslednje ključne faze:

- **Časovna serijska analiza:**  
  Preučile smo letne trende delovno aktivnega prebivalstva. S pomočjo agregacije po letih smo izračunale skupno število delovno aktivnih prebivalcev in te rezultate vizualizirale v stolpčnem diagramu, kar omogoča jasen pregled sprememb skozi čas. S tem smo lahko identificirale sezonske vzorce in prepoznale nenadne odklone.

- **Starostna analiza:**

    Pri starostni analizi smo najprej podatke razvrstile glede na starostne skupine, ki so bile definirane v viru podatkov, ter izdvojile informacije o številu delovno aktivnih prebivalcev za vsako starostno kategorijo. Rezultati so bili vizualno predstavljeni preko grafov, ki jasno prikazujejo trende v deležih posameznih starostnih kategorij skozi opazovano obdobje. To nam omogoča analizo procesov staranja prebivalstva in njihovega vpliva na dinamiko trga dela.

- **Analiza po regijah:**

    Pri analizi strukture delovnega prebivalstva po regijah smo podatke razvrstile glede na statistične regije, kar je omogočilo primerjavo in identifikacijo regionalnih razlik. Najprej smo izbrale podatke za posamezne regije in jih ustrezno agregirale, da smo pridobile letne trende števila delovno aktivnih prebivalcev za vsako regijo. S tem pristopom smo lahko vizualno primerjale, kako se delovno aktivno prebivalstvo spreminja med urbanimi in podeželskimi območji, ter prepoznale specifične regionalne vzorce. 
- **Korelacijska analiza:**

  Za preverjanje povezanosti med številom delovno aktivnih prebivalcev in letno vrednostjo BDP smo izvedle korelacijsko analizo. Zagotovile smo da sta obe seriji podatkov ustrezno usklajeni po letih. Z uporabo Pearsonovega korelacijskega koeficienta smo ugotovile zelo močno pozitivno povezanost med tema dvema kazalnikoma.

- **Analiza vpliva kriznih obdobij:**  
  Posebej smo preučile vpliv gospodarske krize in pandemije COVID-19. Vizualizacije jasno prikazujejo, da se je v obdobjih kriz pojavilo stanje stagnacije oziroma padca delovno aktivnega prebivalstva, s kasnejšim postopnim okrevanjem, kar dodatno poudarja občutljivost trga dela na zunanje šokove.

Pri vizualizaciji rezultatov smo uporabile grafe, ki so ključni za boljše ponazoritev trendov in korelacij med analiziranimi kazalniki.

## Uporabljena orodja

Pri izvedbi analize smo uporabile naslednja orodja:
- **Programski jezik:** Python  
- **Knjižnice:** pandas, matplotlib, numpy, pyaxis  
- **Platforma:** Jupyter Notebook  
- **Podatkovni vmesnik:** pxwebreader za uvoz podatkov iz formata .px

Celotna analiza je dosegljiva v datoteki [`koda/koda.ipynb`](koda/koda.ipynb) v repozitoriju.

## Glavne ugotovitve

Dosedanje analize prinašajo več pomembnih vpogledov:

- **Spremembe demografske strukture:**  
  Opazile smo, da se delež starejših delovno aktivnih prebivalcev v Sloveniji veča, medtem ko se delež mlajših zmanjšuje. Ta trend kaže na proces staranja prebivalstva, kar pomeni, da se več ljudi iz skupine 55+ aktivno udeležuje na trgu dela, medtem ko mlajše generacije vstopajo v delovno silo s slabšo hitrostjo.

- **Vpliv kriznih obdobij:**  
  Analize kažejo na izražene padce števila zaposlenih med gospodarsko kriznimi obdobji, kjer je videti, da se med kriznimi leti 2010–2013 število delovno aktivnih prebivalcev ustavi ali celo zniža, medtem ko pandemija COVID-19 privede do blagega začasnega upada, s hitrim okrevanjem v poznejših obdobjih. To kaže, da trgi dela precej reagirajo na zunanje gospodarske šoke.

- **Povezava z gospodarskimi kazalniki:**  
  Statistična analiza potrjuje, da obstaja močna pozitivna korelacija med številom delovno aktivnih prebivalcev in letno vrednostjo BDP. Večja zaposlenost sovpada z večjo gospodarsko rastjo, kar potrjuje pomembnost človeškega kapitala kot ključnega dejavnika pri ustvarjanju gospodarske vrednosti.

- **Regijska dinamika:**  
  Primerjava med različnimi statističnimi regijami razkriva, da urbanizirane regije, kot je Osrednjeslovenska, beležijo najmočnejšo rast delovno aktivnega prebivalstva, kar je posledica koncentracije gospodarskih aktivnosti. Nasprotno pa bolj podeželske regije kažejo počasnejšo rast ali celo stagnacijo, kar priporoča potrebe po regionalni podpori in investicijah.

## Zaključek in nadaljnji koraki

Dosedanji rezultati nakazujejo na ključne demografske in gospodarske trende v Sloveniji, ki bodo vplivali na prihodnjo dinamiko trga dela. Na podlagi dobivenih vpogledov načrtujemo dodatno poglobljeno analizo...

---

