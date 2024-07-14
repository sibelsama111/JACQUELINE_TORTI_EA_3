import datetime

now = datetime.datetime.now()

def comprar_entradas_mj(escenario):
    precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
               6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
               11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
               16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
               21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
               26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
               31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
               36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
               41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
               46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}
    
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 o 2): "))
    if cantidad < 1 or cantidad > 2:
        print("Cantidad inválida.")
        return
    
    for _ in range(cantidad):
        disponibilidad(escenario)
        asiento = int(input("Seleccione el número del asiento que desea comprar: "))
        if escenario[asiento - 1] == 'X':
            print("El asiento no está disponible.")
            return
        escenario[asiento - 1] = 'X'
        precio = precios[asiento]
        rut = input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {rut}.\n")
    
def disponibilidad(escenario):
    print("\t\t\t ESCENARIO\n")
    for i in range(0, 50, 10):
        fila = ""
        for j in range(10):
            fila += f"{escenario[i + j]}\t"
        print(fila)
    print("\n")

asistentes = []

def listado_asistentes(rut):
    asistentes.append(rut)
    print(asistentes)

def total_vendido(precios, escenario):
    total = 0
    for i, estado in enumerate(escenario):
        if estado == 'X':
            total += precios[i + 1]  # Se suma el precio del asiento vendido
    print(f"Total vendido hasta ahora: ${total}")

# Crear lista de asientos disponibles
escenario = ['O'] * 50  # 'O' indica que el asiento está disponible

opcion = 0

while opcion != "5":
    print("Sanchez Producciones presenta: Concierto Michael Jackson 2024.")
    print("A continuación, digite la opción que desee:")
    print("1. Comprar entradas.")
    print("2. Mostrar ubicaciones disponibles.")
    print("3. Mostrar listado de asistentes.")
    print("4. Mostrar total vendido.")
    print("5. Salir.")
    opcion = input(": ")

    if opcion == "1":
        comprar_entradas_mj(escenario)
    elif opcion == "2":
        disponibilidad(escenario)
    elif opcion == "3":
        listado_asistentes(input("Ingrese el RUN para buscar al asistente: "))
    elif opcion == "4":
        total_vendido(precios, escenario)
    elif opcion == "5":
        print("Gracias por usar el sistema de ventas!")
    else:
        print("Opción inválida.")
