from collections import deque

# ==================== CLASES ====================

class Medicion:
    def __init__(self, id, espacio, temperatura, humedad, co2):
        self.id = id
        self.espacio = espacio
        self.temperatura = temperatura
        self.humedad = humedad
        self.co2 = co2

    def mostrar(self):
        print(f"ID: {self.id}")
        print(f"Espacio: {self.espacio}")
        print(f"Temperatura: {self.temperatura} °C")
        print(f"Humedad: {self.humedad} %")
        print(f"CO2: {self.co2} ppm")


class Alerta:
    def __init__(self, id, espacio, variable, valor, descripcion):
        self.id = id
        self.espacio = espacio
        self.variable = variable
        self.valor = valor
        self.descripcion = descripcion
        self.estado = "Pendiente"

    def mostrar(self):
        print(f"ID de alerta: {self.id}")
        print(f"Espacio: {self.espacio}")
        print(f"Variable: {self.variable}")
        print(f"Valor registrado: {self.valor}")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {self.estado}")

    def atender(self):
        self.estado = "Atendida"


# ==================== ESTRUCTURAS ====================

ESPACIOS = ["Aula", "Laboratorio", "Biblioteca"]
mediciones = []    # Lista: almacena las mediciones
alertas = deque()  # Cola (FIFO): alertas pendientes
pila = deque()     # Pila (LIFO): para deshacer registros

contador_id = 0
contador_alertas = 0


# ==================== UTILIDADES ====================

def titulo(texto):
    print("\n" + "=" * 50)
    print(texto.center(50))
    print("=" * 50)


def leer_float(mensaje, minimo, maximo):
    """Pide un número y lo repite hasta que sea válido y esté en rango."""
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Dato inválido: escribe un número")
            continue
        if valor < minimo or valor > maximo:
            print(f"El valor debe estar entre {minimo} y {maximo}")
            continue
        return valor


# ==================== 1. REGISTRAR MEDICIÓN ====================

def registrar_medicion():
    global contador_id
    titulo("REGISTRAR MEDICIÓN")

    esp = input("Espacio (Aula, Laboratorio, Biblioteca): ").strip().capitalize()
    if esp not in ESPACIOS:
        print("Espacio inválido")
        return

    temp = leer_float("Temperatura (°C): ", -10, 60)
    hum = leer_float("Humedad relativa (%): ", 0, 100)
    co2 = leer_float("CO2 (ppm): ", 0, 10000)

    contador_id += 1
    m = Medicion(contador_id, esp, temp, hum, co2)
    mediciones.append(m)   # Lista
    pila.append(m)         # Pila (para poder deshacer)

    generar_alertas(m)

    print("-" * 50)
    print(f"Medición {m.id} registrada correctamente")


# ==================== 2. CONSULTAR MEDICIONES ====================

def consultar_medicion():
    titulo("CONSULTAR MEDICIONES")
    if not mediciones:
        print("No hay mediciones registradas")
        return

    for m in mediciones:
        m.mostrar()
        print("-" * 50)


# ==================== 3. GENERAR ALERTAS ====================

def generar_alertas(m):
    global contador_alertas
    nuevas = []

    if m.temperatura > 30:
        nuevas.append(("Temperatura", m.temperatura, "Temperatura elevada"))

    if m.humedad < 30:
        nuevas.append(("Humedad", m.humedad, "Humedad baja"))
    elif m.humedad > 70:
        nuevas.append(("Humedad", m.humedad, "Humedad alta"))

    if m.co2 > 1000:
        nuevas.append(("CO2", m.co2, "CO2 elevado"))

    if not nuevas:
        return

    print("\n----- ALERTAS GENERADAS -----")
    for variable, valor, descripcion in nuevas:
        contador_alertas += 1
        alertas.append(Alerta(contador_alertas, m.espacio, variable, valor, descripcion))
        print(f"[{variable}] {descripcion}")


# ==================== CONSULTAR ALERTAS PENDIENTES ====================

def consultar_alertas():
    titulo("ALERTAS PENDIENTES")
    if not alertas:
        print("No hay alertas pendientes")
        return

    for a in alertas:
        a.mostrar()
        print("-" * 50)


# ==================== 4. ATENDER ALERTA ====================

def atender_alerta():
    titulo("ATENDER ALERTA")
    if not alertas:
        print("No hay alertas pendientes")
        return

    a = alertas[0]  # Primera alerta (sin sacarla todavía)
    a.mostrar()
    print("-" * 50)

    confirmar = input("¿Atender esta alerta? (s/n): ").strip().lower()
    if confirmar == "s":
        alertas.popleft()  # FIFO: sale la más antigua
        a.atender()
        print("Alerta atendida correctamente")
    else:
        print("Alerta no atendida, sigue pendiente")


# ==================== 5. DESHACER ÚLTIMO REGISTRO ====================

def deshacer_ultimo():
    titulo("DESHACER ÚLTIMO REGISTRO")
    if not pila:
        print("No hay mediciones para deshacer")
        return

    m = pila.pop()          # LIFO: sale la más reciente
    mediciones.remove(m)
    print(f"Medición {m.id} ({m.espacio}) deshecha correctamente")


# ==================== 6. ESTADÍSTICAS ====================

def estadisticas():
    titulo("ESTADÍSTICAS AMBIENTALES")
    if not mediciones:
        print("No hay mediciones para calcular")
        return

    n = 0
    suma_temp = 0
    suma_hum = 0
    suma_co2 = 0
    temp_max = mediciones[0].temperatura
    temp_min = mediciones[0].temperatura

    for m in mediciones:
        n = n + 1
        suma_temp = suma_temp + m.temperatura
        suma_hum = suma_hum + m.humedad
        suma_co2 = suma_co2 + m.co2

        if m.temperatura > temp_max:
            temp_max = m.temperatura
        if m.temperatura < temp_min:
            temp_min = m.temperatura

    # n > 0 garantizado por la validación anterior (no hay división entre cero)
    prom_temp = suma_temp / n
    prom_hum = suma_hum / n
    prom_co2 = suma_co2 / n

    print(f"Total de mediciones:    {n}")
    print(f"Temperatura promedio:   {prom_temp:.1f} °C")
    print(f"Temperatura máxima:     {temp_max:.1f} °C")
    print(f"Temperatura mínima:     {temp_min:.1f} °C")
    print(f"Humedad promedio:       {prom_hum:.1f} %")
    print(f"CO2 promedio:           {prom_co2:.1f} ppm")
    print(f"Alertas pendientes:     {len(alertas)}")


# ==================== MENÚ PRINCIPAL ====================

def menu():
    while True:
        titulo("EcoLabs")
        print("1. Registrar medición")
        print("2. Consultar mediciones")
        print("3. Consultar alertas pendientes")
        print("4. Atender alerta")
        print("5. Deshacer último registro")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        print("=" * 50)

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción inválida. Escribe un número del 1 al 7")
            continue

        if opcion == 1:
            registrar_medicion()
        elif opcion == 2:
            consultar_medicion()
        elif opcion == 3:
            consultar_alertas()
        elif opcion == 4:
            atender_alerta()
        elif opcion == 5:
            deshacer_ultimo()
        elif opcion == 6:
            estadisticas()
        elif opcion == 7:
            print("¡Hasta pronto! Gracias por usar SIMEA")
            break
        else:
            print("Opción inválida. Intenta de nuevo")


if __name__ == "__main__":
    menu()