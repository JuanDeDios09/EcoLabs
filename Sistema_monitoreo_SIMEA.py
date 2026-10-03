from collections import deque 

#Medicon
class Medicion:
    def __init__(self, id, espacio, temperatura, humedad,co2):

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

# Alertas 
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
        print(f"Descripcion: {self.descripcion}")
        print(f"Estado: {self.estado}")

    def atender(self):
        self.estado = "Atendida"

Espacios = ["Aula", "Laboratorio", "Biblioteca"]
mediciones = [] # Lista
alertas = deque()    # Cola 
pila = deque()       # Pila

contador_id = 0 # Contador id 
contador_alertas = 0  # Contador de alertas


# 1. Registrar mediciones  
def registrar_medicion():
    print("\n---Registrar Medicion---")
    global contador_id 
    
    esp = input("Espacios (Aula, Laboratorio, Biblioteca): ").strip().capitalize()

    if esp not in Espacios:
        print("Espacio invalido")
        return
    
    temp = float(input("Temperatura: "))
    hum = float(input("Humedad: "))
    c02 = float(input("CO2: "))


    if temp > 30:
        print("Temperatura fuera de rango")

    if hum < 30: 
        print("Humedad baja")

    elif hum > 70:
        print("Humedad alta")

    if c02 > 1000:
        print("CO2 elevado")

    contador_id += 1
    j = Medicion(contador_id, esp, temp, hum, c02)
    mediciones.append(j)
    pila.append(j)

    generar_alertas(j)

    print("-" * 36)
    print(f"Medicion {j.id}, Registrada correctamente")

    
# 2. Consultar mediciones registradas
def consultar_medicion():
    print("\n---Consultar Mediciones---")
    if not mediciones:
        print("No hay mediciones registradas")
        return

    for j in mediciones:
        j.mostrar()


# 3. Generar alertas por condiciones ambientales 
def generar_alertas(j):
    global contador_alertas
    alerta_generada = False

    if j.temperatura > 30:
        if not alerta_generada: 
            print("\n----- Alertas -----") 
            alerta_generada = True 
        print("Temperatura fuera de rango")
        contador_alertas += 1

        alertas.append(Alerta(contador_alertas, j.espacio, "Temperatura", j.temperatura, "Temperatura fuera de rango"))

    if j.humedad < 30:
        if not alerta_generada: 
            print("\n----- Alertas -----") 
            alerta_generada = True 
        print("Humedad baja")
        contador_alertas += 1

        alertas.append(Alerta(contador_alertas, j.espacio, "Humedad", j.humedad, "Humedad baja"))

    elif j.humedad > 70:
        if not alerta_generada: 
            print("\n----- Alertas -----") 
            alerta_generada = True 
        print("Humedad alta")
        contador_alertas += 1

        alertas.append(Alerta(contador_alertas, j.espacio, "Humedad", j.humedad, "Humedad alta"))

    if j.co2 > 1000:
        if not alerta_generada: 
            print("\n----- Alertas -----") 
            alerta_generada = True 
        print("CO2 elevado")
        contador_alertas += 1
        
        alertas.append(Alerta(contador_alertas, j.espacio, "CO2", j.co2, "CO2 elevado"))


# Consultar alertas registradas
def consultar_alertas():
    print("\n--- Consultar Alertas ---")

    if not alertas:
        print("No hay alertas registradas")
        return

    for a in alertas:
        a.mostrar()
       


# 4. Atender alertas pendientes 
def alertas_pendientes():
    print("Atender Alertas")
    if not alertas:
        print("No hay alertas pendientes")
        return

    a = alertas.popleft() # Saca las mas antiguas 
    a.atender()
    a.mostrar()

    print("Alerta atendida correctamente")

# 5. Deshacer el ultimo registro
def deshacer_ultimo():
    print("Deshacer ultimo registro")
    if not pila:
        print("No hay mediciones para deshacer")
        return

    j = pila.pop()
    mediciones.remove(j)

    print(f"Medicion {j.id} deshecha")

# 6. Calcular estadisticas ambientales
def estadisticas():
    print("Estadisticas Ambientasles")
    if not mediciones:
        print("No hay mediciones para calcular")
        return

    n = 0 
    suma_temp = 0 
    suma_hum = 0
    suma_c02 = 0
    temp_max = mediciones[0].temperatura
    temp_min = mediciones[0].temperatura

    # Ciclo para calcular con operaciones aritmeticas 
    for j in mediciones:
        n = n + 1
        suma_temp = suma_temp + j.temperatura
        suma_hum = suma_hum + j.humedad
        suma_c02 = suma_c02 + j.co2

        if j.temperatura > temp_max:
            temp_max = j.temperatura 

        if j.temperatura < temp_min:
            temp_min = j.temperatura 

    # Evitar division entre cero
    prom_temp = suma_temp / n 
    prom_hum = suma_hum / n
    prom_c02 = suma_c02 / n

    print(f"Total de medicones:     {n}")
    print(f"    Temperatura promedio:   {prom_temp:.1f} °C")
    print(f"    Temperatura máxima:     {temp_max:.1f} °C")
    print(f"    Temperatura mínima:     {temp_min:.1f} °C")
    print(f"    Humedad promedio:       {prom_hum:.1f} %")
    print(f"    CO2 promedio:           {prom_c02:.1f} ppm")
    print(f"    Alertas pendientes:     {len(alertas)}")

# Menu Principal 
def menu():
    while True:
        print("\n" + "=" * 50)
        print("SIMEA".center(50))
        print("=" * 50)
        print("1. Registrar Medicion")
        print("2. Consultar mediciones")
        print("3. Consultar alertas")
        print("4. Atender Alertas")
        print("5. Deshacer ultimo registro")
        print("6. Mostrar estadisticas")
        print("7. Salir") 
        print("=" * 50)

        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            registrar_medicion()

        elif opcion == 2:
            consultar_medicion()

        elif opcion == 3:
            consultar_alertas()

        elif opcion == 4:
            alertas_pendientes()

        elif opcion == 5:
            deshacer_ultimo()

        elif opcion == 6:
            estadisticas()

        elif opcion == 7:
            print("¡Hasta pronto!, Gracias por usar SIMEA")
            break

        else:
            print("Opcion invalida. Intenta de nuevo")


menu()