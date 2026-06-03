import flet as ft
import random
from view.songsView import SongView


def HomeView(page, auth_controller):
    page.title = "Tabs Music"
    page.bgcolor = "#FFF8EC"

    def change_tab(e):
        index = e.control.selected_index
        if index == 0:
            page.go("/home")
        elif index == 1:
            page.go("/usuarios")
        elif index == 2:
            page.go("/favoritas")


    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=change_tab,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Inicio"
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="Usuarios"
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                label="Favoritas"
            ),
        ]
    )

    
    songs_data = [
    {
        "title": "afterlife",
        "artist": "Avenged Sevenfold",
        "audio": "afterlife.mp3"

    }]
    
    songs = random.sample(songs_data, len(songs_data))

    title = ft.Text(
        "Buscar",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="black",
    )
    
    def open_song(song):

        page.clean()
        page.add(
            SongView(page, song)
    )

    page.update()

    search_bar = ft.TextField(
        hint_text="Un millón de tablaturas",
        prefix_icon=ft.Icons.SEARCH,
        bgcolor="#FFF8EC",
        border_radius=20,
        border_color="transparent",
        color="black",
    )

    song_column = ft.Column(
        spacing=15,
        scroll=ft.ScrollMode.AUTO
    )

    for index, song in enumerate(songs, start=1):

        song_item = ft.Container(
            on_click=lambda e, s=song: open_song(s),
            ink=True,
            animate=200,
            bgcolor="#FFF8EC",
            border_radius=15,
            padding=15,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"{index}.",
                                color="black",
                                size=18
                            ),

                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        song["title"],
                                        color="black",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                    ft.Text(
                                        song["artist"],
                                        color="black54",
                                        size=16,
                                    ),
                                ],
                            ),
                        ]
                    ),

                    ft.Row(
                        spacing=10,
                        controls=[
                        ],
                    ),
                ],
            ),
        )

        song_column.controls.append(song_item)

    floating_button = ft.Container(
        padding=15,
        bgcolor="#99AD7A",
        border_radius=15,
    )

    return ft.Container(
        bgcolor="#DCCCAC",
        padding=20,
        expand=True,
        content=ft.Column(
            controls=[
                title,
                ft.Container(height=15),
                search_bar,
                ft.Container(height=20),
                song_column,
                ft.Container(height=20),
                floating_button,
            ]
        )
    )