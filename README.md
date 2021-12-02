# Ohtuminiprojekti


### Product backlog

<a href="https://docs.google.com/spreadsheets/d/18UunzrSmqwaxQoobDS-6G-ufC1mTFpKDdtghOMa9Yn4/">täällä</a>

### Definition of Done

Valmis ohjelmisto tarkoittaa sitä, että määritelty vaatimus on analysoitu, suunniteltu, ohjelmoitu, testattu, dokumentoitu, integroitu muuhun ja viety tuotantoympäristöön.

Ohjelma on analysoitu sekä suunniteltu ryhmässä ennen ensimmäistä sprinttiä. Sen jälkeen ohjelmasta on ohjelmoitu minimum viable product eli MVP, mikä on dokumentoitu DocString periaatteiden mukaisesti. Ohjelmaan on myös toteutettu testejä.

- Ohjelmassa on tietokantayhteys.
- Lukuvinkki tallentuu tietokantaan.
- Ohjelmassa on tekstipohjainen komentorivikäyttöliittymä lukuvinkin lisäystä varten.
- Käyttöliittymä lukee käyttäjän syötettä.
- Lukuvinkki on toteutettu omana luokkanaan.
- Lukuvinkkejä voi hakea tietokannasta ja ne voi tulostaa.
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

