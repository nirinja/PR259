# **Analiza proračuna Slovenije**  
*Projekt pri predmetu Podatkovno rudarjenje, skupina 9*  

## **Člani**  
- Nika Demšar  
- Urška Frelih Uhelj  
- Anja Klančar  
- Eva Müller  

## **Opis virov in podatkov**  
Uporabljali bomo odprte podatke Slovenije: [Proračun Republike Slovenije](https://podatki.gov.si/dataset/proracun-republike-slovenije), ki vsebujejo podatke do leta 2014.  
Podatke bomo obdelovale v JSON obliki. Do podatkovnega API-ja lahko dostopamo z ukazom:  
[https://podatki.gov.si/api/3/action/datastore_search](https://podatki.gov.si/api/3/action/datastore_search).  

Proračun je sestavljen iz naslednjih delov (ZJF, 10. člen; Proračunski priročnik 2025):  

1. **Splošni del proračuna (I. del)**:  
   Vključuje skupno bilanco prihodkov in odhodkov (A bilanca), račun finančnih terjatev in naložb (B bilanca) ter račun financiranja (C bilanca).  
   Pripravljen je po ekonomski klasifikaciji in podaja informacije o tem, kako država zbira prihodke in jih porablja.  

2. **Posebni del proračuna (II. del)**:  
   Vključuje finančne načrte neposrednih uporabnikov (institucionalna klasifikacija) ter odhodke in druge izdatke, predstavljene po politikah, programih in podprogramih (programska klasifikacija).  
   Daje informacije o tem, kdo porablja sredstva in za katera področja.  

3. **Načrt razvojnih programov (III. del)**:  
   Vključuje letne načrte razvojnih programov neposrednih uporabnikov, ki so opredeljeni z dokumenti dolgoročnega razvojnega načrtovanja ali posebnimi predpisi.  
   Odhodki so načrtovani po posameznih ukrepih, projektih in virih financiranja za celotno obdobje izvajanja. Prikazani so po podprogramih, ukrepih, skupinah projektov in virih sredstev.  

Osredotočile se bomo na **I. in II. del proračuna** – splošni in posebni del. Analizirale bomo, kakšen je proračun in kolikšen del sredstev se porabi za posamezna področja. Na koncu bomo sestavo proračuna povezale s sestavo državnega zbora in koalicije v tistem času.  

## **Cilj**  
Želimo pokazati korelacijo med sestavo državnega zbora in koalicije ter strukturo proračuna. S tem bi lahko na podlagi sestave parlamenta napovedali proračun.