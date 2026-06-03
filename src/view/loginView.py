import flet as ft

def LoginView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo electrónico",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=350,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL,
        color=ft.Colors.BLACK
    )

    pass_input = ft.TextField(
        label="Contraseña",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=350,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        color=ft.Colors.BLACK
    )

    error_text = ft.Text("", color=ft.Colors.RED)

    def login_click(e):
        user, msg = auth_controller.login(
            email_input.value,
            pass_input.value
        )

        if user:
            auth_controller.current_user = user
            page.go("/home")
        else:
            error_text.value = msg
            page.update()


    return ft.Container(
        expand=True,
        bgcolor="#FFF8EC",
        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.LOCK,
                    size=70,
                    color="#DCCCAC"
                ),

                ft.Text(
                    "Login",
                    size=32,
                    weight="bold",
                    color=ft.Colors.BLACK
                ),

                ft.Text(
                    "Acceso al sistema",
                    size=18,
                    color=ft.Colors.BLACK
                ),

                email_input,
                pass_input,
                ft.ElevatedButton(
                    "Entrar",
                    on_click=login_click,
                    width=350,
                    height=45,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),

                error_text,

                ft.ElevatedButton(
                    "Crear una cuenta nueva",
                    on_click=lambda _: page.go("/registro"),
                    width=300,
                    height=30,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),

                ft.ElevatedButton(
                    "¿Olvidaste tu contraseña?",
                    on_click=lambda _: page.go("/recuperar-contraseña"),
                    width=300,
                    height=30,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )