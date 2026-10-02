from collections import deque

class Medicion:
    def __init__(self, id, espacio, temperatura, humedad, co2):
        self.id = id
        self.espacio = espacio
        self.temperatura = temperatura
        self.humedad = humedad
        self.co2 = co2

    def mostrar(self):
        print(f"ID: {self.id}")
        print(f"Espacio {self.espacio}")
        print(f"Temperatura {self.temperatura}°C")        
        print(f"Humedad {self.humedad} %")                
        print(f"CO2 {self.co2} ppm")

    def condicion_alertas(self):
        condicion = []
        if self.temperatura > 30:
            condicion.append("Temperatura mayor a 30")

        elif self.humedad < 30 or self.humedad > 70:
            condicion.append("Humedad fuera de Rango")

        elif self.co2 > 1000:
            condicion.append("CO2 es mayor a 1000")

        return condicion

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
        print(f"Valor registro: {self.valor}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Estado: {self.estado}")

    def atender(self):
        self.estado = "Atendida"


        
mediciones = []

cola_alerta = deque()

pila_deshacer = []


def registar_medicion():
    espacios = input("Ingresa el espacio: ")
    tem = float(input("Ingresa la temperatura: "))
    hum = float(input("Ingresa la humedad: "))
    c02 = float(input("Ingresa el dioxido de carbono: "))

    j = Medicion(len(mediciones) + 1, espacios, tem, c02) 
    mediciones.append(j)

    alertas = j.condicion_alertas()
    for desc in alertas:
        m = Medicion(len(cola_alerta) + 1, espacios, desc, "-", desc)
        cola_alerta.append(m)
 
def consultar_mediciones():
    if not mediciones:
        print("No hay mediciones registradas")
        return

    print(f"{len(mediciones)} mediciones registradas")
    for j in mediciones:
        j.mostar()
        print()

def atender_alertas():
    if not cola_alerta:
        print("No hay alertas pendietes")
        return

    alerta = cola_alerta.popleft()
    alerta.mostrar()
    alerta.atender()
    pila_deshacer.append(alerta)
    print(f"Alerta {alerta.id} Atendida")

def deshacer_ultimo_registro():
    if pila_deshacer:
        return pila_deshacer.pop()
    print("No hay nada que deshacer")

def mostrar_estadisticas():
    print("\n--- Estadísticas Ambientales ---")
    if not mediciones:
        print("No hay mediciones registradas para calcular estadísticas.")
        return

    total_mediciones = len(mediciones)
    suma_temps = sum(m.temperatura for m in mediciones)
    temp_promedio = suma_temps / total_mediciones
    temp_max = max(m.temperatura for m in mediciones)
    temp_min = min(m.temperatura for m in mediciones)
    alertas_pendientes = len(cola_alerta)

    print(f"Total de mediciones: {total_mediciones}")
    print(f"Temperatura promedio: {temp_promedio:.2f} °C")
    print(f"Temperatura máxima: {temp_max} °C")
    print(f"Temperatura mínima: {temp_min} °C")
    print(f"Alertas pendientes en cola: {alertas_pendientes}")

# Menu Principal 
def main():
    while True:
        print("---Menu Principal Sistema EcoLabs---")
        print("1.Registrar Medicion")
        print("2.Consultar Medicion")
        print("3.Consultar Alertas")
        print("4.Atender Alertas")
        print("5.Deshacer Ultimo Registro")
        print("6.Mostrar Estadisticas")
        print("7.Salir")


        opcion = input("Elige Una Opcion").strip

        if opcion == "1":
            registar_medicion()

        elif opcion == "2":
            consultar_mediciones()

        elif opcion == "3":
            atender_alertas()

        elif opcion == "4":
            atender_alertas()

        elif opcion == "5":
            deshacer_ultimo_registro()

        elif opcion == "6":
            mostrar_estadisticas
            
        elif opcion == "7":
            print("Hasta pornto! Gracias por usar EcoLabs")
            break
        else:
            print("Opcion invalida. Intenta de nuevo")

