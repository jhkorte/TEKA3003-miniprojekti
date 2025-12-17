# TEKA3003-miniprojekti
Ryhmä 8 repositorio

[![CI](https://github.com/jhkorte/TEKA3003-miniprojekti/actions/workflows/main.yml/badge.svg)](https://github.com/jhkorte/TEKA3003-miniprojekti/actions)
[![CI](https://codecov.io/github/jhkorte/TEKA3003-miniprojekti/badge.svg)](https://app.codecov.io/github/jhkorte/TEKA3003-miniprojekti)

[Project Backlog](https://jyu-my.sharepoint.com/:x:/g/personal/jhkortww_jyu_fi/EaBAMkVj-MRMu468sCmiTtgBthz1bZm2LLCxn55WsWJ2Kg?e=lhiNUf)

---------------------------------------

# Ohjelman asennus ja suorittaminen

Siirry hakemistoon, johon olet kloonannut projektin. Suorita sitten seuraavat komennot.

```bash
poetry install
poetry shell
python src/main.py

```
# Dropbox konfiguraatio
Luo ensiksi dropboxiin appi DBX Platformiin.

Kopioi selaimeen, lisää app-key dropboxin hallinnasta:
https://www.dropbox.com/oauth2/authorize?client_id=<APP_KEY>&response_type=code&token_access_type=offline

Kopioi code= kohdan jälkeen oleva authorization code.

Komentolinjalla suorita:
```bash
curl https://api.dropbox.com/oauth2/token \
    -d code=<YOUR_AUTHORIZATION_CODE> \
    -d grant_type=authorization_code \
    -d client_id=<YOUR_APP_KEY> \
    -d client_secret=<YOUR_APP_SECRET>
```
Kopioi saamasi refresh token.
Luo projektin pääkansioon tiedosto .env ja lisää sisälle:
```bash
DROPBOX_APP_KEY=KOODI
DROPBOX_APP_SECRET=KOODI
DROPBOX_REFRESH_TOKEN=KOODI
```
---------------------------------------

# Definition of done
Sovellus toimii komentorivikäyttöliittymässä.
- Kaikki käyttäjän kannalta tarpeelliset komennot ja ominaisuudet on toteutettu ja ne toimivat.
- Testikattavuus on kohtuullisella tasolla.
- Automatisoidut testit.
- Koodi on selkeää ja hyvin kommentoitua.

---------------------------------------

# Raportti
https://docs.google.com/document/d/1w1rpHdt5EpWcX8nfXDhhCVPwJ2st1gTR5jzENkY55Fo/edit?usp=sharing

