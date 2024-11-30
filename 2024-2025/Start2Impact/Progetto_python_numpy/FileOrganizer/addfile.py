import os
import csv
import shutil
import argparse

def smista_file_with_info(path : str, user_input : str) -> list[dict]:

    """
        Smista i file in base alla loro estensione e ne recupera le informazioni.

        Args:
            path (str): Il percorso della directory di origine.
            user_input (str): Il nome del file da cercare.
        
        Returns:
            lista_diz [str]: Lista contenente i dizionari con le varie info.
    """

    # Creazione di una lista per contenere i vari dizionari
    lista_diz = []

    # Creo un dizionario per contenere i formati e le rispettive cartelle in base alle estensioni 'ext : [formato, nome cartella]'
    estensioni = {
        'png': ['image', 'images'],
        'jpg': ['image', 'images'],
        'jpeg': ['image', 'images'],
        'mp3' : ['audio', 'audio'],
        'txt' : ['doc', 'docs'],
        'odt' : ['doc', 'docs']
    }
    
    # Crea tre variabili distinte per contenere il nome, il estensione e la grandezza in byte

    nome = user_input.split('.')[0]
    estensione = user_input.split('.')[1]
    size = str(os.path.getsize(path+'\\'+user_input))

    # In base al estensione crea una directory
    # Per poi spostare il file dal vecchio path al nuovo
    if estensione in estensioni:
        # Definisco il path della cartella (nome) aggiungendo il estensione al path
        nome_dir = path+f'\\{estensioni[estensione][1]}'
        # Creo la cartella se non già esistente
        os.makedirs(nome_dir, exist_ok=True)
        # Sposto il file nella cartella tramite la funzione sposta_file()
        sposta_file(path, nome_dir, user_input)

    else:
        print(nome + estensione, 'Estensione non gestibile')

    # Mostro a schermo i vari file iterati
    print(nome, f'type:{estensioni[estensione][0]}', f'size:{size}B')

    # Creo la struttura dei dizionari per contenere le info dei file e li inserisco nella lista
    lista_diz.append({
        'name' : nome,
        'type' : estensione,
        'size(B)' : size})

    # Ritorno la lista di dizionari con le info
    return lista_diz

def scrivi_recap(path : str, lista_diz : list) -> None:

    """
        Crea o modifica un file CSV di recap.

        Args:
            path (str): Il percorso della directory di destinazione.
            lista_diz [str]: Lista contenente i dizionari.
        
        Returns:
            None
    """

    # Se ci sono degli elementi da scrivere
    if lista_diz:

        # Verifico se il file sia già esistente e se esiste cambio il valore di exists
        if os.path.exists(path+'\\recap.csv'):
            exists = True
        else:
            exists = False
        
        # Apro il file in append mode
        with open(path + '\\recap.csv', 'a', newline='', encoding='utf-8') as f:
            
            # Definisco lo scrittore e le intestazioni
            writer = csv.DictWriter(f, fieldnames=['name', 'type', 'size(B)'])

            # Se il file viene creato per la prima volta inserisco le intestazioni
            if exists == False:
                writer.writeheader()

            # Scrivo il dizionario nel file
            writer.writerows(lista_diz)

# Sposta il file da una cartella all'altra
def sposta_file(initial_path : str, final_path : str, file_name : str ) -> None:

    """
        Sposta un file da una directory di origine a una directory di destinazione.

        Args:
            initial_path (str): Il percorso della directory di origine.
            final_path (str): Il percorso della directory di destinazione.
            file_name (str): Il nome del file da spostare.
        
        Returns:
            None
    """

    # Prendo il path iniziale del file
    initial_path = initial_path+f'\\{file_name}'
    # Prendo il path finale del file
    final_path_with_file = final_path+f'\\{file_name}'

    # Se il file di destinazione esiste, crea un nuovo nome
    if os.path.exists(final_path_with_file):

        # Estraggo il nome e l'estensione
        base, ext = os.path.splitext(file_name)
        # Creo un counter
        i = 0
        # Ricompongo il nome del file
        new_name = f"{base}{ext}"
        # Creo il nuovo path
        new_dst_path = os.path.join(final_path, new_name)

        # Finchè il path esiste, riprovo modificando il nome del file
        while os.path.exists(new_dst_path):
            # Aggiorno il counter
            i += 1
            # Inserisco il nuovo numero nel nome
            new_name = f"{base}_{i}{ext}"
            # Creo il nuovo path
            new_dst_path = os.path.join(final_path, new_name)
        # Assegno il nuovo path alla variabile final path
        final_path = new_dst_path

    # Sposto il file
    shutil.move(initial_path, final_path)

def quale_file(path : str) -> None:

    """
        Prende un file di quelli presenti nella directory in input e lo sposta.

        Args:
            path (str): Il percorso della directory dei file.

        Returns:
            None
    """

    # Creo una descrizione per l'uso dell'utente  
    parser = argparse.ArgumentParser(description=" Selezionare un file tra quelli presenti nella directory.")
    # Spiego l'argomento di input
    parser.add_argument('input', type=str, help="python addfile.py [example.ext]", choices=sorted([x for x in os.listdir(path) if len(os.path.splitext(x)[1]) > 0 and x != 'recap.csv']))

    # Eseguo il parsing dell'input
    args = parser.parse_args()
    # Prendo il file da spostare
    user_input = args.input

    # Stampo l'input dell'utente
    print(f"Hai scelto: {user_input}")

    # Creo la lista di dizionari contenente le infomazioni del file tramite la funzione smista_file_with_info()
    lista_diz = smista_file_with_info(path, user_input)
    # Creo o modifico il recap tramite la funzione scrivi_recap() e la lista contenente le info
    scrivi_recap(path, lista_diz)
    # Stampo il messaggio di successo
    print(f'File {user_input} spostato con successo.')


if __name__ == '__main__':

    # Definisco la variabile path_files con la directory da dove prendere i file
    path_files = 'files'
    # Uso la funzione per selezionare il file
    quale_file(path_files)

