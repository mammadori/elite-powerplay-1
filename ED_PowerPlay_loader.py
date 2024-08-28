#!/usr/bin/env python3
# Copyright 2024 CMDR AffaGammaRanna
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.WTF Licence

"""
Questo script automatizza la selezione e l'acquisto di materiali Power Play in Elite Dangerous.
È progettato per funzionare in combinazione con il gioco Elite Dangerous su un sistema operativo Linux
utilizzando il modulo `pynput` per simulare le pressioni dei tasti.

Funzionalità principali:
- Simula la navigazione del menu Power Play per acquistare materiali in blocco.
- Automatizza la selezione di materiali e l'aumento della quantità fino a un massimo configurato.
- Include ritardi casuali tra le pressioni dei tasti per evitare rilevamenti come bot.

Come usare:
1. Assicurati che Python 3 e il modulo `pynput` siano installati sul tuo sistema.
2. Avvia Elite Dangerous e naviga fino al menu di Power Play dove puoi acquistare materiali.
3. Posiziona il cursore sulla prima voce.
4. Esegui questo script. Lo script inizierà automaticamente ad acquistare materiali secondo la configurazione.
5. Lo script può essere interrotto manualmente in qualsiasi momento premendo `Ctrl+C` nella console.

Licenza:
Questo script è rilasciato sotto la licenza WTFPL (Do What The Fuck You Want To Public License).
Puoi fare ciò che vuoi con questo script.
Copyright 2024 CMDR AffaGammaRanna.
"""



from time import sleep
from random import uniform
from pynput.keyboard import Controller, Key

# Configurazioni globali
CARGO_MAX = 796              # Carico massimo della nave
MATERIALS_PER_BUY = 25       # Numero di pressioni del tasto "Destra" per comprare i materiali

# Calcola il numero massimo di cicli necessario per raggiungere o superare il carico massimo
max_loops = (CARGO_MAX + MATERIALS_PER_BUY - 1) // MATERIALS_PER_BUY

# Ritardi configurabili (in secondi, ridotti del 20%)
DELAY_BETWEEN_KEYS = 0.08        # Ritardo tra le pressioni dei tasti direzionali (80ms)
DELAY_AFTER_SPACE = 0.56         # Ritardo dopo la pressione del tasto "Spazio" (560ms)
DELAY_AFTER_SELECTION = 1.2      # Ritardo dopo la selezione con "Spazio" (1200ms)
PRESS_RELEASE_DELAY = 0.04       # Ritardo tra pressione e rilascio di un tasto (40ms)
RANDOM_DELAY_VARIATION = 0.02    # Variazione casuale del ritardo (20ms)

# Debug configurazione
DEBUG = True  # Cambia a False per disattivare i messaggi di debug

# Inizializza il controller della tastiera
keyboard = Controller()

def debug_print(message):
    """Stampa messaggi di debug se la modalità di debug è attiva."""
    if DEBUG:
        print(message)

def countdown(seconds):
    """Effettua un conto alla rovescia prima di iniziare l'operazione."""
    for i in range(seconds, 0, -1):
        print(f"Avvio in {i} secondi...")
        sleep(1)

def get_random_delay(base_delay):
    """Ritorna un ritardo casuale intorno al ritardo base."""
    return base_delay + uniform(-RANDOM_DELAY_VARIATION, RANDOM_DELAY_VARIATION)

def send_key(key, delay=DELAY_BETWEEN_KEYS):
    """Invia un tasto con un piccolo ritardo tra press e release e un ritardo casuale."""
    keyboard.press(key)
    sleep(PRESS_RELEASE_DELAY)  # Ritardo tra press e release
    keyboard.release(key)
    sleep(get_random_delay(delay))  # Ritardo casuale dopo il rilascio del tasto

def perform_cycle():
    """Esegue un ciclo completo di operazioni per acquistare materiali Power Play in Elite Dangerous."""
    # Scorri verso il basso due volte per selezionare l'opzione
    for _ in range(2):
        send_key(Key.down)

    # Premi "Spazio" per selezionare l'opzione
    send_key(Key.space, DELAY_AFTER_SPACE)

    # Premi "Destra" per aumentare la quantità
    for _ in range(MATERIALS_PER_BUY):
        send_key(Key.right)

    # Premi "Spazio" per confermare
    send_key(Key.space, DELAY_AFTER_SPACE)
   
    # Attendi e premi "Spazio" di nuovo per continuare
    send_key(Key.space, DELAY_AFTER_SELECTION)

# Loop principale
if __name__ == "__main__":
    countdown(5)  # Effettua un conto alla rovescia di 5 secondi prima di iniziare

    for i in range(max_loops):
        debug_print(f"Inizio ciclo {i + 1}")
        perform_cycle()
        debug_print(f"Ciclo {i + 1} completato.")

    print("Operazione completata. Numero massimo di cicli raggiunto o carico massimo soddisfatto.")
