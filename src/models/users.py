import bcrypt
from .dataBase import DataBase

class Usuarios:
    def registrar(self, nombre, apellido, email, password, telefono=None):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        query = """INSERT INTO usuarios (nombre, apellido, email, password, telefono) 
                    VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, apellido, email, password_hash, telefono))
        conn.commit()
        cursor.close()
        conn.close()

    def login(self, email, password):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND activo = 1", (email,))
        usuarios = cursor.fetchone()
        cursor.close()
        conn.close()
        if usuarios and bcrypt.checkpw(password.encode('utf-8'), usuarios['password'].encode('utf-8')):
            return usuarios
        return None

    def buscar_por_id(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado