import os
import zipfile
from PIL import Image
from reportlab.pdfgen import canvas
import shutil

# Funzione per estrarre le immagini da un file .cbz e salvarle in una cartella temporanea
def extract_images_from_cbr(cbr_file, temp_dir):
    """
    Estrai le immagini da un file .cbr e salvale in una cartella temporanea.
    
    Args:
    - cbr_file: Percorso del file .cbr da cui estrarre le immagini.
    - temp_dir: Cartella temporanea in cui estrarre le immagini.
    
    Returns:
    - images: Lista dei percorsi delle immagini estratte.
    """
    images = []  # Lista per memorizzare i percorsi delle immagini estratte
    with zipfile.ZipFile(cbr_file, 'r') as zip_ref:
        # Itera su tutti i file nel file .cbr (che è un file zip)
        for file in zip_ref.namelist():
            # Estrae solo i file che sono immagini (.png, .jpg, .jpeg, .bmp, .gif)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                zip_ref.extract(file, temp_dir)  # Estrai il file nella cartella temporanea
                # Aggiungi il percorso dell'immagine alla lista
                images.append(os.path.join(temp_dir, file))
    return images  # Restituisce la lista delle immagini estratte

# Funzione per convertire una lista di immagini in un file PDF
def images_to_pdf(images, output_pdf):
    """
    Converte una lista di immagini in un file PDF.
    
    Args:
    - images: Lista di percorsi delle immagini da inserire nel PDF.
    - output_pdf: Percorso del file PDF di output.
    """
    c = canvas.Canvas(output_pdf)  # Crea un oggetto Canvas per generare il PDF
    for image in images:
        img = Image.open(image)  # Apre l'immagine
        width, height = img.size  # Ottieni le dimensioni dell'immagine
        c.setPageSize((width, height))  # Imposta la dimensione della pagina del PDF uguale all'immagine
        c.drawImage(image, 0, 0, width, height)  # Disegna l'immagine nel PDF
        c.showPage()  # Aggiungi una nuova pagina per la prossima immagine
    c.save()  # Salva il PDF

# Funzione principale che converte un file .cbr in un file .pdf
def convert_cbr_to_pdf(cbr_file, output_pdf):
    """
    Converte un file .cbr in un file .pdf.
    
    Args:
    - cbr_file: Percorso del file .cbr da convertire.
    - output_pdf: Percorso del file PDF di output.
    """
    # Crea una cartella temporanea per contenere le immagini estratte dal .cbr
    temp_dir = os.path.join(os.path.dirname(cbr_file), 'temp_images')
    os.makedirs(temp_dir, exist_ok=True)  # Crea la cartella temporanea (non fallisce se esiste già)

    try:
        # Estrai le immagini dal file .cbr nella cartella temporanea
        images = extract_images_from_cbr(cbr_file, temp_dir)
        
        # Converte le immagini estratte in un file PDF
        images_to_pdf(images, output_pdf)
        print(f"Conversione completata in: {output_pdf}")  # Stampa un messaggio di completamento
    finally:
        # Rimuovi la cartella temporanea e le immagini estratte
        shutil.rmtree(temp_dir)  # Cancella la cartella temporanea (insieme alle immagini)
        print(f"Cartella temporanea e immagini rimosse da: {temp_dir}")  # Stampa un messaggio di rimozione

# Funzione che converte tutti i file .cbz in una cartella in file PDF nella cartella di destinazione
def convert_all_cbr_in_directory(directory_path, output_directory):
    """
    Converte tutti i file .cbz nella cartella di input in file PDF nella cartella di output.
    
    Args:
    - directory_path: Percorso della cartella contenente i file .cbz da convertire.
    - output_directory: Percorso della cartella in cui salvare i file PDF di output.
    """
    # Ottieni tutti i file .cbz nella directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.cbz'):  # Controlla se il file è un file .cbz
            cbr_file = os.path.join(directory_path, filename)  # Percorso completo del file .cbz
            
            # Definisci il nome del file PDF di output, rimuovendo la parte iniziale del nome (prima del primo '_')
            output_pdf = os.path.join(output_directory, f"{os.path.splitext(filename)[0][:filename.index('_')]}.pdf")
            
            # Controlla se il file PDF esiste già
            if os.path.exists(output_pdf):
                print(f"Il file {output_pdf[len(directory_path)+1:]} esiste già. Conversione saltata.")
                continue  # Se il file PDF esiste già, salta la conversione di questo file .cbz
            
            # Converte il file .cbz in .pdf
            convert_cbr_to_pdf(cbr_file, output_pdf)

# Esempio di utilizzo:
input_directory = "convertitore_cbz_to_pdf"  # Cartella contenente i file .cbz da convertire
output_directory = "convertitore_cbz_to_pdf"  # Cartella di destinazione per i PDF generati

# Converte tutti i file .cbz nella cartella di input in file PDF nella cartella di output
convert_all_cbr_in_directory(input_directory, output_directory)
