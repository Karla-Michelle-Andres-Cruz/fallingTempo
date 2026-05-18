from ast import pattern
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime, time

class UserSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    apellido: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    telefono: Optional[str] = Field(None, pattern=r'^\+?\d{7,15}$')
    
class UsuarioAlta(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    nombre: str = Field(min_length=3, max_length=100)
    apellido: str = Field(min_length=3, max_length=100)
    telefono: Optional[str] = Field(None, pattern=r'^\+?\d{7,15}$')
    
    activo: bool = True
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    ultimo_acceso: datetime = Field(default_factory=datetime.now)