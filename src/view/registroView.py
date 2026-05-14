import flet as ft

def RegistroView(page, auth_controller):

    nombre_input = ft.TextField(
        label="Nombre",
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.PERSON
    )

    apellido_input = ft.TextField(
        label="Apellido",
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.BADGE
    )

    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL
    )

    pass_input = ft.TextField(
        label="Contraseña",
        width=350,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    telefono_input = ft.TextField(
        label="Teléfono (opcional)",
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.PHONE
    )

    def registrar_click(e):

        success, msg = auth_controller.registrar_usuario(
            nombre_input.value,
            apellido_input.value,
            email_input.value,
            pass_input.value,
            telefono_input.value
        )

        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            open=True
        )

        page.update()

        if success:
            page.go("/")

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_900,

        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.PERSON_ADD,
                    size=70,
                    color=ft.Colors.PINK_200
                ),

                ft.Text(
                    "SIGE",
                    size=32,
                    weight="bold",
                    color=ft.Colors.WHITE
                ),

                ft.Text(
                    "Crear cuenta nueva",
                    size=18,
                    color=ft.Colors.WHITE70
                ),

                nombre_input,
                apellido_input,
                email_input,
                pass_input,
                telefono_input,

                ft.ElevatedButton(
                    "Registrarse",
                    on_click=registrar_click,
                    width=350,
                    height=45,
                    bgcolor=ft.Colors.PINK_200,
                    color=ft.Colors.WHITE
                ),

                ft.TextButton(
                    "Ya tengo cuenta",
                    on_click=lambda _: page.go("/")
                )

            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            expand=True
        )
    )