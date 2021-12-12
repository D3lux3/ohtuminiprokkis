# Ohtuminiprojekti

![GitHub Actions](https://github.com/D3lux3/ohtuminiprokkis/workflows/CI/badge.svg)

### Product backlog

<a href="https://docs.google.com/spreadsheets/d/18UunzrSmqwaxQoobDS-6G-ufC1mTFpKDdtghOMa9Yn4/">täällä</a>

### Definition of Done

Valmiissa ohjelmistossa määritellyt vaatimukset on analysoitu, suunniteltu, ohjelmoitu, testattu, dokumentoitu, integroitu muuhun ohjelmaan ja se on viety tuotantoympäristöön.
- user storyt testattu monipuolisesti
- ohjelma läpäisee CI:n, testikattavuus vähintään 70 %
- koodi on selkeää ja ylläpidettävää
- koodi on yhtenäistä ja noudattaa pylintissä määriteltyä tyyliä
- product backlog ja sprint backlog ovat ajan tasalla

Ohjelma on analysoitu sekä suunniteltu ryhmässä ennen ensimmäistä sprinttiä. Sen jälkeen ohjelmasta on ohjelmoitu minimum viable product eli MVP, mikä on dokumentoitu DocString periaatteiden mukaisesti. Ohjelmaan on myös toteutettu testejä.

### Tällä hetkellä

- Ohjelmassa on tietokantayhteys.
- Lukuvinkki tallentuu tietokantaan.
- Ohjelmassa on tekstipohjainen komentorivikäyttöliittymä lukuvinkin lisäystä varten.
- Käyttöliittymä lukee käyttäjän syötettä.
- Lukuvinkki on toteutettu omana luokkanaan.
- Lukuvinkkit voi tulostaa tietokannasta.
- Ohjelman testaus on aloitettu.

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komennot

### Ohjelma

Komennot suoritetaan virtuaaliympäristössä komennolla:

```bash
poetry shell
```

Ohjelma suoritetaan komennolla:

```bash
python3 src/main.py
```

### Testaus

Testit suoritetaan komennolla:

```bash
pytest src
```

### Pylint

Pylint raportti saadaan komennolla:

```bash
pylint src
```


### Coverage

Coverage raportti saadaan komennolla:

```bash 
coverage run --branch -m pytest; coverage html
```

Tämän hetkinen testikattavuus:
<img width="843" alt="Näyttökuva 2021-12-9 kello 14 15 08" src="https://user-images.githubusercontent.com/75832352/145394695-9b04ce98-dd38-4f03-9819-84868367cd14.png">


