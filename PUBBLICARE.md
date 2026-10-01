# Pubblicare e aggiornare il repository su GitHub

Guida per l'Animatore Digitale. Serve una sola volta per la pubblicazione; poi bastano i passi della sezione «Aggiornare». Le voci dei menu di GitHub possono cambiare leggermente nel tempo.

## Prima di pubblicare

- [ ] Licenza confermata con il dirigente (`LICENZE.md`).
- [ ] Foto del tempio verificata o sostituita (`LICENZE.md`).
- [ ] `[EMAIL-REFERENTE]` sostituito in `README.md` e in `index.html`.

## 1. Creare l'account e il repository

1. Crea un account gratuito su github.com, preferibilmente con l'email istituzionale. Il nome utente comparirà nell'indirizzo del sito (per esempio `icvivona.github.io`).
2. Installa GitHub Desktop (desktop.github.com) e accedi con l'account.
3. Scompatta la cartella `segesta-in-codice` dove vuoi tenerla sul computer.
4. In GitHub Desktop: **File → Add local repository**, scegli la cartella. GitHub Desktop segnala che non è ancora un repository: clicca **create a repository**, lascia il nome `segesta-in-codice` e conferma.
5. Clicca **Publish repository**. Togli la spunta da **Keep this code private**: GitHub Pages è gratuito solo per i repository pubblici.

## 2. Attivare la pagina web (GitHub Pages)

1. Su github.com apri il repository e vai in **Settings → Pages**.
2. In **Build and deployment** scegli **Deploy from a branch**, poi il ramo **main** e la cartella **/ (root)**, e salva.
3. Dopo qualche minuto la pagina è online all'indirizzo `https://NOMEUTENTE.github.io/segesta-in-codice/`.
4. Sostituisci `[NOMEUTENTE]` in `README.md` e in `index.html` con il tuo nome utente e pubblica la modifica (sezione 4).

## 3. Allegare i PDF a una versione (Release)

1. Rigenera i PDF con `python esporta-pdf.py` oppure usa quelli già pronti.
2. Su github.com, nella colonna a destra del repository, clicca **Releases → Create a new release** (o **Draft a new release**).
3. Come tag scrivi la versione del `CHANGELOG.md` (per esempio `v1.0.0`), incolla le righe del changelog nella descrizione e trascina i due PDF nell'area degli allegati.
4. Pubblica. Copia il link della pagina Releases in `index.html` al posto di `[LINK-RELEASES]`.

## 4. Aggiornare

1. Modifica i file sul computer e annota la modifica in `CHANGELOG.md`, facendo salire il numero di versione.
2. Apri GitHub Desktop: a sinistra vedi i file cambiati, a destra le righe modificate.
3. In basso a sinistra scrivi un riassunto breve (per esempio «Corretto testo slide 9») e clicca **Commit to main**, poi **Push origin**.
4. Per una versione importante crea una nuova Release con i PDF aggiornati.

## 5. Accettare una traduzione da una scuola partner

Il docente partner, con il suo account GitHub, apre il repository, clicca **Fork**, aggiunge il file tradotto e propone la modifica con una **Pull request**. Tu la trovi nella scheda **Pull requests**: controlli i file e clicchi **Merge pull request**. Ricordati di aggiungere la lingua in `index.html` e nel `CHANGELOG.md`.

## 6. Copia su Drive

Ad ogni versione importante comprimi la cartella in uno ZIP e caricalo su Drive in `02_Laboratorio_Segesta/Sorgenti` come nuova versione del file esistente (**Gestisci versioni → Carica nuova versione**), poi scegli **Conserva per sempre** su quella versione. Nella colonna «Materiali e link» dell'archivio delle attività (riga 2026-S1) incolla il link del repository.
