import flet as ft
from calculadoraHoras.logic import (cargar_cronograma,
    guardar_cronograma, calcular_horas_en_periodo,
    agregar_actividad, eliminar_actividad, modificar_actividad)
from calculadoraHoras.ui_components import crear_interfaz

def main(page: ft.Page):
    page.title = "Calculadora de Horas de Servicio Social"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO

    # Cargar cronograma al iniciar
    cronograma = cargar_cronograma()

    interfaz = crear_interfaz(
        page,
        cronograma,
        agregar_actividad,
        guardar_cronograma,
        calcular_horas_en_periodo,
        eliminar_actividad,
        modificar_actividad
    )
    page.add(*interfaz)

if __name__ == "__main__":
    ft.app(target=main)  # Ejecuta como app de escritorio
