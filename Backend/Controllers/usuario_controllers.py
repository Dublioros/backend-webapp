from sqlalchemy.exc import IntegrityError, OperationalError
from fastapi import HTTPException
from sqlalchemy import text
from DataBase.connection import SessionLocal
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime
from Security.function_jwt import get_password_hash


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Listar usuarios
def get_listar_usuario(db):
    try:
        query = text(
            """SELECT
                    usuario_nombres,
                    usuario_apellidos,
                    usuario_email,
                    usuario_dni,
                    tipo_usuario.tipo_usuario_descripcion
                FROM 
                    usuario AS U
                JOIN 
                    tipo_usuario ON U.usuario_tipo_usuario_id = tipo_usuario.tipo_usuario_id 
                WHERE
                    U.status = 1;""")

        usuarios = db.execute(query).fetchall()

        usuarios_listado = []
        for usuario in usuarios:
            usuarios_resultados = {
                "nombres": usuario.usuario_nombres,
                "apellidos": usuario.usuario_apellidos,
                "email": usuario.usuario_email,
                "dni": usuario.usuario_dni,
                "tipo de usuario": usuario.tipo_usuario_descripcion
            }
            usuarios_listado.append(usuarios_resultados)

        return usuarios_listado

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#Eliminar usuario
def get_eliminar_usuario(id_usuario, db):
    try:
        query = text("""
                UPDATE usuario
                SET
                status='0'
                WHERE usuario_id=:id_usuario""")

        result = db.execute(query, {"id_usuario": id_usuario})
        affected_rows = result.rowcount

        if affected_rows > 0:
            return {"mensaje": "El usuario se eliminó correctamente"}
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró el usuario con nombres {id_usuario}")

    except (IntegrityError, OperationalError) as e:
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}")
        
#Listar usuario por el id
def get_listar_usuario_id(id_usuario,db):
    
    try:
        query = text(
            """SELECT
                usuario_nombres, 
                usuario_apellidos, 
                usuario_email,
                usuario_dni
                FROM usuario
                where usuario_id=:id_usuario""")

        usuarios = db.execute(query, {"id_usuario": id_usuario}).fetchone()

        if usuarios:
            usuario_encontrado = {
                "nombres": usuarios.usuario_nombres,
                "apellidos": usuarios.usuario_apellidos,
                "email": usuarios.usuario_email,
                "dni": usuarios.usuario_dni
            }

            return usuario_encontrado
        else:
            raise HTTPException(
                status_code=404, detail="Usuario no encontrado")

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# Registrar Usuario
def get_registrar_usuario(usuario, db):
    password_hash = get_password_hash(usuario.usuario_password)
    try:
        query = text(
        """INSERT INTO usuario (
                usuario_nombres,
                usuario_apellidos,
                usuario_fecha_de_nacimiento,
                usuario_dni,
                usuario_email,           
                usuario_password) 
            VALUES (
                :usuario_nombres,
                :usuario_apellidos,
                :usuario_fecha_de_nacimiento,
                :usuario_dni,
                :usuario_email,
                :hashed_password) 
            """
    )
        db.execute(query, {
                "usuario_nombres": usuario.usuario_nombres,
                "usuario_apellidos": usuario.usuario_apellidos,
                "usuario_fecha_de_nacimiento": usuario.usuario_fecha_de_nacimiento,
                "usuario_dni": usuario.usuario_dni,
                "usuario_email": usuario.usuario_email,
                "hashed_password": password_hash
                })
        db.commit()
        return {"mensaje": "Usuario registrado correctamente", "res": True}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar usuario")