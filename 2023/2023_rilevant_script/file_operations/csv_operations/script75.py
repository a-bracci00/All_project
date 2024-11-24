# operazione si file csv

def alberinomi(stringa):
    import csv
    with open('Alberi-Monumentali-Della-Campania.csv', 'r', encoding='utf-8', newline = '') as f:
        reader = csv.reader(f, delimiter=';')
        for x,y in enumerate(list(reader)[0]):
           print(y, x)
        #next(reader)
        for x in reader:
            if stringa.lower() in x[6].lower():
                print(x[6])

alberinomi('tiglio')