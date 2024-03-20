listado = [7,7,6,6,5,5]

def quitar_repetidos() :
    nuevalista = set(listado)
    return list(nuevalista)


print(quitar_repetidos())

def ordenar_contar_valores():
    contar_numeros = {}
    for i in listado:
        contar_numeros[i] = contar_numeros.get(i,0)+1

    numeros_ordenados = sorted(contar_numeros.items())

    return numeros_ordenados


print(ordenar_contar_valores())