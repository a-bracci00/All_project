# La funzione aggiungi_riga_vuota legge un file di input, 
# aggiunge una riga vuota dopo ogni punto (.) 
# e salva il risultato in un file di output chiamato terzo.txt

import chardet

def aggiungi_riga_vuota(file_input, file_output):
    with open(file_input, 'rb') as f_input:
        raw_data = f_input.read()
        encoding_result = chardet.detect(raw_data)
        encoding = encoding_result['encoding']
    
    try:
        with open(file_input, 'r', encoding=encoding) as f_input:
            testo = f_input.read()
    except UnicodeDecodeError:
        print("Errore di decodifica durante la lettura del file.")
        return
    
    testo_formattato = ""
    inizio_frase = True
    
    for carattere in testo:
        testo_formattato += carattere
        
        if carattere == '.':
            inizio_frase = True
            testo_formattato += '\n\n'
        elif carattere.isalpha():
            inizio_frase = False
    
    with open(file_output, 'w', encoding='utf-8') as f_output:
        f_output.write(testo_formattato)


file_input = input("Inserisci il nome del file di input: ")
file_output = "terzo.txt"

aggiungi_riga_vuota(file_input, file_output)
print("Il file terzo.txt è stato creato con successo.")
