import flet as ft

def crear_interfaz(page, cronograma, agregar_actividad_fn, guardar_fn, calcular_fn, eliminar_fn=None, modificar_fn=None):
    nombre = ft.TextField(label="Nombre de actividad")
    inicio = ft.TextField(label="Fecha inicio (YYYY-MM-DD)")
    fin = ft.TextField(label="Fecha fin (YYYY-MM-DD)")
    horas = ft.TextField(label="Horas totales")
    mensaje = ft.Text(value="")

    desde = ft.TextField(label="Desde (YYYY-MM-DD)")
    hasta = ft.TextField(label="Hasta (YYYY-MM-DD)")
    resultado = ft.Text(value="")
    
    tabla_cronograma = ft.Column()
    
    def actualizar_tabla():
        tabla_cronograma.controls = []
        for idx, act in enumerate(cronograma):
            fila = ft.Row([
                ft.Text(f"{act['nombre']}"),
                ft.Text(f"{act['inicio']}"),
                ft.Text(f"{act['fin']}"),
                ft.Text(f"{act['horas']}"),
                ft.ElevatedButton("Editar", on_click=lambda e, idx=idx: editar_actividad(idx)),
                ft.ElevatedButton("Eliminar", on_click=lambda e, idx=idx: eliminar_actividad(idx))
                ])
        tabla_cronograma.controls.append(fila)
        
    def on_agregar(e):
        msj = agregar_actividad_fn(cronograma, nombre.value, inicio.value, fin.value, horas.value)
        guardar_fn(cronograma)
        mensaje.value = msj
        nombre.value = inicio.value = fin.value = horas.value = ""
        page.update()

    def on_consultar(e):
        periodo, acumulado, msj = calcular_fn(cronograma, desde.value, hasta.value)
        if msj:
            resultado.value = msj
        else:
            resultado.value = f"Horas en periodo: {periodo}\nHoras acumuladas: {acumulado}"
        page.update()
        
    def eliminar_actividad(index):
        msj = eliminar_fn(index)
        guardar_fn(cronograma)
        mensaje.value = eliminar_fn(cronograma, index)
        actualizar_tabla()
        page.update()
        
    def editar_actividad(index):
        act = cronograma[index]
        nombre.value = act['nombre']
        inicio.value = act['inicio']
        fin.value = act['fin']
        horas.value = act['horas']
        
        def confirmar_edicion(e):
            guardar_fn(cronograma)
            mensaje.value = modificar_fn(cronograma, index, nombre.value, inicio.value, fin.value, horas.value)
            actualizar_tabla()
            nombre.value = inicio.value = fin.value = horas.value = ""
            page.update()
            btn_guardar_edicion.visible = False
           

        btn_guardar_edicion.visible = True
        btn_guardar_edicion.on_click = True
    
    btn_guardar_edicion = ft.ElevatedButton("Guardar Edición", visible = False)
    
    actualizar_tabla()
        
    return [
        ft.Text("Agregar Actividad", size=20, weight="bold"),
        nombre, inicio, fin, horas,
        ft.ElevatedButton("Agregar", on_click=on_agregar),
        mensaje,
        ft.Divider(),
        ft.Text("Consultar Horas", size=20, weight="bold"),
        desde, hasta,
        ft.ElevatedButton("Consultar", on_click=on_consultar),
        resultado
    ]
