# Definition of done

User storyt ovat sprintin päätteeksi asiakkaalle esiteltävissä ja valmiita silloin kun ne täyttävät seuraavat hyväksymiskriteerit:

## Yleisesti

- Sovellus toteuttaa user storyn kuvaaman toiminnallisuuden ja sitä on mahdollisuus käyttää käyttöliittymän kautta
- User storyt on jaettu teknisiin taskeihin, joiden työmäärä on estimoitu ja user storyjen kannalta välttämättömät taskit on tehty
- Dokumentaatio on päivitetty, käytetyt työtunnit on merkitty ja burndown-kaavio on saatavilla

## Testaus

- Frontendin toiminnallisuutta on testattu manuaalisesti yleisimpien oikeiden sekä virheellisten käyttötilanteiden kannalta
- Backendin tarjoama REST api on testattu kattavasti user storyyn liittyvän toiminnallisuuden osalta

## CI/CD

- Backend ja frontend läpäisevät Circlen suorittaman buildauksen ja testit
- Frontend on bundlattu backendin juureen ja koko stack on viety tuotantoon Herokuun
