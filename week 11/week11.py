import sqlite3
con = sqlite3.connect('db_penjualan.db')
cursor = con.cursor()
cursor.execute('''
CREATE TABLE barang(
    id_barang INT NOT NULL auto_increment PRIMARY KEY,
    nama_barang VARCHAR(20) NOT NULL,
    harga INT,
    stok INT
    )        
''')
con.commit()
cursor.close()
con.close()
