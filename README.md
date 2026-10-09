# TecOlogic
## Sistema inteligente de monitoreo y atención ambiental

Prototipo en Python (interfaz de consola) que registra mediciones ambientales simuladas de Aula, Laboratorio y Biblioteca, genera alertas cuando se superan los umbrales, permite atenderlas en orden y deshacer el último registro.

Proyecto de la materia **Estructura de Datos**, Ingeniería Informática.

## Características

- Registro de temperatura, humedad relativa y CO₂ con validación de datos.
- Consulta de todas las mediciones registradas.
- Generación automática de alertas según umbrales.
- Atención de alertas en orden de llegada (FIFO) con confirmación.
- Deshacer el último registro (LIFO).
- Estadísticas: total, temperatura promedio, máxima y mínima, humedad y CO₂ promedio, y alertas pendientes.

## Estructuras de datos utilizadas

| Funcionalidad | Estructura | Implementación |
|---|---|---|
| Mediciones registradas | Lista | `list` |
| Alertas pendientes | Cola (FIFO) | `collections.deque` |
| Deshacer registros | Pila (LIFO) | `collections.deque` |

## Umbrales de alerta

| Variable | Se genera alerta si es… |
|---|---|
| Temperatura | Mayor que 30 °C |
| Humedad relativa | Menor que 30 % o mayor que 70 % |
| CO₂ | Mayor que 1000 ppm |

> Los umbrales son didácticos y no representan normas oficiales de calidad ambiental.

## Requisitos

- Python 3.6 o superior (se recomienda 3.8 o más reciente).
- No necesita instalar librerías externas: solo usa la biblioteca estándar de Python.

## Instalación y ejecución en Windows

### 1. Instalar Python

Descarga Python desde [python.org/downloads](https://www.python.org/downloads/).

Abre el instalador y marca la casilla **“Add python.exe to PATH”** (aparece en la primera pantalla). Haz clic en **Install Now** y espera a que termine.

### 2. Comprobar la instalación

Abre CMD o PowerShell y ejecuta:

```bash
python --version
```

Debe mostrar algo como `Python 3.12.x`. Si Windows abre la Microsoft Store o dice que no reconoce el comando, vuelve a instalar Python y asegúrate de marcar **“Add python.exe to PATH”**. También puedes probar con:

```bash
py --version
```

### 3. Descargar el proyecto

**Opción A, con Git:**

```bash
git clone https://github.com/JuanDeDios09/TecOlogic.git
cd TecOlogic
```

**Opción B, sin Git:** en la página del repositorio haz clic en **Code → Download ZIP**, descomprime la carpeta y abre CMD dentro de ella (en el Explorador de archivos, escribe `cmd` en la barra de direcciones y presiona Enter).

### 4. Ejecutar

```bash
python Sistema_monitoreo_TecOlogic.py
```

Si `python` no funciona, usa:

```bash
py Sistema_monitoreo_TecOlogic.py
```

## Instalación y ejecución en Linux

### 1. Instalar Python

La mayoría de las distribuciones ya lo traen. Compruébalo con:

```bash
python3 --version
```

Si no está instalado, usa el comando de tu distribución:

| Distribución | Comando |
|---|---|
| Ubuntu / Debian / Linux Mint | `sudo apt update && sudo apt install python3 git` |
| Fedora | `sudo dnf install python3 git` |
| Arch / Manjaro | `sudo pacman -S python git` |

### 2. Descargar el proyecto

**Opción A, con Git:**

```bash
git clone https://github.com/JuanDeDios09/TecOlogic.git
cd TecOlogic
```

**Opción B, sin Git:**

```bash
wget https://github.com/JuanDeDios09/TecOlogic/archive/refs/heads/main.zip
unzip main.zip
cd TecOlogic-main
```

Si no tienes `unzip`, puedes instalarlo con:

```bash
sudo apt install unzip
```

### 3. Ejecutar

```bash
python3 Sistema_monitoreo_TecOlogic.py
```

## Cómo se usa

Al ejecutar el programa aparece el menú principal:

```text
==================================================
                     TecOlogic
==================================================
1. Registrar medición
2. Consultar mediciones
3. Consultar alertas pendientes
4. Atender alerta
5. Deshacer último registro
6. Mostrar estadísticas
7. Salir
==================================================
```

| Opción | Qué hace |
|---|---|
| 1 | Pide espacio (Aula, Laboratorio o Biblioteca), temperatura (°C), humedad (%) y CO₂ (ppm). Valida que sean números en rango y genera alertas si aplica. |
| 2 | Muestra todas las mediciones registradas. |
| 3 | Muestra las alertas pendientes, de la más antigua a la más reciente. |
| 4 | Muestra la primera alerta y pide confirmación (s/n). Si confirmas con `s`, se retira de la cola. |
| 5 | Elimina la medición más reciente. |
| 6 | Muestra las estadísticas ambientales. |
| 7 | Cierra el programa. |

## Ejemplo rápido

1. Elige `1` y captura: `Laboratorio, 31.5, 42, 800` → se genera una alerta de temperatura.
2. Elige `3` para ver la alerta, luego `4` y responde `s` para atenderla.
3. Elige `6` para ver las estadísticas.

## Datos de prueba

| Espacio | Temperatura | Humedad | CO₂ | Alertas esperadas |
|---|---:|---:|---:|---|
| Laboratorio | 31.5 °C | 42 % | 800 ppm | 1 (temperatura) |
| Aula | 26 °C | 25 % | 1200 ppm | 2 (humedad baja y CO₂) |
| Biblioteca | 24 °C | 45 % | 700 ppm | 0 |

## Si algo falla

| Problema | Solución |
|---|---|
| `python` no se reconoce (Windows) | Reinstala Python marcando “Add python.exe to PATH”, o usa `py`. |
| `python3: command not found` (Linux) | Instala Python con el comando de tu distribución (ver arriba). |
| `can't open file ... No such file or directory` | Abre la terminal dentro de la carpeta del proyecto (usa `cd TecOlogic`) y revisa que el nombre del archivo esté bien escrito. |
| “Dato inválido” | Escribiste letras o dejaste el campo vacío. Captura un número. |
| “Espacio inválido” | Escribe exactamente Aula, Laboratorio o Biblioteca. |
| “No hay alertas pendientes” | La cola está vacía. Registra una medición que supere un umbral. |

## Estructura del repositorio

```text
TecOlogic/
├── Sistema_monitoreo_TecOlogic.py        # Código fuente
├── TecOlogic_Documentacion_Proyecto.pdf  # Documentación, pruebas y diagrama
├── Manual_de_uso_TecOlogic.pdf          # Manual de uso (1 página)
├── Diagrama_de_flujo.png                # Diagrama de flujo del sistema
└── README.md
```

## Mejoras futuras

- Que al deshacer una medición también se quiten las alertas que generó.
- Guardar mediciones y alertas en un archivo para no perderlas al cerrar el programa.
- Filtrar mediciones y estadísticas por espacio.
- Atender primero las alertas más graves con una cola de prioridad.

## Integrantes

- Miguel Angel Luna
- Victor Emiliano Reyes
- Juan de Dios Antunez

**Ingeniería Informática · Estructura de Datos**