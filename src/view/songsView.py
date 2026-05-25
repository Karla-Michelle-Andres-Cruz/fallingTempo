import flet as ft


def SongView(page, song):


    guitar_tabs = """
e|--------------------------------|
B|--------------------------------|
G|------2---3---5-----------------|
D|--------------------------------|
A|--------------------------------|
E|--------------------------------|
"""

    bass_tabs = """
G|----------------|
D|------5---7-----|
A|--5-7-----------|
E|----------------|
"""

    drum_tabs = """
HH|x-x-x-x-x-x-x-x-|
SD|----o-------o---|
BD|o-------o-------|
"""


    instrument_content = ft.Text(
        value=guitar_tabs,
        color="white",
        size=18,
        font_family="Courier New",
    )


    def change_tab(e):

        selected = tabs_control.selected_index

        # GUITARRA
        if selected == 0:
            instrument_content.value = guitar_tabs

        # BAJO
        elif selected == 1:
            instrument_content.value = bass_tabs

        # BATERÍA
        elif selected == 2:
            instrument_content.value = drum_tabs

        page.update()


    def go_back(e):

        page.go("/home")


    tabs_control = ft.Tabs(
        selected_index=0,
        on_change=change_tab,

        tabs=[
            ft.Tab(
                label="Guitarra"
            ),

            ft.Tab(
                label="Bajo"
            ),

            ft.Tab(
                label="Batería"
            ),
        ]
    )


    return ft.Container(
        expand=True,
        bgcolor="#13294B",
        padding=20,

        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="white",
                    on_click=go_back
                ),


                ft.Text(
                    value=song["title"],
                    size=30,
                    color="white",
                    weight=ft.FontWeight.BOLD
                ),


                ft.Text(
                    value=song["artist"],
                    size=18,
                    color="white70"
                ),

                ft.Container(height=20),


                ft.Container(
                    bgcolor="#111111",
                    border_radius=15,
                    padding=15,

                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                        controls=[

                            # BOTONES
                            ft.Row(
                                controls=[

                                    ft.IconButton(
                                        icon=ft.icons.PLAY_ARROW,
                                        icon_color="white"
                                    ),

                                    ft.IconButton(
                                        icon=ft.icons.PAUSE,
                                        icon_color="white"
                                    ),
                                ]
                            ),

                            # TIEMPO
                            ft.Text(
                                value="01:23 / 08:35",
                                color="white"
                            )
                        ]
                    )
                ),

                ft.Container(height=20),


                tabs_control,

                ft.Container(height=20),


                ft.Container(
                    bgcolor="#111111",
                    border_radius=15,
                    padding=20,

                    content=instrument_content
                )
            ]
        )
    )