import flet as ft

def LoginView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo electrónico",
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL,
        color=ft.Colors.WHITE
    )

    pass_input = ft.TextField(
        label="Contraseña",
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        width=350,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        color=ft.Colors.WHITE
    )

    def login_click(e):

        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, complete todos los campos"),
                open=True
            )
            page.update()
            return

        user, msg = auth_controller.login(
            email_input.value,
            pass_input.value
        )

        if user:
            page.data = {"user": user}
            page.go("/dashboard")
        else:
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
                    ft.Icons.LOCK,
                    size=70,
                    color=ft.Colors.PINK_200
                ),

                ft.Text(
                    "Login",
                    size=32,
                    weight="bold",
                    color=ft.Colors.WHITE
                ),

                ft.Text(
                    "Acceso al sistema",
                    size=18,
                    color=ft.Colors.WHITE70
                ),

                email_input,
                pass_input,

                ft.ElevatedButton(
                    "Entrar",
                    on_click=login_click,
                    width=350,
                    height=45,
                    bgcolor=ft.Colors.PINK_200,
                    color=ft.Colors.WHITE
                ),

                ft.TextButton(
                    "Crear una cuenta nueva",
                    on_click=lambda _: page.go("/registro")
                ),

                ft.TextButton(
                    "¿Olvidaste tu contraseña?",
                    on_click=lambda _: page.go("/recuperar-contraseña")
                ),
                
                ft.TextButton(
                    "Home",
                    on_click=lambda _: page.go("/home")
                )
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )