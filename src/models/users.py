import bcrypt
from .dataBase import DataBase


class Usuarios:
    def registrar(self, nombre, apellido, email, password, telefono=None):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')
        query = """
        INSERT INTO usuarios
        (nombre, apellido, email, password, telefono)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (nombre, apellido, email, password_hash, telefono)
        )
        conn.commit()

        cursor.close()
        conn.close()

    def login(self, email, password):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)

        print("EMAIL INGRESADO:", email)

        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s",
            (email,)
        )

        usuario = cursor.fetchone()

        print("USUARIO ENCONTRADO:", usuario)

        cursor.close()
        conn.close()
        if usuario and bcrypt.checkpw(
            password.encode("utf-8"),
            usuario["password"].encode("utf-8")
        ):
            return usuario

        return None

    def buscar_por_id(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM usuarios WHERE id_usuarios = %s",
            (id_usuario,)
        )
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado


    def buscar_por_email(self, email):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s",
            (email,)
        )
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

    def guardar_codigo(self, email, codigo):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO recuperacion_password
        (email, codigo)
        VALUES (%s, %s)
        """
        cursor.execute(query, (email, codigo))
        conn.commit()
        cursor.close()
        conn.close()

    def verificar_codigo(self, email, codigo):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT * FROM recuperacion_password
        WHERE email = %s AND codigo = %s
        """
        cursor.execute(query, (email, codigo))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        return resultado

    def actualizar_password(self, email, nueva_password):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(
            nueva_password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')
        query = """
        UPDATE usuarios
        SET password = %s
        WHERE email = %s
        """
        cursor.execute(query, (password_hash, email))
        conn.commit()

        cursor.close()
        conn.close()

    def eliminar_usuario(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuarios = %s",
            (id_usuario,)
        )

        conn.commit()
        cursor.close()
        conn.close()

    def actualizar_usuario(
        self,
        id_usuario,
        nombre,
        apellido,
        email,
        telefono
    ):
        conn = DataBase.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE usuarios
            SET nombre=%s,
                apellido=%s,
                email=%s,
                telefono=%s
            WHERE id_usuarios=%s
            """,
            (
                nombre,
                apellido,
                email,
                telefono,
                id_usuario
            )
        )

        conn.commit()
        cursor.close()
        conn.close()