class Kasutaja:
    def __init__(self, nimi, vanus, sugu):  # Kasutaja klassi konstruktor, võtab vastu nime, vanuse ja soo
        self.nimi = nimi  # Määrame nime
        self.vanus = vanus  # Määrame vanuse
        self.sugu = sugu  # Määrame soo

    def kuva_andmed(self):  # Meetod kasutaja andmete kuvamiseks
        print("Kasutaja andmed")  # Prindime välja "Kasutaja andmed"
        print("Nimi:", self.nimi)  # Prindime välja nime
        print("Vanus:", self.vanus)  # Prindime välja vanuse
        print("Sugu:", self.sugu)  # Prindime välja soo


class Pank(Kasutaja):  # Panga klass, mis pärineb Kasutaja klassist
    def __init__(self, nimi, vanus, sugu):  # Panga klassi konstruktor, võtab vastu nime, vanuse ja soo
        super().__init__(nimi, vanus, sugu)  # Kutsume Kasutaja klassi konstrukturi
        self.saldo = 0  # Määrame saldoks null

    def sissemakse(self, summa):  # Meetod sissemakse tegemiseks
        self.summa = summa  # Määrame sissemakse summa
        self.saldo = self.saldo + self.summa  # Lisame sissemakse summa saldole
        print("Sissemakse summas: € ", self.saldo)  # Prindime välja sissemakse summa

    def valjavote(self, summa):  # Meetod väljavõtte tegemiseks
        self.summa = summa  # Määrame väljavõtte summa
        if self.summa > self.saldo:  # Kui väljavõtte summa on suurem kui saldo
            print("Vahendeid pole piisavalt väljavõtuks: € ", self.saldo)  # Prindime välja saldo
        else:  # Muul juhul
            self.saldo = self.saldo - self.summa  # Vähendame saldot väljavõtte summaga
            print("Väljavõte summas.", self.saldo)  # Prindime välja sõnumi ja uue saldo

    def vaata_saldo(self):  # Meetod saldole vaatamiseks
        self.kuva_andmed()  # Kutsutakse välja meetod kasutaja andmete kuvamiseks
        print("Kontojääk: € ", self.saldo)  # Prinditakse välja kontojääk


# Küsime kasutajalt andmeid
nimi = input("Sisestage oma nimi: ")  # Küsime kasutajalt nime
vanus = int(input("Sisestage oma vanus: "))  # Küsime kasutajalt vanust

# Küsime soo seni, kuni saame sobiva vastuse
while True:  # Käivitame lõpmatu tsükli
    sugu = input(
        "Sisestage oma sugu (mees/naine): ").lower()  # Küsime kasutajalt soo ja teisendame selle väikesteks tähtedeks
    if sugu in ["mees", "naine"]:  # Kui sugu on mees või naine
        break  # Katkestame tsükli
    else:  # Muul juhul
        print("Vigane sugu! Palun sisestage 'mees' või 'naine'.")  # Prindime välja veateate

# Loome uue kasutaja
kasutaja = Pank(nimi, vanus, sugu)  # Loome uue kasutaja Pank klassi abil

# Kasutaja üksikasjade kuvamine
kasutaja.kuva_andmed()  # Kutsutakse välja meetod kasutaja andmete kuvamiseks

# Sissemakse tegemine
summa = float(input("Sisestage sissemakse summa:"))  # Küsime kasutajalt sissemakse summat
kasutaja.sissemakse(summa)  # Kutsutakse välja meetod sissemakse tegemiseks

# Vaatame saldo
kasutaja.vaata_saldo()  # Kutsutakse välja meetod saldole vaatamiseks

# Väljavõtmine
summa = float(input("Sisestage väljavõetav summa: €"))  # Küsime kasutajalt väljavõetava summat
kasutaja.valjavote(summa)  # Kutsutakse välja meetod väljavõtte tegemiseks

# Vaatame saldo uuesti
kasutaja.vaata_saldo()  # Kutsutakse välja meetod saldole vaatamiseks