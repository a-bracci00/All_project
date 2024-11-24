# Qualche operazione semplice su dei file json

import json

with open('bike-sharing-lavis.json', encoding='utf-8') as f:
    contenuto_python = json.load(f)
    print(contenuto_python)
    print()
    for riga in contenuto_python:
        print(riga)
    print()
    print(type(contenuto_python))
    print()
    for riga in contenuto_python:
        print(type(riga))
    print()
    print(contenuto_python[0])
    print()
    print(contenuto_python[0]['address'])
    print()
    print(contenuto_python[0]['position'])
    print()
    for riga in contenuto_python[0]:
        print(riga)
print()

with open('impiegati.jsonl', encoding='utf-8') as f:
    lista_testi_json = list(f)
    print(lista_testi_json)
    print()
    i = 0
    for testo_json in lista_testi_json:
        print(type(testo_json))
        contenuto_python = json.loads(testo_json)
        print('Oggetto ', i)
        print(contenuto_python)
        i = i + 1
print()