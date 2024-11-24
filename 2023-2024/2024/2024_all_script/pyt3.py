# La funzione ordina_frasi legge un file di testo contenente frasi, 
# le ordina in ordine alfabetico e salva il risultato in un nuovo file chiamato output.txt

def ordina_frasi():
    # Richiede all'utente di fornire il percorso del file di input
    file_input = input("Inserisci il percorso del file di input: ")

    try:
        # Legge il contenuto del file di input utilizzando la codifica 'utf-8'
        with open(file_input, 'r', encoding='utf-8') as input_file:
            frasi = input_file.readlines()

        # Rimuove i caratteri di spazio iniziali e finali e converte in minuscolo le frasi
        frasi = [frase.strip().lower() for frase in frasi]

        # Ordina le frasi in ordine alfabetico
        frasi_ordinate = sorted(frasi)

        # Crea il nuovo file di output con le frasi ordinate
        file_output = 'output.txt'
        with open(file_output, 'w') as output_file:
            for frase in frasi_ordinate:
                output_file.write(frase + '\n')

        print("Frasi ordinate con successo. Il risultato è stato salvato nel file 'output.txt'.")
    except FileNotFoundError:
        print("File non trovato. Assicurati di inserire un percorso corretto.")

# Chiama la funzione per ordinare le frasi
ordina_frasi()

