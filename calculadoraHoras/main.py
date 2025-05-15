import flet as ft
from logic import (cargar_cronograma,
    guardar_cronograma, calcular_horas_en_periodo,
    agregar_actividad, eliminar_actividad, modificar_actividad)
from ui_components import crear_interfaz

def main(page: ft.Page):
    page.window_width = 500
    page.window_height = 400
    page.window_min_width = 300
    page.window_min_height = 400
    
    page.title = "Calculadora de Horas de Servicio Social"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK  # o DARK/SYSTEM
    

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
    page.add(interfaz)

if __name__ == "__main__":
    ft.app(target=main)  # Ejecuta como app de escritorio
