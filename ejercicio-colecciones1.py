# Programa: Agenda de contactos
# Autor: Jhon Morales
# Descripción: Permite almacenar contactos usando un diccionario.

# Diccionario donde se guardarán los contactos
contactos = {}

while True:
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número telefónico: ")
        contactos[nombre] = telefono
        print("Contacto agregado correctamente.")

    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos registrados.")
        else:
            print("\n--- Lista de contactos ---")
            for nombre, telefono in contactos.items():
                print(f"{nombre}: {telefono}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre que desea buscar: ")
        if nombre in contactos:
            print(f"Teléfono de {nombre}: {contactos[nombre]}")
        else:
            print("El contacto no fue encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre que desea eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado correctamente.")
        else:
            print("El contacto no existe.")

    elif opcion == "5":
        print("Gracias por usar la agenda de contactos.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")