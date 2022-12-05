from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def index():
    import sqlite3,os
    databaseName = os.getcwd() + '/sqlite_db/database.db'
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    container = []
    for id,judul,penulis,penerbit in \
    cursor.execute('Select * From tbuku'):
        container.append((id,judul,penulis,penerbit))
    cursor.close()
    conn.close()
    return render_template('Database.html', container = container)

if __name__ == '__main__':
    application.run(debug=True)