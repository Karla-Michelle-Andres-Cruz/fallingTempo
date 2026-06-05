import flet as ft

def RecuperarView(page, auth_controller):

    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
    )

    codigo_input = ft.TextField(
        label="Código",
        width=350,
        border_radius=10,
        visible=False,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
    )

    nueva_pass_input = ft.TextField(
        label="Nueva contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10,
        visible=False,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
    )

    def enviar_codigo(e):

        if not email_input.value:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("Ingrese un correo electrónico", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )
            return

        success, msg = auth_controller.enviar_codigo_recuperacion(
            email_input.value
        )

        if success:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("✓ Código enviado al correo", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREEN
                )
            )
            codigo_input.visible = True
            nueva_pass_input.visible = True
            page.update()
        else:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text(msg, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )

    def cambiar_password(e):

        if not codigo_input.value:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("Ingrese el código recibido", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )
            return

        if not nueva_pass_input.value:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("Ingrese una nueva contraseña", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )
            return

        success, msg = auth_controller.cambiar_password(
            email_input.value,
            codigo_input.value,
            nueva_pass_input.value
        )

        if success:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("✓ Contraseña actualizada correctamente", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREEN
                )
            )
            page.go("/")
        else:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text(msg, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )

    return ft.Container(
        expand=True,
        bgcolor="#FFF8EC",
        alignment=ft.Alignment(0, 0),

        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.LOCK_RESET,
                    size=70,
                    color="#DCCCAC"
                ),

                ft.Text(
                    "Recuperar contraseña",
                    size=30,
                    weight="bold",
                    color=ft.Colors.BLACK
                ),

                email_input,
                codigo_input,
                nueva_pass_input,

                ft.ElevatedButton(
                    "Enviar código",
                    on_click=enviar_codigo,
                    width=350,
                    height=45,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),

                ft.ElevatedButton(
                    "Cambiar contraseña",
                    on_click=cambiar_password,
                    width=350,
                    height=45,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),

                ft.ElevatedButton(
                    "Volver al login",
                    width=350,
                    height=45,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK,
                    on_click=lambda _: page.go("/")
                )
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
