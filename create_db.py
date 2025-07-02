# create_db.py

# Importa las variables necesarias de tu aplicación principal
from app import app, db, User

# Datos de los dos usuarios de prueba
usuarios_de_prueba = [
    {
        "username": "juanavedano@soysiglo.edu.ar",
        "password": "juan123", # En un proyecto real, esto debería estar encriptado
        "nombre": "Juan Cruz",
        "apellido": "Avedano",
        "email_institucional": "juancruzavedano@soysiglo21.com",
        "email_personal": "juanavedano2334@gmail.com",
        "tel_celular": "5493516989710",
        "tel_fijo": "5493516989710",
        "calle": "Gardenia", "numero": "253", "piso": "0", "depto": "0", "torre": "0",
        "barrio": "El Talar", "codigo_postal": "5008", "localidad": "Mendiolaza",
        "provincia": "Cordoba", "pais": "Argentina"
    },
    {
        "username": "alesio@soysiglo.edu.ar",
        "password": "ale123",
        "nombre": "Alesio",
        "apellido": "Giudice ",
        "email_institucional": "Alesiogiudi@soysiglo21.com",
        "email_personal": "aleesiogiudi22@gmail.com",
        "tel_celular": "549543123456", "tel_fijo": "549351123456",
        "calle": "Mujica Lainez", "numero": "3252", "piso": "0", "depto": "0", "torre": "0",
        "barrio": "Poeta lugones", "codigo_postal": "5000", "localidad": "Cordoba",
        "provincia": "Cordoba", "pais": "Argentina"
    }
]

# Usamos app_context para que el script sepa a qué base de datos conectarse
with app.app_context():
    print("Creando tablas en la base de datos...")
    # Crea la tabla 'user' (y cualquier otra) si no existe
    db.create_all() 
    
    # Recorre la lista y agrega los usuarios solo si no existen
    for user_data in usuarios_de_prueba:
        if not User.query.filter_by(username=user_data['username']).first():
            new_user = User(**user_data)
            db.session.add(new_user)
            print(f"Usuario '{user_data['username']}' agregado.")

    # Guarda todos los cambios en la base de datos
    db.session.commit()
    print("¡Listo! Base de datos y usuarios creados.")