import flet as ft

def UserView(page, auth_controller):

    page.title = "Perfil"
    page.bgcolor = "#13294B"

    user = auth_controller.current_user

    if not user:
        return ft.Container(
            content=ft.Text(
                "No hay sesión iniciada",
                color="white"
            )
        )

    page.navigation_bar = ft.NavigationBar(
        selected_index=1,

        on_change=lambda e:
            page.go("/home")
            if e.control.selected_index == 0
            else page.go("/usuarios"),

        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Inicio"
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="Usuarios"
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                label="Favoritas"
            ),
        ]
    )

    profile_card = ft.Card(
        elevation=15,

        content=ft.Container(
            width=350,
            padding=25,
            border_radius=20,
            bgcolor="#1B365D",

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
                            color="white",
                            weight=ft.FontWeight.BOLD
                        )
                    ),

                    ft.Text(
                        f"{user['nombre']} {user['apellido']}",
                        size=24,
                        color="white",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Divider(color="white24"),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(ft.Icons.EMAIL, color="white70"),

                            ft.Text(
                                user["email"],
                                color="white70"
                            )
                        ]
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(ft.Icons.PHONE, color="white70"),

                            ft.Text(
                                user["telefono"]
                                if user["telefono"]
                                else "Sin teléfono",
                                color="white70"
                            )
                        ]
                    ),
                ]
            )
        )
    )

    return ft.Container(
        expand=True,

        alignment=ft.alignment.center,

        content=profile_card
    )