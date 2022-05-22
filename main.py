class Biblioteka():
    def __init__(self,operacja):
        self._operacja = operacja

        self.listaWypozyczonych = list()
       # self.listaStatusow = list()
    def getOperacja(self):
        return operacja
    def dodaj(self,tytul,autor):
        ksiazka = tytul,autor
        listaKsiazekWBibliotece.append(ksiazka)
        listaStatusow.append("True")
    def wypozycz(self,czytelnik,tytul):
        counterCzytelnika = 0

        linia = czytelnik,tytul
        for line in listaKsiazekWBibliotece:
            if tytul == line[0]:
                self.listaWypozyczonych.append(linia)
                listaStatusow.append("True")
                listaKsiazekWBibliotece.remove(line)
                counterCzytelnika +=1
                if counterCzytelnika > 3:
                    listaStatusow.append("False")

    def oddaj(self,czytelnik,tytul):
        linijka = czytelnik,tytul
        if linijka in self.listaWypozyczonych:
           self.listaWypozyczonych.remove(linijka)
        else:
            pass
listaKsiazekWBibliotece = list()
listaStatusow = []
listaOperacji = []
ileOperacji = int(input())
for i in range(ileOperacji):
    op = eval(input())
    if op[0] == 'dodaj':
        operacja = Biblioteka(op[0])
        operacja.dodaj(op[1],op[2])
        listaOperacji.append(operacja)
    elif op[0] == 'wypozycz':
        operacja = Biblioteka(op[0])
        operacja.wypozycz(op[1], op[2])
        listaOperacji.append(operacja)
    else:
        operacja = Biblioteka(op[0])
        operacja.oddaj(op[1], op[2])
        listaOperacji.append(operacja)

for line in listaStatusow:
    print(line)
