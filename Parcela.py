import sqlite3
conn = sqlite3.connect('kv.db')
kursor = conn.cursor()
kursor.execute('''CREATE TABLE IF NOT EXISTS parcela(
br_parcele INTEGER,
pbr_parcele INTEGER,
kultura VARCHAR(15),
klasa INTEGER,
povrsina FLOAT,
sp VARCHAR(5)
);''')


kursor.execute('''CREATE TABLE IF NOT EXISTS vlasnik(
jmbg INTEGER(13) PRIMARY KEY,
ime VARCHAR(50),
prezime VARCHAR(50),
udio VARCHAR(10),
vrsta_svojine VARCHAR(15)
);''')