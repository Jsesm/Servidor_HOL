import random

def traducir_palo(numeroReal, numeroNo):
    mi_set = set()     
    numeros= generar_numeros_aleatorios()
    mi_set.add(traducir_valor(str(numeroReal)))
    mi_set.add(traducir_valor(str(numeroNo)))
    for num in numeros:
        mi_set.add(traducir_valor(str(num)))
    mi_lista= list(mi_set)
    random.shuffle(mi_lista)
    return mi_lista


def generar_numeros_aleatorios():
    numeros = [random.randint(1, 13) for _ in range(3)]
    return numeros

def traducir_valor(valor):
    valor = str(valor).upper()
    
    if valor=="1" or valor == "ACE":
        return "A"
    elif valor == "11" or valor == "JACK":
        return "J"
    elif valor == "12" or valor == "QUEEN":
        return "Q"
    elif valor == "13" or valor == "KING":
        return "K"
    else:
        return str(valor)  # Devuelve lo que le han pasado
    


def elegir_carta():
    numeros_validos = [n for n in range(1, 13) if n not in (8, 9)]
    
    palabras = ["Atleti", "Simpsons", "ESI", "Toledo"]
    
    numero = random.choice(numeros_validos)
    palo = random.choice(palabras)
    
    return numero, palo

