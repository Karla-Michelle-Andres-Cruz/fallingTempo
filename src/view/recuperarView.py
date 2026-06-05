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

    mensaje_text = ft.Text(
        "",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    def enviar_codigo(e):

        if not email_input.value:
            mensaje_text.value = "Ingrese un correo electrónico"
            mensaje_text.color = ft.Colors.RED
            page.update()
            return

        success, msg = auth_controller.enviar_codigo_recuperacion(
            email_input.value
        )

        if success:
            mensaje_text.value = "✓ Código enviado al correo"
            mensaje_text.color = ft.Colors.GREEN

            codigo_input.visible = True
            nueva_pass_input.visible = True

        else:
            mensaje_text.value = msg
            mensaje_text.color = ft.Colors.RED

        page.update()

    def cambiar_password(e):

        if not codigo_input.value:
            mensaje_text.value = "Ingrese el código recibido"
            mensaje_text.color = ft.Colors.RED
            page.update()
            return

        if not nueva_pass_input.value:
            mensaje_text.value = "Ingrese una nueva contraseña"
            mensaje_text.color = ft.Colors.RED
            page.update()
            return

        success, msg = auth_controller.cambiar_password(
            email_input.value,
            codigo_input.value,
            nueva_pass_input.value
        )

        if success:
            mensaje_text.value = "✓ Contraseña actualizada correctamente"
            mensaje_text.color = ft.Colors.GREEN
            page.update()

            page.go("/")

        else:
            mensaje_text.value = msg
            mensaje_text.color = ft.Colors.RED
            page.update()

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

                mensaje_text,

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