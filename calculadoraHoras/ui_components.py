import flet as ft

def crear_interfaz(page, cronograma, agregar_actividad_fn, guardar_fn, calcular_fn, eliminar_fn=None, modificar_fn=None):
    # controles 
    nombre = ft.TextField(label="Nombre de actividad")
    inicio = ft.TextField(label="Fecha inicio (YYYY-MM-DD)")
    fin = ft.TextField(label="Fecha fin (YYYY-MM-DD)")
    horas = ft.TextField(label="Horas totales")
    mensaje = ft.Text(value="")
    # controles para consultar las fechas
    desde = ft.TextField(label="Desde (YYYY-MM-DD)")
    hasta = ft.TextField(label="Hasta (YYYY-MM-DD)")
    resultado = ft.Text(value="")
    
    # tabla para mostrar actividades
    tabla_cronograma = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Actividad")),
            ft.DataColumn(ft.Text("Fecha Inicio")), 
            ft.DataColumn(ft.Text("Fecha Fin")),
            ft.DataColumn(ft.Text("Horas")),
            ft.DataColumn(ft.Text("Modificar")),
            ft.DataColumn(ft.Text("Eliminar"))
        ],
        rows=[],
        expand = True
    )
    
    def actualizar_tabla():
        rows = []
        for idx, act in enumerate(cronograma):
            rows.append(
                ft. DataRow(
                    cells=[
                        ft.DataCell(ft.Text(act['nombre'])),
                        ft.DataCell(ft.Text(act['inicio'])),
                        ft.DataCell(ft.Text(act['fin'])),
                        ft.DataCell(ft.Text(str(act['horas']))),
                        ft.DataCell(ft.Row([
                            ft.ElevatedButton("editar", on_click=lambda e, idx=idx: modificar_actividad(idx)),
                            ft.ElevatedButton("eliminar", on_click=lambda e, idx=idx: eliminar_actividad(idx)
                                              , color=ft.colors.RED_400)
                            
                        ], spacing=5))
                    ]
                    
                )
            )
        tabla_cronograma.rows = rows
        page.update()
        
    def on_agregar(e):
        msj = agregar_actividad_fn(
            cronograma,
            nombre.value,
            inicio.value,
            fin.value,
            horas.value
            )
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
        mensaje.value = eliminar_fn(cronograma, index)
        guardar_fn(cronograma)
        actualizar_tabla()
        page.update()
        
    def modificar_actividad(index):
        act = cronograma[index]
        nombre.value = act['nombre']
        inicio.value = act['inicio']
        fin.value = act['fin']
        horas.value = act['horas']
        
        def confirmar_edicion(e):
            mensaje.value = modificar_fn(
                cronograma,
                index,
                nombre.value,
                inicio.value,
                fin.value,
                horas.value
                )
            guardar_fn(cronograma)
            nombre.value = inicio.value = fin.value = horas.value = ""
            actualizar_tabla()
           

        btn_guardar_edicion.visible = True
        btn_guardar_edicion.on_click = confirmar_edicion
        page.update()
    
    btn_guardar_edicion = ft.ElevatedButton("Guardar Edición", visible = False)
    
    actualizar_tabla()
        
    return ft.Column(
        controls=[
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Agregar Actividad", size=20, weight="bold"),
                        ft.Row([nombre, inicio, fin, horas], spacing=10),
                        ft.ElevatedButton("Agregar", on_click=on_agregar, icon=ft.Icons.ADD),
                        mensaje
                    ]),
                    padding=15
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Consultar Horas", size=20, weight="bold"),
                        ft.Row([desde, hasta], spacing=10),
                        ft.ElevatedButton("Consultar", on_click=on_consultar, icon=ft.Icons.CALCULATE),
                        resultado
                    ]),
                    padding=15
                )
            ),
            ft.Text("Cronograma", size=20, weight="bold"),
            ft.Container(
                content=tabla_cronograma,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=5,
                padding=10,
                expand=True
            ),
            btn_guardar_edicion
        ],
        spacing=20,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )
