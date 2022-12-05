from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def index():
    import sqlite3,os
    databaseName = os.getcwd() + 'db_penjualan.db'
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    container = []
    for id_barang,nama_barang,harga,stok in \
    cursor.execute('Select * From barang'):
        container.append((id_barang,nama_barang,harga,stok))
    cursor.close()
    conn.close()
    return render_template('index.html', container = container)

if __name__ == '__main__':
    application.run(debug=True)