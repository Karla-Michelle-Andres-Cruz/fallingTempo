import flet as ft

def UserView(page, auth_controller):

    page.title = "Perfil"
    page.bgcolor = "#FFF8EC"

    user = auth_controller.current_user

    def cerrar_sesion(e):
        auth_controller.logout()
        page.navigation_bar = None
        page.data = None
        page.go("/")
        page.update()

    def editar_perfil(e):
        page.go("/editar")

    def confirmar_eliminacion(e):
        print("ELIMINANDO USUARIO:", user["id_usuarios"])
        auth_controller.eliminar_usuario(user["id_usuarios"])
        auth_controller.logout()
        page.navigation_bar = None
        if page.data:
            page.data.clear()
        page.go("/")

    def eliminar_cuenta(e):
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text(
                "¿Estás seguro de que quieres eliminar tu cuenta?"
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: cerrar(dlg)
                ),
                ft.ElevatedButton(
                    "Eliminar",
                    on_click=confirmar_eliminacion
                )
            ]
        )

        

        page.dialog = dlg
        dlg.open = True
        page.update()


    def cerrar(dlg):
        dlg.open = False
        page.update()

    if not user:
        return ft.Container(
            content=ft.Text(
                "No hay sesión iniciada",
                color="black"
            )
        )

    

    def cambiar_pagina(e):
        if e.control.selected_index == 0:
            page.go("/home")

        elif e.control.selected_index == 1:
            page.go("/usuarios")

    page.navigation_bar = ft.NavigationBar(
        selected_index=1,
        on_change=cambiar_pagina,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Inicio"
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="Usuarios"
            ),
        ]
    )

    profile_card = ft.Card(
        elevation=15,

        content=ft.Container(
            width=350,
            padding=25,
            border_radius=20,
            bgcolor="#DCCCAC",

            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,

                controls=[

                    ft.CircleAvatar(
                        radius=45,
                        bgcolor="#5A5D8F",

                        content=ft.Text(
                            user["nombre"][0].upper(),
                            size=35,
                            color="black",
                            weight=ft.FontWeight.BOLD
                        )
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(ft.Icons.BADGE, color="black"),
                                ft.Text(
                                f"ID: {user['id_usuarios']}",
                                color="black"
                                )
                        ]
                    ),

                    ft.Text(
                        f"{user['nombre']} {user['apellido']}",
                        size=24,
                        color="black",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Divider(color="black"),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(ft.Icons.EMAIL, color="black"),

                            ft.Text(
                                user["email"],
                                color="black"
                            )
                        ]
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(ft.Icons.PHONE, color="black"),
                            ft.Text(
                                user["telefono"]
                                if user["telefono"]
                                else "Sin teléfono",
                                color="black"
                            )
                        ]
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.Icons.CALENDAR_MONTH, color="black"),
                                    ft.Text(
                                        user["fecha_registro"].strftime("%d/%m/%Y"),
                                        color="black"
                                    )
                                ]
                            )
                        ]
                    ),

                    ft.ElevatedButton(
                        "Cerrar sesión",
                        icon=ft.Icons.LOGOUT,
                        bgcolor=ft.Colors.RED_400,
                        color="black",
                        on_click=cerrar_sesion
                    ),

                    ft.ElevatedButton(
                        "Editar perfil",
                        icon=ft.Icons.EDIT,
                        bgcolor=ft.Colors.BLUE_400,
                        color="black",
                        on_click=editar_perfil
                    ),

                    ft.ElevatedButton(
                        "Eliminar cuenta",
                        icon=ft.Icons.DELETE,
                        bgcolor=ft.Colors.RED_700,
                        color="black",
                        on_click=eliminar_cuenta
                    ),
                ]
            )
        )
    )

    return ft.Container(
        expand=True,
        alignment=ft.Alignment(0, 0),
        content=profile_card
    )