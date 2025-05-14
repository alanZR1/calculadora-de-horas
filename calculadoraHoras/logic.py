import json
from datetime import datetime

CRONOGRAMA_FILE = "cronograma.json"


def validar_fechas(fecha_inicio, fecha_fin):
    return fecha_inicio <= fecha_fin


def cargar_cronograma():
    try:
        with open(CRONOGRAMA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_cronograma(cronograma):
    with open(CRONOGRAMA_FILE, 'w') as f:
        json.dump(cronograma, f, indent=4)


def agregar_actividad(cronograma, nombre, fecha_inicio, fecha_fin, horas):
    fecha_inicio = fecha_inicio.strip()
    fecha_fin = fecha_fin.strip()
    try:
        f_ini = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        f_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        horas = float(horas)

        if not validar_fechas(f_ini, f_fin):
            return "La fecha de fin no puede ser anterior a la de inicio."

        if horas <= 0:
            return "Las horas deben ser mayores a cero."

        cronograma.append({
            "nombre": nombre,
            "inicio": fecha_inicio,
            "fin": fecha_fin,
            "horas": horas
        })
        return "Actividad agregada."

    except Exception as e:
        return f"Error: {e}"


def calcular_horas_en_periodo(cronograma, desde, hasta):
    try:
        f_desde = datetime.strptime(desde.strip(), "%Y-%m-%d")
        f_hasta = datetime.strptime(hasta.strip(), "%Y-%m-%d")
        if f_hasta < f_desde:
            return 0, 0, "La fecha hasta no puede ser anterior a la de desde."

        horas_periodo = 0
        horas_acumuladas = 0

        for act in cronograma:
            f_ini = datetime.strptime(act['inicio'], "%Y-%m-%d")
            f_fin = datetime.strptime(act['fin'], "%Y-%m-%d")
            horas = float(act['horas'])

            if f_ini <= f_hasta:
                horas_acumuladas += horas
            if f_ini <= f_hasta and f_fin >= f_desde:
                horas_periodo += horas

        return horas_periodo, horas_acumuladas, ""
    except Exception as e:
        return 0, 0, f"Error: {e}"
    
    
def eliminar_actividad(cronograma, nombre):
    try: 
        del cronograma[nombre]
        return "Actividad eliminada."
    except KeyError:
        return "Actividad no encontrada."
    
def modificar_actividad(cronograma,index, nombre, fecha_inicio, fecha_fin, horas):
    try:
        f_ini = datetime.strptime(fecha_inicio.strip(), "%Y-%m-%d")
        f_fin = datetime.strptime(fecha_fin.strip(), "%Y-%m-%d")
        horas = float(horas)

        if not validar_fechas(f_ini, f_fin):
            return "La fecha de fin no puede ser anterior a la de inicio."

        if horas <= 0:
            return "Las horas deben ser mayores a cero."

        cronograma[index] = {
            "nombre": nombre,
            "inicio": fecha_inicio,
            "fin": fecha_fin,
            "horas": horas
        }
        return "Actividad modificada."
    except Exception as e:
        return f"Error: al modificar {e}"