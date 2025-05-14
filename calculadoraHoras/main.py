import flet as ft
from . import logic
from . import ui_components

def main(page: ft.Page):
    page.title = "Calculadora de Horas de Servicio Social"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO

    # Creamos la interfaz (inputs, botones, texto, etc.)
    interfaz = ui_components.crear_interfaz(page, logic.calcular_total)

    # Agregamos los componentes a la página
    page.add(*interfaz)

# Lanzamos la app (modo navegador)
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
