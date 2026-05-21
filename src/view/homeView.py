import flet as ft
import random


def HomeView(page, auth_controller):
    page.title = "Tabs Music"
    page.bgcolor = "#13294B"

    
    song_names = [
        "Broken Dreams",
        "Electric Fire",
        "Night Escape",
        "Silent Thunder",
        "Dark Horizon",
        "Golden Skies",
        "Lost Memories",
        "Neon Lights",
        "Crimson Moon",
        "Fading Stars",
    ]

    artists = [
        "The Wolves",
        "Nova",
        "Black Echo",
        "Skyline",
        "Firestorm",
        "Velvet Sound",
        "Dream Hunters",
        "The Shadows",
        "Unknown Signal",
        "Last Desire",
    ]

    def generate_songs(amount=20):
        songs = []

        for i in range(amount):
            songs.append({
                "title": random.choice(song_names),
                "artist": random.choice(artists)
            })

        return songs

    songs = generate_songs()

    title = ft.Text(
        "Buscar",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="white",
    )

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
