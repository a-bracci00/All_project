#La funzione modifica una frase aggiungendo un'espressione sentimentale all'inizio o alla fine, 
# in base al tipo di sentimento e alla sua posizione indicata nel dizionario sentimenti

sentimenti = {
                1: {
                    "espressione": "Gulp!",
                    "posizione": "i"},
                2: {
                    "espressione": "Sgaragulp !",
                    "posizione": "i"},
                3: {
                    "espressione": "Uff..",
                    "posizione": "f"}}

def onomat(frase, sentimento, sentimenti):
    #for x in range(len(sentimenti)):
    if sentimenti[sentimento]['posizione'] == 'i':
        return sentimenti[sentimento]['espressione'] + ' ' + frase
    elif sentimenti[sentimento]['posizione'] == 'f':
        return frase + ' ' + sentimenti[sentimento]['espressione']
    
print(onomat("Ma quelli sono i bassotti!", 1, sentimenti))
print(onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti))
# INIZIO TEST - NON TOCCARE !!!
sentimenti = {
1: { "espressione": "Gulp!",
"posizione": "i"
},
2: { "espressione": "Sgaragulp!",
"posizione": "i"
},
3: { "espressione": "Uff..",
"posizione": "f"
},
4: { "espressione": "Yuk yuk!",
"posizione": "f"
},
5: { "espressione": "Sgrunt!",
"posizione": "i"
},
6: { "espressione": "Gasp!",
"posizione" : "i"
}
}
assert onomat("Mi chiamo Pippo.", 4, sentimenti) == "Mi chiamo Pippo. Yuk yuk!"
assert onomat("Quel topastro mi ha rovinato un'altra rapina!", 5, sentimenti) == "Sgrunt! Quel topastro mi ha rovinato un'altra rapina!"
assert onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti) == "Non voglio alzarmi dall'amaca. Uff.."
# FINE TEST