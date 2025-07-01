from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Clave secreta para manejar sesiones (necesaria para el login)
app.secret_key = os.urandom(24)

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
# Reemplaza con tus propios datos de PostgreSQL
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_db
DATABASE_URL = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos con la app
db = SQLAlchemy(app)
# --- MODELO DE LA BASE DE DATOS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    # Todos los datos del formulario que ya tenías
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email_institucional = db.Column(db.String(120))
    email_personal = db.Column(db.String(120))
    tel_celular = db.Column(db.String(20))
    tel_fijo = db.Column(db.String(20))
    calle = db.Column(db.String(120))
    numero = db.Column(db.String(20))
    piso = db.Column(db.String(20))
    depto = db.Column(db.String(20))
    torre = db.Column(db.String(20))
    barrio = db.Column(db.String(120))
    codigo_postal = db.Column(db.String(20))
    localidad = db.Column(db.String(120))
    provincia = db.Column(db.String(120))
    pais = db.Column(db.String(120))

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        
        # Busca al usuario en la base de datos
        user = User.query.filter_by(username=username).first()
        
        # ¡YA NO VERIFICAMOS LA CONTRASEÑA!
        # Solo verificamos si el usuario existe en la base de datos.
        if user:
            session['user_id'] = user.id # Guarda el ID del usuario en la sesión
            return redirect(url_for('pagina_principal'))
        else:
            flash('Usuario incorrecto') # Muestra un mensaje de error
            return redirect(url_for('login'))
    
    return render_template('login.html')
@app.route('/principal')
def pagina_principal():
    # 1. Verifica si el usuario está logueado (si su ID está en la sesión)
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    # 2. Obtiene el ID del usuario que inició sesión
    user_id = session['user_id']
    
    # 3. Busca en la base de datos al usuario con ese ID específico
    usuario_logueado = User.query.get(user_id)
    
    # Si no lo encuentra por alguna razón, lo manda al login para más seguridad
    if not usuario_logueado:
        return redirect(url_for('login'))

    # 4. Pasa los datos de ESE usuario a la plantilla HTML
    return render_template('pagina_principal.html', user=usuario_logueado)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)