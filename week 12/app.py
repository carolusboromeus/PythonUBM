from flask import Flask, render_template, \
request, redirect, url_for
import pymysql.cursors, os

application = Flask(__name__)

conn = cursor = None
#fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost",user="root",password="",db="db_kelompok" )
    cursor = conn.cursor()

#fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

#fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM daftar"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index.html', container=container,)

#fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        NIM = request.form['NIM']
        openDb()
        sql = "INSERT INTO daftar (NIM,nama,jurusan) VALUES (%s, %s, %s)"
        val = (NIM, nama, jurusan)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

#fungsi view edit() untuk form edit
@application.route('/edit/<NIM>', methods=['GET','POST'])
def edit(NIM):
    openDb()
    cursor.execute('SELECT * FROM daftar WHERE NIM=%s', (NIM))
    data = cursor.fetchone()
    if request.method == 'POST':
        NIM = request.form['NIM']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        sql = "UPDATE daftar SET NIM=%s, nama=%s, jurusan=%s WHERE NIM=%s"
        val = (NIM, nama, jurusan, NIM)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit.html', data=data)

#fungsi untuk menghapus data
@application.route('/hapus/<NIM>', methods=['GET','POST'])
def hapus(NIM):
    openDb()
    cursor.execute('DELETE FROM daftar WHERE NIM=%s', (NIM,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)