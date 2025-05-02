from PIL import Image  # Importa la libreria Pillow per lavorare con immagini

def unisci_immagini_verticalmente(img1_path, img2_path, output_path):
    """
    Unisce due immagini in verticale (una sopra l'altra) e salva il risultato in un nuovo file.

    Parametri:
    - img1_path (str): percorso del file della prima immagine
    - img2_path (str): percorso del file della seconda immagine
    - output_path (str): percorso del file dove salvare l'immagine unita
    """

    # Apri le due immagini dai percorsi indicati
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Calcola la larghezza massima tra le due immagini
    larghezza_totale = max(img1.width, img2.width)
    # Calcola l'altezza totale sommando le altezze delle due immagini
    altezza_totale = img1.height + img2.height

    # Crea una nuova immagine vuota (sfondo bianco) con le dimensioni combinate
    immagine_unita = Image.new('RGB', (larghezza_totale, altezza_totale), (255, 255, 255))

    # Incolla la prima immagine nella parte superiore della nuova immagine
    immagine_unita.paste(img1, (0, 0))
    # Incolla la seconda immagine immediatamente sotto la prima
    immagine_unita.paste(img2, (0, img1.height))

    # Salva l'immagine unita nel percorso specificato
    immagine_unita.save(output_path)

    # Stampa un messaggio di conferma
    print(f"Immagine salvata in: {output_path}")

# Esempio di utilizzo della funzione
unisci_immagini_verticalmente("input1.png", "input2.png", "output.png")
