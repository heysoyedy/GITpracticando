from flask import Flask, jsonify, redirect, render_template, request, send_file, url_for, flash
from models.db import connect_db

app = Flask(__name__)

#Conexión BDD
mysql = connect_db(app)

#sett
app.secret_key = 'mysecretkey'


varVanessssssa = 0
varedinsddon = 3



#creamos decorador @app.route
@app.route('/') #ruta principal
def home(): #Las funciones vana  representar las vistas
    # return 'Página de Inicio'    
    data = {
        'titulo':'Vanedilla',
    } #diccionario para enviar valores a nuestra plantilla html
    return render_template('index.html', data=data)




@app.route('/crear_receta', methods=['POST'])
def crear_receta():
    if request.method == 'POST':
        Nombre_Postre = request.form['Nombre_Postre']
        # Imagen_Postre = request.form['Imagen_Postre']
        Descripcion_Postre = request.form['Descripcion_Postre']
        Receta_Postre = request.form['Receta_Postre']
        
        #obtenemos la conexión con la bdd
        cursor = mysql.connection.cursor()
        
        #Escribimos la consulta que queremos realizar
        #Inserta un nuevo postre y sus valores serán los siguientes
        cursor.execute('INSERT INTO postre (Nombre_Postre,Descripcion_Postre,Receta_Postre) VALUES (%s,%s,%s)',
                       (Nombre_Postre,Descripcion_Postre,Receta_Postre))
                    #    (Nombre_Postre,Imagen_Postre,Descripcion_Postre,Receta_Postre))
        
        #Ejecutamos dicha consulta
        mysql.connection.commit()
        flash('Se ha agregado el prostre satisfactoriamente')
        return redirect(url_for('catalogo'))
        
        
        
        
@app.route('/catalogo')
def catalogo():
    data = {
        'titulo': 'Catalogo de Postres',
    }
    recuperar = mysql.connection.cursor()
    recuperar.execute('SELECT * FROM postre')
    datos = recuperar.fetchall()
    return render_template('catalogo.html', datosrecuperados=datos,data=data)




@app.route('/eliminar/<string:id>')
def eliminar_postre(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM postre WHERE id = {0}'.format(id)) #eliminar de la tabla postre el ID que se está enviando
    mysql.connection.commit()
    flash('Se ha eliminado el postre :( )')
    return redirect(url_for('catalogo'))
    



#Si el archivo se está ejecutando es app.py, nuestro archivo principal, if name : arranca todo.
if __name__ == '__main__':
    app.run(debug=True)