from flask_mysqldb import MySQL

def connect_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'vanedilla123'
    app.config['MYSQL_DB'] = 'vanedilla'
    mysql = MySQL(app)
    return mysql