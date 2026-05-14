import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)

    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"), open=True)
            page.update()
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.data = {"user": user}
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg), open=True)
            page.update()

import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)

    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"), open=True)
            page.update()
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.data = {"user": user}
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg), open=True)
            page.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.AppBar(
                    title=ft.Text("Login", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.PINK_200,
                    center_title=True
                ),
                ft.Column(
                    [
                        ft.Text("Acceso al sistema", size=24, weight="bold", color=ft.Colors.WHITE),
                        email_input,
                        pass_input,
                        ft.ElevatedButton(
                            "Entrar",
                            on_click=login_click,
                            width=350,
                            color=ft.Colors.PINK_200,
                            bgcolor=ft.Colors.BLUE_GREY_700
                            
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        ),
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_700
    )
