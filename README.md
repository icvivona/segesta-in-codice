# Segesta in codice · Segesta in code

[Italiano](#italiano) · [English](#english)

Presentazioni per la classe del laboratorio di coding *Segesta in codice*, proposto dall'IC "Francesco Vivona" di Calatafimi Segesta (Trapani, Sicilia) per la EU Code Week e per l'alleanza CodeWeek4All.

Classroom presentations for the *Segesta in code* coding lab, proposed by IC "Francesco Vivona" in Calatafimi Segesta (Trapani, Sicily, Italy) for EU Code Week and the CodeWeek4All alliance.

---

## Italiano

### Che cos'è

Un laboratorio di 75 minuti con Tinkercad Codeblocks per alunni di 11–14 anni. A squadre di 2–3, gli alunni costruiscono in 3D la facciata del tempio dorico di Segesta: tre gradini, sei colonne, la trabeazione e il frontone. Un ciclo «ripeti» costruisce le colonne e quattro variabili (N, P, R, H) cambiano l'intero modello.

Le presentazioni hanno 15 slide, con la stessa struttura in italiano e in inglese, così le classi partner possono confrontare i passaggi slide per slide.

### Come si guardano

- **Online:** [NOMEUTENTE].github.io/segesta-in-codice (dopo la pubblicazione con GitHub Pages).
- **Sul computer:** scarica la cartella e apri `index.html` o una delle presentazioni con Chrome, Edge o Firefox.
- **In PDF:** i PDF di ogni versione sono allegati alla pagina *Releases* del repository.

Le slide sono pensate per lo schermo di un computer o per il proiettore; sul telefono si rimpiccioliscono per stare nella pagina.

### Contenuto della cartella

| File o cartella | Che cos'è |
| --- | --- |
| `index.html` | Pagina iniziale bilingue con i link alle due presentazioni |
| `presentazione-classe-IT.html` | Presentazione per la classe in italiano (15 slide) |
| `presentazione-classe-EN.html` | La stessa presentazione in inglese |
| `assets/fonts/` | Caratteri Fredoka e Nunito con le loro licenze (SIL Open Font License 1.1) |
| `assets/tempio-segesta.jpg` | Foto del tempio usata in copertina |
| `esporta-pdf.py` | Script facoltativo per rigenerare i PDF |
| `CHANGELOG.md` | Registro delle modifiche, versione per versione |
| `LICENZE.md` | Licenze dei materiali, dei caratteri e della foto |
| `PUBBLICARE.md` | Guida passo passo per pubblicare e aggiornare il repository su GitHub |

### Come si modifica

1. Apri il file `.html` con un editor di testo (per esempio Visual Studio Code o Blocco note).
2. Cambia solo i testi tra i tag; lascia com'è il codice che disegna blocchi e modello 3D.
3. Salva e riapri il file nel browser per controllare.
4. Annota la modifica in `CHANGELOG.md`.

### Come si rigenerano i PDF

Serve Python 3 con Playwright (`pip install playwright` e poi `playwright install chromium`).

```
python esporta-pdf.py            # crea entrambi i PDF nella cartella pdf/
python esporta-pdf.py presentazione-classe-IT.html
```

### Tradurre in un'altra lingua

Le scuole partner possono aggiungere una lingua: copia `presentazione-classe-EN.html` in un nuovo file (per esempio `presentazione-classe-ES.html`), traduci solo i testi, cambia l'attributo `lang` in cima al file e aggiungi il link in `index.html`. Le etichette dei blocchi devono corrispondere a quelle che Tinkercad mostra in quella lingua: controllale aprendo Codeblocks.

### Privacy

Il repository contiene solo materiali didattici: nessun dato, nome o immagine di alunni.

### Contatti

prof. Livio Di Franco, Animatore Digitale, IC "Francesco Vivona", Calatafimi Segesta (TP) · [EMAIL-REFERENTE]

---

## English

### What it is

A 75-minute lab with Tinkercad Codeblocks for students aged 11–14. In teams of 2–3, students build a 3D model of the façade of the Doric temple of Segesta: three steps, six columns, the entablature and the pediment. A "repeat" loop builds the columns and four variables (N, P, R, H) change the whole model.

The presentations have 15 slides with the same structure in Italian and English, so partner classes can compare the steps slide by slide.

### How to view them

- **Online:** [NOMEUTENTE].github.io/segesta-in-codice (once published with GitHub Pages).
- **On a computer:** download the folder and open `index.html` or one of the presentations in Chrome, Edge or Firefox.
- **As PDF:** the PDFs of each version are attached to the repository's *Releases* page.

The slides are designed for a computer screen or a projector; on a phone they shrink to fit the page.

### How to edit

1. Open the `.html` file in a text editor (for example Visual Studio Code).
2. Change only the text between the tags; leave the code that draws the blocks and the 3D model as it is.
3. Save and reopen the file in the browser to check.
4. Record the change in `CHANGELOG.md`.

### Regenerating the PDFs

You need Python 3 with Playwright (`pip install playwright`, then `playwright install chromium`), then run `python esporta-pdf.py`. The PDFs are saved in the `pdf/` folder.

### Translating into another language

Partner schools can add a language: copy `presentazione-classe-EN.html` to a new file (for example `presentazione-classe-ES.html`), translate only the text, change the `lang` attribute at the top of the file and add the link to `index.html`. Block labels must match those Tinkercad shows in that language: check them by opening Codeblocks.

### Privacy

The repository contains teaching materials only: no student data, names or images.

### Contact

Prof. Livio Di Franco, Digital Coordinator, IC "Francesco Vivona", Calatafimi Segesta (TP), Italy · [EMAIL-REFERENTE]
