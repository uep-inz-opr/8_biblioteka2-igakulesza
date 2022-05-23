import string

class Biblioteka():
    def __init__(self,operacja):
        self._operacja = operacja



        #self.listaStatusow = list()
    def getOperacja(self):
        return operacja
    def dodaj(self,tytul,autor):
        ksiazka = tytul,autor
        listaKsiazekWBibliotece.append(ksiazka[0].strip())
        listaStatusow.append("True")

    def wypozycz(self,czytelnik,tytul):
        line = czytelnik,tytul
        counterCzytelnika = 0
        if tytul.strip() not in listaKsiazekWBibliotece:
            listaStatusow.append("False")
        elif tytul.strip() in listaKsiazekWBibliotece and line not in listaKsiazkaCzytelnik:
            listaWypozyczonych.append(tytul.strip())
            listaStatusow.append("True")
            listaKsiazekWBibliotece.remove(tytul.strip())
            listaKsiazkaCzytelnik.append(line)
            listaCzytelnikow.append(czytelnik.strip())
        else:
            listaStatusow.append("False")
    def oddaj(self,czytelnik,tytul):
        if tytul.strip() in listaWypozyczonych and czytelnik.strip() in listaCzytelnikow:
           listaWypozyczonych.remove(tytul.strip())
           listaStatusow.append("True")
           listaKsiazekWBibliotece.append(tytul.strip())
           listaCzytelnikow.remove(czytelnik.strip())
        else:
            listaStatusow.append("False")

listaWypozyczonych=[]
listaKsiazkaCzytelnik=[]
listaKsiazekWBibliotece = list()
listaStatusow = []
listaOperacji = []
listaCzytelnikow=[]
ileOperacji = int(input())
for i in range(ileOperacji):
    op = eval(input())
    if op[0].strip() == 'dodaj':
        operacja = Biblioteka(op[0])
        operacja.dodaj(op[1], op[2])
        listaOperacji.append(operacja)

    elif op[0].strip() ==  'wypozycz':
        operacja = Biblioteka(op[0])
        operacja.wypozycz(op[1], op[2])
        listaOperacji.append(operacja)
    else:
        operacja = Biblioteka(op[0])
        operacja.oddaj(op[1], op[2])
        listaOperacji.append(operacja)

for line in listaStatusow:
    print(line)
