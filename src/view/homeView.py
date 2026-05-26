import flet as ft
import random
from view.songsView import SongView


def HomeView(page, auth_controller):
    page.title = "Tabs Music"
    page.bgcolor = "#13294B"

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
        "title": "Bend the clock",
        "artist": "Dream Theater"
    },

    {
        "title": "Save me",
        "artist": "Avenged Sevenfold"
    },

    {
        "title": "Nightmare to remember",
        "artist": "Dream Theater"
    },

    {
        "title": "Gunslinger",
        "artist": "Avenged Sevenfold"
    },

    {
        "title": "Danger Line",
        "artist": "Avenged Sevenfold"
    },

    {
        "title": "The Count of Tuscany",
        "artist": "Dream Theater"
    },

    {
        "title": "Hail to the King",
        "artist": "Avenged Sevenfold"
    },

    {
        "title": "Dance of Eternity",
        "artist": "Dream Theater"
    },

    {
        "title": "In the Name of God",
        "artist": "Dream Theater"
    },

    {
        "title": "Stream of Consciousness",
        "artist": "Dream Theater"
    }
    ]
    
    songs = random.sample(songs_data, len(songs_data))

    title = ft.Text(
        "Buscar",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="white",
    )
    
    def open_song(song):

        page.clean()
        page.add(
            SongView(page, song)
    )

    page.update()

    search_bar = ft.TextField(
        hint_text="Un millón de tablaturas",
        bgcolor="#4E5D78",
        border_radius=20,
        border_color="transparent",
        color="white",
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
            bgcolor="#111111",
            border_radius=15,
            padding=15,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"{index}.",
                                color="white70",
                                size=18
                            ),

                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        song["title"],
                                        color="white",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                    ft.Text(
                                        song["artist"],
                                        color="white54",
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
        bgcolor="#5A5D8F",
        border_radius=15,
        content=ft.Text(
            "Transcribir con IA",
            color="white",
            weight=ft.FontWeight.BOLD,
        ),
    )

    return ft.Container(
        bgcolor="#13294B",
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