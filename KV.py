import sqlite3

conn = sqlite3.connect('kv.db')
kursor = conn.cursor()

kursor.execute('''CREATE TABLE IF NOT EXISTS vodovod (
id INTEGER PRIMARY KEY,
br_lista INTEGER,
vlasnik VARCHAR(100),
br_parcele INTEGER,
pbr_parcele INTEGER,
visina_tla FLOAT,
visina_voda FLOAT,
oznaka VARCHAR(15),
datum VARCHAR(20));''')

#kursor.execute('''CREATE TABLE IF NOT EXISTS kanalizacija (
#id INTEGER PRIMARY KEY,
#br_parcele INTEGER,
#pbr_parcele INTEGER,
#vlasnik VARCHAR(100),
#visina_tla FLOAT,
#visina_voda FLOAT,
#oznaka VARCHAR(15),
#datum DATE;''')

class UnosV(): #unos podataka o vodovima vodovodne mreze
    def __init__(self, id, br_parcele, pbr_parcele, vlasnik, visina_tla, visina_voda, oznaka, datum):
        self.id = id
        self.br_parcele = br_parcele
        self.pbr_parcele = pbr_parcele
        self.vlasnik = vlasnik
        self.visina_tla = visina_tla
        self.visina_voda = visina_voda
        self.oznaka = oznaka
        self.datum = datum
    def __str__(self):
        return str(self.id) + str(self.br_parcele) + str(self.pbr_parcele) + self.vlasnik + str(self.visina_tla) + str(self.visina_voda) + self.oznaka + str(self.datum)
class ListVM(): #vlasnicki list vodoovodne mreze
    def __init__(self, broj, vlasnik):
        self.broj = broj
        self.vlasnik = vlasnik
        self.lista_vm = []
    def dodaj_vod(self, dodaj_vod):
        self.dodaj_vod = dodaj_vod
        self.lista_vm.append(dodaj_vod)
    def __str__(self):
        s = ''
        for i in self.lista_vm:
            s += str(i)
            print(i)
        print(s)
        return s
print('Izaberite vrstu voda za koju zelite da izvrsite promjene: ')
lista_vodova = ['Vodovodna mreza', 'Kanalizaciona mreza', 'Toplovodna mreza', 'Elektroenergetska mreza',
                'Telekomunikaciona mreza', 'Naftovodna mreza', 'Gasovodna mreza']
for i in lista_vodova:
    print(str(i))
unesi = input('Ukoliko zelite da unesete podateke u vodovodnu mrezu, unesite V!\n')
      #'Ukoliko zelite da unesete podateke u kanalizacionu mrezu, unesite K! \n',
      #'Ukoliko zelite da unesete podateke u toplovodnoj mrezu, unesite T!\n',
      #'Ukoliko zelite da unesete podateke u elektroenergetsku mrezu, unesite E!\n',
      #'Ukoliko zelite da unesete podateke u telekomunikacionu mrezu, unesite TT!\n',
      #'Ukoliko zelite da unesete podateke u naftovodnu mrezu, unesite N!\n',
      #'Ukoliko zelite da unesete podateke u gasovodnu mrezu, unesite G!\n')
if unesi == 'V':
    id_v = int(input('Unesite id voda vodovodne mreze: '))
    br_lista = int(input('Unesite broj lista vodova: '))
    vlasnik = input('Unesite ime i prezime vlasnika preko cije parcele se prostire vod: ')
    br_parcele = int(input('Unesite broj parcele preko koje se prostire vod: ')) #ukoliko se vod prostire preko vise parcela, razmisliti kako to definisati
    pbr_parcele = int(input('Unesite podbroj parcele: '))
    visina_tla = float(input('Unesite viisnu tla: '))
    visina_voda = float(input('Unesite visinu voda: '))
    oznaka = input('Unesite oznaku voda: ')
    datum = input('Unesite datum unosa: ')
    #vod1 = UnosV(id_v, br_parcele, pbr_parcele, vlasnik, visina_tla, visina_voda, oznaka, datum)
    #list1 = ListVM(45, 'Test')
    #list1.dodaj_vod(vod1)
    #unos = list(list1)


    #upis = list(unos1)
    #print(upis)
conn.execute("""INSERT INTO vodovod VALUES (int(id_v), br_lista, vlasnik, br_parcele, pbr_parcele, visina_tla, visina_voda, oznaka, datum);""")





    #list1 = ListVM(45,'Test') #ovo je ispis - kreiranje lista vodova
    #list1.dodaj_vod(vod) #ovo je ispis - kreiranje lista vodova








#vrti_petlju = True
#while vrti_petlju:
    #print('Unesite U za unos novih podataka u bazu! \n', 'Za pretragu podataka unesite P! \n', 'Za azuriranje podataka unesite A! \n', 'Za brisanje podataka unesite B!')



conn.commit()

conn.close()

