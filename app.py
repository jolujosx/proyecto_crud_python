from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Nueva estructura de tabla con Fecha y Prioridad
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tareas 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         nombre TEXT, descripcion TEXT, 
         prioridad TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()



@app.route('/')
def index():
    search = request.args.get('search')
    conn = get_db_connection()
    if search:
        # Buscador profesional con SQL LIKE
        query = "SELECT * FROM tareas WHERE nombre LIKE ? OR descripcion LIKE ?"
        tareas = conn.execute(query, ('%'+search+'%', '%'+search+'%')).fetchall()
    else:
        tareas = conn.execute('SELECT * FROM tareas').fetchall()
    conn.close()
    return render_template('index.html', tareas=tareas)


@app.route('/add', methods=['POST'])
def add():
    nombre = request.form['nombre']
    desc = request.form['descripcion']
    prioridad = request.form['prioridad'] # Nuevo campo
    conn = get_db_connection()
    conn.execute('INSERT INTO tareas (nombre, descripcion, prioridad) VALUES (?, ?, ?)', 
                 (nombre, desc, prioridad))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    if request.method == 'POST':
        nombre, desc = request.form['nombre'], request.form['descripcion']
        conn.execute('UPDATE tareas SET nombre = ?, descripcion = ? WHERE id = ?', (nombre, desc, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    tarea = conn.execute('SELECT * FROM tareas WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', tarea=tarea)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tareas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
