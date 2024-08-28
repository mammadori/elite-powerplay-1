# elite-powerplay-1

Questo script automatizza la selezione e l'acquisto di materiali Power Play in Elite Dangerous.
È progettato per funzionare in combinazione con il gioco Elite Dangerous su un sistema operativo che abbia Python3
e che possa installare il modulo `pynput` per simulare le pressioni dei tasti.

Funzionalità principali:
- Simula la navigazione del menu Power Play per acquistare materiali in blocco.
- Automatizza la selezione di materiali e l'aumento della quantità fino a un massimo configurato.
- Include ritardi casuali tra le pressioni dei tasti per evitare rilevamenti come bot.

Come usare:
1. Assicurati che Python 3 e il modulo `pynput` siano installati sul tuo sistema.
2. Avvia Elite Dangerous e naviga fino al menu di Power Play dove puoi acquistare materiali.
3. Posiziona il cursore sulla prima voce.
4. Esegui questo script. Ritorna su Elite entro il timeout e inizierà automaticamente ad acquistare materiali secondo la configurazione.
5. Lo script può essere interrotto manualmente in qualsiasi momento premendo `Ctrl+C` nella console.

Licenza:
Questo script è rilasciato sotto la licenza WTFPL (Do What The Fuck You Want To Public License).
Puoi fare ciò che vuoi con questo script.
Copyright 2024 CMDR AffaGammaRanna.
