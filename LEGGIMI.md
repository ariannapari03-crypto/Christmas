# Liste di Natale

Un'app per le liste dei regali di famiglia. Ognuno ha la sua lista, chi regala tocca
"Lo prendo io" e tutti vedono subito cosa è ancora libero.
Chi riceve il link lo apre e basta: niente account, niente email.

## Messa in linea (una volta sola, circa 10 minuti)

### 1. Crea il database gratuito su Firebase
1. Vai su https://console.firebase.google.com ed entra con il tuo account Google.
2. Clicca **Crea un progetto** e chiamalo per esempio `liste-natale`. Google Analytics non serve: puoi disattivarlo.
3. Nel menu a sinistra apri **Crea → Firestore Database** e clicca **Crea database**.
   Scegli la località `eur3 (Europe)` e poi **Avvia in modalità di produzione**.

### 2. Incolla le regole di accesso
In Firestore apri la scheda **Regole**, cancella quello che c'è, incolla tutto il contenuto
del file `firestore.rules` di questo progetto e clicca **Pubblica**.

### 3. Prendi la configurazione dell'app
1. Torna alla pagina iniziale del progetto (l'icona della casetta) e clicca sull'icona **</>** (Web).
2. Dai un nome qualsiasi, lascia **non** spuntato "Firebase Hosting" e clicca **Registra app**.
3. Firebase ti mostra un blocco `const firebaseConfig = { apiKey: ..., projectId: ..., ... }`.
   Copialo e incollalo in `config.js` al posto di `null`
   (oppure mandalo a Claude, che lo inserisce per te). Questi valori non sono segreti.

### 4. Pubblica il sito con GitHub Pages
1. Su GitHub apri il repository → **Settings → Pages**.
2. In "Build and deployment" scegli **Deploy from a branch**, seleziona il branch con l'app e la cartella `/ (root)`, poi clicca **Save**.
3. Dopo un minuto l'indirizzo del sito compare in alto in quella pagina
   (sarà simile a `https://ariannapari03-crypto.github.io/Christmas/`).

### 5. Il link per la famiglia
In `config.js` la voce `family` fissa lo spazio della famiglia: chiunque apra l'indirizzo del sito
vede sempre le stesse liste. C'è un solo link da mandare, quello del sito, senza niente dopo.

## Da sapere
- Chi ha il link può vedere e modificare le liste, come un documento Google condiviso con "chiunque abbia il link".
  Mandalo solo in famiglia. Il codice della famiglia è in `config.js`, quindi è visibile a chi guarda il repository pubblico.
- Il piano gratuito di Firebase basta e avanza: 50.000 letture e 20.000 modifiche al giorno.
- `artifact-claude.html` è la versione di anteprima per claude.ai: si rigenera da `index.html` con `python3 build-artifact.py`.
