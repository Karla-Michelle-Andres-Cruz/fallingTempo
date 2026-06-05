import flet as ft

def EditarView(page, auth_controller):

    user = auth_controller.current_user

    nombre_input = ft.TextField(
        label="Nombre",
        value=user["nombre"],
        width=350,
        color=ft.Colors.BLACK
    )

    apellido_input = ft.TextField(
        label="Apellido",
        value=user["apellido"],
        width=350,
        color=ft.Colors.BLACK
    )

    email_input = ft.TextField(
        label="Correo",
        value=user["email"],
        width=350,
        color=ft.Colors.BLACK
    )

    telefono_input = ft.TextField(
        label="Teléfono",
        value=user["telefono"],
        width=350,
        color=ft.Colors.BLACK
    )

    mensaje = ft.Text()

    def guardar_cambios(e):

        success, msg = auth_controller.actualizar_usuario(
            user["id_usuarios"],
            nombre_input.value,
            apellido_input.value,
            email_input.value,
            telefono_input.value
        )

        if success:

            auth_controller.current_user["nombre"] = nombre_input.value
            auth_controller.current_user["apellido"] = apellido_input.value
            auth_controller.current_user["email"] = email_input.value
            auth_controller.current_user["telefono"] = telefono_input.value

            mensaje.value = "✓ Perfil actualizado"
            mensaje.color = ft.Colors.GREEN

        else:
            mensaje.value = msg
            mensaje.color = ft.Colors.RED

        page.update()

    return ft.Container(
        expand=True,
        bgcolor="#FFF8EC",

        content=ft.Column(
            [
                ft.Text(
                    "Editar perfil",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                nombre_input,
                apellido_input,
                email_input,
                telefono_input,

                mensaje,

                ft.ElevatedButton(
                    "Guardar cambios",
                    bgcolor="#99AD7A",
                    color=ft.Colors.BLACK,
                    on_click=guardar_cambios
                ),

                ft.ElevatedButton(
                    "Volver",
                    bgcolor="#99AD7A",
                    color=ft.Colors.BLACK,
                    on_click=lambda _: page.go("/usuarios")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )