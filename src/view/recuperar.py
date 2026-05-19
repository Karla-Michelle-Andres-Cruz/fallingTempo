import flet as ft

def RecuperarView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo electrónico",
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL,
        color=ft.Colors.WHITE
    )

    def recuperar_click(e):

        if not email_input.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, ingrese su correo electrónico"),
                open=True
            )
            page.update()
            return

        success, msg = auth_controller.send_password_reset(email_input.value)

        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            open=True
        )
        page.update()

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_900,
        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.LOCK_RESET,
                    size=70,
                    color=ft.Colors.PINK_200
                ),
                ft.Text(
                    "Recuperar contraseña",
                    style=ft.TextStyle(size=24, weight="bold", color=ft.Colors.WHITE)
                ),
                email_input,
                ft.ElevatedButton(
                    "Enviar enlace de recuperación",
                    on_click=recuperar_click
                ),
                ft.TextButton(
                    "Volver al inicio de sesión",
                    on_click=lambda _: page.go("/login")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )