import flet as ft

def FavoritosView(page, auth_controller):
    page.title = "Tabs Music - Favoritas"
    page.bgcolor = "#13294B"

    page.navigation_bar = ft.NavigationBar(
        selected_index=0 if page.route == "/" else 2,
            on_change=lambda e: page.go("/") if e.control.selected_index == 0 else page.go("/favoritas"),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Usuarios"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER, label="Favoritas"),
        ]
    )