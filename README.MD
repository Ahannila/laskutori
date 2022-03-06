### Laskutori
https://laskutori.herokuapp.com/


## Lopullinen sovellus
Sovellus on tehty lasketteluvälineiden kauppapaikaksi, jonne kirjautunut käyttäjä voi lisätä/poistaa oman julkaisun, kommentoida muiden julkaisuja, katsoa julkaisuja kategorioittain ja lisätä julkaisuja suosikeiksi.

Sovelluksen päätoiminta on routes.py tiedostossa, josta käsitellään lomakkeista saadut tiedot PRG-mallilla, ja viemällä tiedot käsiteltäväksi muihin luokkiin. Sovelluksessa on otettu huomioon tietoturva SQL-injektioiden, XSS-haavoittuvuuksien ja CSRF-haavoittuvuuksien osalta.

## Käyttäjät

### Käyttäjä:
- Näkee mahdollisuuden lisätä ilmoituksen, ja näkee muiden käyttäjien lisäämiä ilmoituksia.
- Käyttäjä näkee omat ilmoituksensa ja voi muokata omia ilmoituksiaan painamalla ilmoituksen auki.

- käyttäjä voi hakea ilmoituksia sanahaulla.
- voi lisätä omia ilmoituksia sekä tarkastella muiden ilmoituksia. 

### Ylläpitäjä:
- Ylläpitäjä on olemassa admin - admin tunnuksilla, mutta toiminnallisuutta ei tällä hetkellä ole.


## Ohjelmiston tarjoamat toiminnallisuudet

Ilmoituksen tekeminen:
- Otsikko, alaotsikko, kuvat, tekstikenttä.
- Ilmoituksen tekeminen aukaisee uuden sivun jossa on kohdat jotka voi täyttää ilmoitusta varten.

Ilmoituksen poistaminen:
- Menemällä sivulle julkaisusi näet omat julkaisusi ja painamalla nappia poista julkaisu, voit poistaa julkaisusi.

Suosikiksi lisääminen:
- Painamalla etusivulla olevaa lisää suosikiksi nappia, voit lisätä julkaisun suosikkeihin.
- Voit poistaa julkaisun suosikeistasi menemällä suosikit sivulle ja painamalla ilmoituksessa olevaa poista suosikeista nappia.

Kategoriat:
- Menemällä kategoriat sivulle näet kategorioittain julkaisut.

Haku:
- Haku löytyy sivun oikeasta yläkulmasta ja haku kohdistuu tällä hetkellä Julkaisujen otsikoihin.

## Ohjelmiston kirjastot
Saat ohjelmiston kirjastot ladattua kun pip install -r requirements.txt





