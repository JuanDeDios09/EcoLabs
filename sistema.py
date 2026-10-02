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

medicion = []

cola_alerta = deque()

pila_deshacer = []

def registrar_id():

def registar_medicion():
    espacios = ["Aula, Laboratorio, Biblioteca"]
    print("Espacio")

    def consultar_mediciones():
    def atender_alertas():
    def deshacer_ultimo_registro():
    def mostrar_estadisticas():





# Menu Principal 
opcion = input("Elige una opcion").strip

while True:
    print("---Menu Principal---")
    print("1.Registrar Medicion")
    print("2.Consultar Medicion")
    print("3.Consultar Alertas")
    print("4.Atender Alertas")
    print("5.Deshacer Ultimo Registro")
    print("6.Mostrar Estadisticas")
    print("7.Salir")


    opcion = input("Elige Una Opcion")

    if opcion == "1":
        
    elif opcion == "2":

    elif opcion == "3":

    elif opcion == "4":

    elif opcion == "5":

    elif opcion == "6":
        
    elif opcion == "7":
        print("Hasta Pronto")
        break
    else:
        print("Opcion invalida, Intenta de nuevo")

