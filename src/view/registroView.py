import flet as ft

def RegistroView(page, auth_controller):

    nombre_input = ft.TextField(
        label="Nombre",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        prefix_icon=ft.Icons.PERSON,
        color=ft.Colors.BLACK
    )

    apellido_input = ft.TextField(
        label="Apellido",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        prefix_icon=ft.Icons.BADGE,
        color=ft.Colors.BLACK
    )

    email_input = ft.TextField(
        label="Correo electrónico",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        prefix_icon=ft.Icons.EMAIL,
        color=ft.Colors.BLACK
    )

    pass_input = ft.TextField(
        label="Contraseña",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        color=ft.Colors.BLACK
    )

    pass_confirm_input = ft.TextField(
        label="Confirmar contraseña",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        color=ft.Colors.BLACK
    )

    telefono_input = ft.TextField(
        label="Teléfono",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=300,
        border_radius=10,
        prefix_icon=ft.Icons.PHONE,
        color=ft.Colors.BLACK
    )

    def validarPassword(pass1, pass2):
        if pass1 != pass2:
            return False, "Las contraseñas no coinciden"
        if len(pass1) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        return True, ""

    def registrar_click(e):

        if not nombre_input.value or not apellido_input.value or not email_input.value \
            or not pass_input.value or not pass_confirm_input.value or not telefono_input.value:
                page.show_dialog(
                    ft.SnackBar(
                        ft.Text("Por favor, completa todos los campos", color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.RED
                    )
                )
                return

        valido, mensaje = validarPassword(
            pass_input.value,
            pass_confirm_input.value
        )

        if not valido:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text(mensaje, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )
            return

        success, msg = auth_controller.registrar_usuario(
            nombre_input.value,
            apellido_input.value,
            email_input.value,
            pass_input.value,
            pass_confirm_input.value,
            telefono_input.value
        )

        if success:
            page.show_dialog(
                ft.SnackBar(
                    ft.Text("Usuario creado correctamente", color=ft.Colors.WHITE),
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
                    ft.Icons.PERSON_ADD,
                    size=70,
                    color="#DCCCAC"
                ),

                ft.Text(
                    "Crear cuenta nueva",
                    size=25,
                    weight="bold",
                    color=ft.Colors.BLACK
                ),

                nombre_input,
                apellido_input,
                email_input,
                pass_input,
                pass_confirm_input,
                telefono_input,

                ft.ElevatedButton(
                    "Registrarse",
                    on_click=registrar_click,
                    width=300,
                    height=30,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK
                ),
                ft.ElevatedButton(
                    "Ya tengo cuenta",
                    width=300,
                    height=30,
                    bgcolor="#DCCCAC",
                    color=ft.Colors.BLACK,
                    on_click=lambda _: page.go("/")
                )
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            expand=True
        )
    )