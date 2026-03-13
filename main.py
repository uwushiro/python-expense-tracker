from gastos import agregar_gasto, mostrar_gastos, total_gastos, cargar_gastos, total_por_categoria

gastos = cargar_gastos()

while True:
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Ver total")
    print("4. Ver total por categoria")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto: "))
        categoria = input("Ingrese la categoria:")
        agregar_gasto(gastos, monto, categoria)

    elif opcion == "2":
        mostrar_gastos(gastos)

    elif opcion == "3":
        total_gastos(gastos)

    elif opcion == "4":
        total_por_categoria(gastos)

    elif opcion == "5":
        print("Adios!")
        break

    else:
        print("Opcion invalida.")