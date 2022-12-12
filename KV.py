import sqlite3

conn = sqlite3.connect('kv.db')
kursor = conn.cursor()

kursor.execute('''CREATE TABLE IF NOT EXISTS vodovod (
id INTEGER PRIMARY KEY,
br_parcele INTEGER,
pbr_parcele INTEGER,
vlasnik VARCHAR(100),
visina_tla FLOAT,
visina_voda FLOAT,
oznaka VARCHAR(15),
datum DATE);''')

kursor.execute('''CREATE TABLE IF NOT EXISTS kanalizacija (
id INTEGER PRIMARY KEY,
br_parcele INTEGER,
pbr_parcele INTEGER,
vlasnik VARCHAR(100),
visina_tla FLOAT,
visina_voda FLOAT,
oznaka VARCHAR(15),
datum DATE);''')



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

class Unos():
    print('Izaberite vrstu voda za koju zelite da izvrsinte promjene: ')
    lista_vodova= ['Vodovodna mreza', 'Kanalizaciona mreza', 'Toplovodna mreza', 'Elektroenergetska mreza', 'Telekomunikaciona mreza', 'Naftovodna mreza', 'Gasovodna mreza']
    for i in lista_vodova:
        print(str(i))
    print('Ukoliko zelite da izvrsite promjene u vodovodnoj mrezi, unesite V!\n','Ukoliko zelite da izvrsite promjene u kanalizacionoj mrezi, unesite K! \n',
          'Ukoliko zelite da izvrsite promjene u toplovodnoj mrezi, unesite T!\n','Ukoliko zelite da izvrsite promjene u elektroenergetskoj mrezi, unesite E!\n',
          'Ukoliko zelite da izvrsite promjene u telekomunikacionoj mrezi, unesite TT!\n','Ukoliko zelite da izvrsite promjene u naftovodnoj mrezi, unesite N!\n',
          'Ukoliko zelite da izvrsite promjene u gasovodnoj mrezi, unesite G!\n')
    #kako se kreira unos u bazu, naci predavanje!!!
    def __init__(self):



vrti_petlju = True
while vrti_petlju:
    print('Unesite U za unos novih podataka u bazu! \n', 'Za pretragu podataka unesite P! \n', 'Za azuriranje podataka unesite A! \n', 'Za brisanje podataka unesite B!')



conn.commit()

conn.close()

