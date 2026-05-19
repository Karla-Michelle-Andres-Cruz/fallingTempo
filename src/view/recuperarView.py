import flet as ft

def RecuperarView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10
    )

    codigo_input = ft.TextField(
        label="Código",
        width=350,
        border_radius=10,
        visible=False
    )

    nueva_pass_input = ft.TextField(
        label="Nueva contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10,
        visible=False
    )

    def enviar_codigo(e):
        success, msg = auth_controller.enviar_codigo_recuperacion(
            email_input.value
        )
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        if success:
            codigo_input.visible = True
            nueva_pass_input.visible = True
        page.update()

    def cambiar_password(e):
        success, msg = auth_controller.cambiar_password(
            email_input.value,
            codigo_input.value,
            nueva_pass_input.value
        )
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
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
                    ft.Icons.LOCK_RESET,
                    size=70,
                    color=ft.Colors.PINK_200
                ),

                ft.Text(
                    "Recuperar contraseña",
                    size=30,
                    weight="bold",
                    color=ft.Colors.WHITE
                ),

                email_input,
                codigo_input,
                nueva_pass_input,

                ft.ElevatedButton(
                    "Enviar código",
                    on_click=enviar_codigo,
                    width=350
                ),

                ft.ElevatedButton(
                    "Cambiar contraseña",
                    on_click=cambiar_password,
                    width=350
                )
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )