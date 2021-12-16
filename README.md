# Ohtuminiprojekti

![GitHub Actions](https://github.com/D3lux3/ohtuminiprokkis/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/D3lux3/ohtuminiprokkis/branch/main/graph/badge.svg?token=BPB8EMSJC8)](https://codecov.io/gh/D3lux3/ohtuminiprokkis)

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
- Lukuvinkkit voi tulostaa tietokannasta.
- käyttäjä voi tallentaa kirja, video, blogpost, sekä podcast tyyppisiä lukuvinkkejä
- lukuvinkille voi tallentaa tagin tai liittyvän kurssin, joiden perusteella voi hakea lukuvinkkejä
- lukuvinkkejä voi poistaa
- voi hakea satunnaisen lukuvinkin

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


