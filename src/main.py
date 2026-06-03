import flet as ft
from controllers.userController import AuthController
from view.homeView import HomeView
from view.loginView import LoginView
from view.registroView import RegistroView
from view.recuperarView import RecuperarView
from view.userView import UserView
from view.favoritosView import FavoritosView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    page.bgcolor = ft.Colors.WHITE
    page.navigation_bar = None

    def route_change(e):
        print(f" route_change llamado: {page.route}")
        page.controls.clear()
        if page.route == "/":
            page.controls.append(LoginView(page, auth_ctrl))
        elif page.route == "/registro":
            page.controls.append(RegistroView(page, auth_ctrl))
        elif page.route == "/recuperar-contraseña":
            page.controls.append(RecuperarView(page, auth_ctrl))
        elif page.route == "/home":
            page.controls.append(HomeView(page, auth_ctrl))
        elif page.route == "/usuarios":
            page.controls.append(UserView(page, auth_ctrl))
        elif page.route == "/favoritas":
            page.controls.append(FavoritosView(page, auth_ctrl))
        page.update()
        
    
    
        

    page.on_route_change = route_change
    route_change(None)

def main():
    ft.app(target=start)