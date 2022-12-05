import sqlite3
con = sqlite3.connect('database.db')
cursor = con.cursor()
cursor.execute('''
CREATE TABLE tbuku(
    id char(4) NOT NULL PRIMARY KEY,
    judul VARCHAR(40),
    penulis VARCHAR(25),
    penerbit VARCHAR(30)
    )        
''')

cursor.execute('INSERT INTO tbuku VALUES(?,?,?,?)',
                ('A01', 'Pemrograman Python', 'Blessy Jeniffer', 'Vanda Press'))
cursor.execute('INSERT INTO tbuku VALUES(?,?,?,?)',
                ('A02', 'Pemrograman Flask', 'Brino Ferdinand', 'Vanda Press'))
con.commit()
cursor.close()
con.close()
