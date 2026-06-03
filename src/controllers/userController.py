from models.users import Usuarios
from models.schemas import UserSchema, UsuarioAlta
from pydantic import ValidationError

import random
import smtplib
from email.mime.text import MIMEText


class AuthController:
    def __init__(self):
        self.current_user = None
        self.model = Usuarios()

    def registrar_usuario(self, nombre, apellido, email, password, confirm_password, telefono=None):
        try:
            if password != confirm_password:
                return False, "Las contraseñas no coinciden"
            nuevo_usuario = UsuarioAlta(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password,
                confirm_password=confirm_password,
                telefono=telefono
            )
            self.model.registrar(
                nombre=nuevo_usuario.nombre,
                apellido=nuevo_usuario.apellido,
                email=nuevo_usuario.email,
                password=nuevo_usuario.password,
                telefono=nuevo_usuario.telefono
            )
            return True, "Usuario creado correctamente"

        except ValidationError as e:
            return False, e.errors()[0]['msg']
        
    def login(self, email, password):
        try:
            usuario = self.model.login(email, password)
            if usuario:
                return usuario, "Bienvenido"
            return None, "Correo o contraseña incorrectos"
        except Exception as e:
            return None, str(e)

    def enviar_codigo_recuperacion(self, email):
        try:
            usuario = self.model.buscar_por_email(email)

            if not usuario:
                return False, "El correo no existe"
            codigo = str(random.randint(100000, 999999))
            self.model.guardar_codigo(email, codigo)
            remitente = "andres.karlaa@gmail.com"
            password = "jibg ihnk mmwc iqgi"
            mensaje = MIMEText(
                f"Tu código de recuperación es: {codigo}"
            )
            mensaje["Subject"] = "Recuperación de contraseña"
            mensaje["From"] = remitente
            mensaje["To"] = email
            try:
                servidor = smtplib.SMTP("smtp.gmail.com", 587)

                servidor.ehlo()
                servidor.starttls()
                servidor.ehlo()

                servidor.login(remitente, password)

                servidor.send_message(mensaje)

                servidor.quit()

                print("Correo enviado correctamente")

            except Exception as e:
                print("ERROR CORREO:", e)

            return True, "Código enviado al correo"

        except Exception as e:
            return False, str(e)

    def cambiar_password(self, email, codigo, nueva_password):
        try:
            codigo_valido = self.model.verificar_codigo(
                email,
                codigo
            )
            if not codigo_valido:
                return False, "Código incorrecto"
            self.model.actualizar_password(
                email,
                nueva_password
            )
            return True, "Contraseña actualizada"

        except Exception as e:
            return False, str(e)
    
    def HomeView(self, page):
        from view.homeView import HomeView
        return HomeView(page)
    
    def logout(self):
        self.current_user = None

    def eliminar_usuario(self, id_usuario):
        self.model.eliminar_usuario(id_usuario)