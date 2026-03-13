import json


def guardar_gastos(lista):
    with open("archivo_gastos.json", "w") as archivo:
        json.dump(lista, archivo)


def cargar_gastos():
    try:
        with open("archivo_gastos.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []


def agregar_gasto(lista, monto, categoria):
    gasto = {
        "monto": monto,
        "categoria": categoria
    }

    lista.append(gasto)
    guardar_gastos(lista)


def mostrar_gastos(lista):
    print("\nLista de gastos:")
    for g in lista:
        print("Monto:", g["monto"], "| Categoria:", g["categoria"])


def total_gastos(lista):
    total = 0
    for g in lista:
        total += g["monto"]

    print("Total gastado:", total)
    
def total_por_categoria(lista):
    categorias = {}

    for g in lista:
        categoria = g["categoria"]
        monto = g["monto"]

        if categoria in categorias:
            categorias[categoria] += monto
        else:
            categorias[categoria] = monto

    print("\nTotal por categoria:")
    for c in categorias:
        print(c + ":", categorias[c])