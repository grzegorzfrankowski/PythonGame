# Gierka RPG
# Grzegorz Frankowski Data Science grupa 1
import sys
import os
import time
import random

#################### Obsługa menu głównego ####################
def title_screen_selections():
    option=input(">").lower()
    if option==("n"):
        setup_game()
    elif option==("p"):
        help_menu()
    elif option==("w"):
        os.system('cls')
        print("########################################")
        print("###          Do zobaczenia!          ###")
        print("########################################")
        sys.exit()
    while option not in ['n', 'p', 'w']:
        print("Proszę wybrać którąś z opcji wpisując symbol podany w nawiasie.")
        title_screen_selections()
def title_screen():
    os.system('cls')
    print("########################################")
    print("############# Witaj w grze #############")
    print("############# DEVIL's NEST #############")
    print("########################################")
    print("###          -Nowa gra(n)-           ###")
    print("###            -Pomoc(p)-            ###")
    print("###           -Wyjście(w)-           ###")
    print("########################################")
    print("###       Copyright 2021 G.F.        ###")
    title_screen_selections()
def help_menu():
    os.system('cls')
    print("########################################")
    print("############# Witaj w grze #############")
    print("############# DEVIL's NEST #############")
    print("########################################")
    print("###     Gra polega na wpisywaniu     ###")
    print("###    w konsoli literek podanych    ###")
    print("### w nawiasach przy interesujących  ###")
    print("###         nas poleceniach.         ###")
    print("###   Nowa gra(n)   |    Wyjście(w)  ###")
    print("########################################")
    print("###       Copyright 2021 G.F.        ###")
    title_screen_selections()

#################### Obsługa rejestracji i logowania ####################
def register():
    db=open("data_login.csv", "r")
    print("########################################")
    print("############# Witaj w grze #############")
    print("############# DEVIL's NEST #############")
    print("########################################")
    username=input("Podaj nazwę użytkownika: ")
    password=input("Podaj hasło: ")
    password1=input("Potwierdź hasło: ")
    d = []
    f = []
    for line in db:
        if ', ' in line:
            key, value = line.strip().split(', ')
            d.append(key)
            f.append(value)
    data = dict(zip(d, f))


    if password!=password1:
        print("Hasła nie pasują do siebie, spróbuj ponownie.")
        register()
    else:
        if len(username)<2:
            print("Nazwa użytkownika jest za krótka, spróbuj ponownie.")
            register()
        elif len(password)<=4:
            print("Hasło musi składać się z conajmniej 5 znaków. Spróbuj ponownie.")
            register()
        elif username in d:
            print("Nazwa użytkownika jest zajęta")
            register()
        else:
            db=open("data_login.csv", "a")
            db.write(username+', '+password+"\n")
            print("Rejestracja powiodła się! Przy ponownym uruchomieniu będziesz mógł/mogła się zalogować.")
            time.sleep(4)
def access():
    db = open("data_login.csv", "r")
    print("########################################")
    print("############# Witaj w grze #############")
    print("############# DEVIL's NEST #############")
    print("########################################")
    username = input("Podaj nazwę użytkownika: ")
    password = input("Podaj hasło: ")

    if not len(username or password)<1:
        d = []
        f = []
        for line in db:
            if ', ' in line:
                key, value = line.strip().split(', ')
                d.append(key)
                f.append(value)
        data = dict(zip(d, f))

        try:
            if data[username]:
                if password==data[username]:
                    os.system('cls')
                    print("Zalogowano")
                    print(f"Witaj, {username}")
                    time.sleep(1)
                    title_screen()
                else:
                    print("Nazwa lub hasło nieprawidłowe")
            else:
                print("Użytkownik o takiej nazwie nie istnieje.")
        except KeyError:
            os.system('cls')
            print("Podany login nie istnieje.")
            time.sleep(1.5)
            os.system('cls')
            access()
def home(option=None):
    print("########################################")
    print("############# Witaj w grze #############")
    print("############# DEVIL's NEST #############")
    print("########################################")
    option=input("###   Logowanie(l) | Rejestracja(r)  ###\n wybierz opcję z menu: >").lower()
    if option=="l":
        os.system('cls')
        access()
    elif option=="r":
        os.system('cls')
        register()
    else:
        os.system('cls')
        print("Proszę wybrać którąś z opcji wpisując symbol podany w nawiasie.")
        time.sleep(1.8)
        os.system('cls')
        home()

#################### Tworzenie klasy Enemy ####################
class Enemy():
    def __init__(self, imie):
        self.imie=imie
        self.punkty_zycia=0
        self.punkty_ataku=0
        self.punkty_obrony=0
        self.loot=random.randint(0, 2)
class Szkielet(Enemy):
    imie="Szkielet"
    punkty_zycia = 18
    punkty_ataku = 3
    punkty_obrony = 1.5
    loot = random.randint(0, 2)
class Demon(Enemy):
    imie="Demon"
    punkty_zycia = 22
    punkty_ataku = 4
    punkty_obrony = 2
    loot = random.randint(0, 2)
class Sam_Diabel_Wcielony(Enemy):
    imie="Sam Diabeł Wcielony"
    punkty_zycia = 35
    punkty_ataku = 7
    punkty_obrony = 3
    loot = random.randint(0, 2)

#################### Tworzenie klasy Bohater ####################
class Bohater:
    def __init__(self, imie):
        self.imie=imie
        self.__sila=0
        self.inteligencja=0
        self.zwinnosc=0
        self.punkty_zycia=0
        self.punkty_ataku=0
        self.punkty_obrony=0

    def get_sila(self):
        return self.__sila
    def przedstaw_sie(self):
        print(f"{myhero.imie}: ")
        prz=(f'"Jestem {str(myhero.imie)}, W pas się kłaniam!"\n')
        for character in prz:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
    def atakuj(self):
        print(f"{myhero.imie}: ")
        okrzyk=(f'"Giń plugawa bestio!"\n')
        for character in okrzyk:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{enemy.imie}: ")
        okrzyk2=(f'"Wolobloboblo!"\n')
        for character in okrzyk2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        os.system('cls')
    def atakujBossa(self):
        print(f"{myhero.imie}: ")
        okrzyk = (f'"Giń plugawa bestio!"\n')
        for character in okrzyk:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{enemy.imie}: ")
        okrzyk2 = (f'"Zważaj na słowa śmiertelne ścierwo!"\n')
        for character in okrzyk2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        os.system('cls')
    def uciekaj(self):
        os.system('cls')
        print(f"{myhero.imie}: ")
        uciek = (f'"W wynikłej sytuacji postanawiam wziąć nogi za pas :|"\n')
        for character in uciek:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{enemy.imie}: ")
        uciek2 = (f'"Bleee wracaj tu!"\n')
        for character in uciek2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        os.system('cls')
    def rozmawiaj(self):
        os.system('cls')
        print(f"{myhero.imie}: ")
        talk1 = (f'"Może zamiast walczyć najpierw porozmawiamy?"\n')
        for character in talk1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{enemy.imie}: ")
        talk2 = (f'"Gebelebeble giń brlurrblr!"\n')
        for character in talk2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{myhero.imie}: ")
        talk3 = (f'"Chyba się nie dogadamy..."\n')
        for character in talk3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
    def rozmawiajzBossem(self):
        os.system('cls')
        print(f"{myhero.imie}: ")
        talk1 = (f'"Tylko ty dzielisz mnie od zwycięstwa dla ludzkości!"\n')
        for character in talk1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{enemy.imie}: ")
        talk2 = (f'"Nie mów do mnie jak do równego sobie. Jesteś ledwie śmiertelnym pyłem,\n'
                 f'któremu tacy jak ja łaskawie pozwalają istnieć."\n')
        for character in talk2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
        print(f"{myhero.imie}: ")
        talk3 = (f'"Uważaj, żeby ten pył nie wpadł Ci do oka."\n')
        for character in talk3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
class Egzorcysta(Bohater):
    imie='imie'
    __sila=5
    inteligencja=10
    zwinnosc=7
    punkty_zycia=95
    punkty_ataku=8
    punkty_obrony=7
    swietosc=15
    charyzma=10

    def przedstaw_sie(self):
        print(f"{myhero.imie}: ")
        prz=(f'"Jestem {str(myhero.imie)}, Egzorcysta. W pas się kłaniam!"\n')
        for character in prz:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
    def SwietaTarcza(self):
        rzodkiew=f'{enemy.imie} widząc Cię w blasku Mocy Światła, nie będzie miał odwagi atakować z pełną siłą.\n'
        for character in rzodkiew:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        tekst="Twój przeciwnik zada Ci połowę obrażeń.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        enemy.punkty_ataku=enemy.punkty_ataku/2
    def Charyzma(self):
        tekst = f'Twoja charyzma sprawia, że {enemy.imie} nie będzie w stanie bronić się przed ciosami.\n'
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        enemy.punkty_obrony=1
class Swiety_Strzelec(Bohater):
    imie = 'imie'
    __sila=7
    inteligencja=6
    zwinnosc=6
    punkty_zycia=90
    punkty_ataku=8
    punkty_obrony=5
    super_damage=7
    super_obrona=15

    def przedstaw_sie(self):
        print(f"{myhero.imie}: ")
        prz=(f'"Jestem {str(myhero.imie)}, Święty Strzelec. W pas się kłaniam!"\n')
        for character in prz:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
    def SuperDamage(self):
        tekst = "Moc Światła znacząco zwiększa moc twoich strzałów.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        myhero.punkty_ataku = myhero.punkty_ataku+myhero.super_damage
    def SuperObrona(self):
        tekst = "Moc Światła znacząco zwiększa twoją obronę.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        myhero.punkty_obrony = myhero.punkty_obrony + myhero.super_obrona
class Kaplanka_Swiatla(Bohater):
    imie = 'imie'
    __sila=4
    inteligencja=12
    zwinnosc=6
    punkty_zycia=85
    punkty_ataku=7
    punkty_obrony=12
    szczescie=20
    restart_hp=25

    def przedstaw_sie(self):
        print(f"{myhero.imie}: ")
        prz=(f'"Jestem {str(myhero.imie)}, Kapłanka Światła. W pas się kłaniam!"\n')
        for character in prz:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
    def Szczescie(self):
        tekst = "Moc Światła pozwala na nadludzką siłę gdy będziesz na skraju śmierci.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        if myhero.punkty_zycia<20:
            myhero.punkty_ataku = myhero.punkty_ataku + myhero.szczescie
    def RestartHP(self):
        tekst = "Moc Światła przywraca Ci siły witalne.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        myhero.punkty_zycia = myhero.punkty_zycia + myhero.restart_hp
class Dobry_Diabel(Bohater):
    imie = 'imie'
    __sila=10
    inteligencja=5
    zwinnosc=6
    punkty_zycia=112
    punkty_ataku=7
    punkty_obrony=10
    no_mercy=40
    fun_begins=15

    def przedstaw_sie(self):
        print(f"{myhero.imie}: ")
        prz=(f'"Jestem {str(myhero.imie)}, Dobry Diabeł. W pas się kłaniam!"\n')
        for character in prz:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
    def NoMercy(self):
        tekst = "Moc Światła pozwala Ci wykończyć przeciwnika, gdy oboje jesteście bliscy śmierci.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        if enemy.punkty_zycia<12 and myhero.punkty_zycia<20:
            myhero.punkty_ataku = myhero.punkty_ataku + myhero.no_mercy
    def FunBegins(self):
        tekst = f"Moc Światła zwiększa twoją obronę, dopóki {enemy.imie} jest w pełni sił.\n"
        for character in tekst:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        if enemy.punkty_zycia < 15:
            myhero.punkty_obrony = myhero.punkty_obrony + myhero.fun_begins
#################### Funkcjonowanie gry ####################
def GameOver(myhero, score):
    if myhero.punkty_zycia<=0:
        os.system('cls')
        smierc="W związku z utratą całego zdrowia postanowiłeś umrzeć...\n GAME OVER\n"
        for character in smierc:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1.5)
        wynik=f"Udało Ci się zdobyć {score} punktów!"
        for character in wynik:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1.5)
        exit()
def Choose_hero():
    os.system('cls')
    global myhero
    Pytanie1=("Na początek, jak chcesz nazwać swoją postać?: ")
    for character in Pytanie1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    heroname=input('>')
    os.system('cls')
    Pytanie1a=(f"Świetnie, witaj {heroname}.")
    for character in Pytanie1a:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    klasa=input('  Jaką klasę chcesz wybrać dla swojej postaci?\n'
                'Egzorcysta(e)/ Święty Strzelec(s)/ Kapłanka Światła(k)/ Dobry Diabeł(d):').lower()
    variable=['e','s','k','d']
    while klasa not in variable:
        print("Nieprawidłowa wartość")
        klasa = input('Jaką klasę chcesz wybrać dla swojej postaci?\n'
                      'Egzorcysta(e)/ Święty Strzelec(s)/ Kapłanka Światła(k)/ Dobry Diabeł(d):').lower()
    if klasa == 'e':
        myhero=Egzorcysta
        myhero.imie=heroname
        teskt=(f'Świetny wybór. Powodzenia, Egzorcysto {str(heroname)}!')
        for character in teskt:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        return myhero
    if klasa == 's':
        myhero=Swiety_Strzelec
        myhero.imie = heroname
        teskt=(f'Świetny wybór. Powodzenia, Święty Strzelcu {heroname}!')
        for character in teskt:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        return myhero
    if klasa == 'k':
        myhero=Kaplanka_Swiatla
        myhero.imie = heroname
        teskt=(f'Świetny wybór. Powodzenia, Kapłanko Światła {heroname}!')
        for character in teskt:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        return myhero
    if klasa == 'd':
        myhero=Dobry_Diabel
        myhero.imie = heroname
        teskt=(f'Świetny wybór. Powodzenia, Dobry Diable {heroname}!')
        for character in teskt:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        return myhero
def loot():
    loot=["MiksturaPŻ","Miecz","Tarcza"]
    lootChance=random.randint(0,2)
    lootDrop=loot[lootChance]
    return lootDrop
def lootEffect(lootDrop, myhero):
    if lootDrop=="MiksturaPŻ":
        myhero.punkty_zycia=myhero.punkty_zycia+15
        tresc1="Wypiłeś miksturę która przywraca Ci siły witalne.\n"
        for character in tresc1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        tresc11 = f"Posiadasz teraz {round(myhero.punkty_zycia)} zdrowia.\n"
        for character in tresc11:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)

    elif lootDrop=="Miecz":
        myhero.punkty_ataku=myhero.punkty_ataku+2
        tresc2="Nowy, ostrzejszy miecz uczyni twoje ataki bardziej zabójczymi.\n"
        for character in tresc2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        tresc22 = f"Posiadasz teraz {myhero.punkty_ataku} ataku.\n"
        for character in tresc22:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)

    elif lootDrop=="Tarcza":
        myhero.punkty_obrony=myhero.punkty_obrony+2
        tresc3="Nowa, wytrzymalsza tarcza uczyni twoją obronę jeszcze szczelniejszą.\n"
        for character in tresc3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        tresc33 = f"Posiadasz teraz {myhero.punkty_obrony} obrony.\n"
        for character in tresc33:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.8)
def enemyselect(Szkielet, Demon):
    enemyList=[Szkielet, Demon]
    chance=random.randint(0,1)
    enemy=enemyList[chance]
    return enemy
def setup_game():
    myhero = Choose_hero()
    os.system('cls')
    myhero.przedstaw_sie(myhero);
    # if myhero==Egzorcysta:
    #     myhero.przedstaw_sie(Egzorcysta)
    # elif myhero==Swiety_Strzelec:
    #     myhero.przedstaw_sie(Swiety_Strzelec)
    # elif myhero==Kaplanka_Swiatla:
    #     myhero.przedstaw_sie(Kaplanka_Swiatla)
    # elif myhero==Dobry_Diabel:
    #     myhero.przedstaw_sie(Dobry_Diabel)

    os.system('cls')
    speech1="Istoty piekielne sieją spustoszenie w krainie ludzi.\n"
    speech2="Ludzkość ledwo odpiera ich ataki.\n"
    speech3="Skoro nie można sobie z nimi poradzić na powierzchni...\n"
    speech4=f"...bohater {myhero.imie} postanawia zejść w najgłębsze odmęty piekła...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.25)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.2)
    os.system('cls')
    print('#####################################################')
    print('###############      Zaczynajmy!      ###############')
    print('#####################################################')
    time.sleep(1.5)
    os.system('cls')
    battlestate(score)
def battlestate(score):
    global enemy
    if score<50:
        enemy=enemyselect(Szkielet, Demon)
        tekst1=(f"Przerażający {str(enemy.imie)} pojawił się na twojej drodze!\n")
        tekst2=("Co robisz?\n")
        for character in tekst1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        for character in tekst2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
        while enemy.punkty_zycia>0:
            choice=input("Atak(a) - 70% szans/ Rozmowa(r)/\nUcieczka(u) - 60% szans/ Ruch specjalny(s) - 40% szans: ").lower()
            if choice=="a":
                os.system('cls')
                myhero.atakuj(Bohater)
                tekst3 = (f"Wymierzasz cios, {str(enemy.imie)} czeka...\n")
                for character in tekst3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)
                hitchance = random.randint(1, 10)
                if hitchance > 3 and hitchance<=7:
                    enemy.punkty_zycia = enemy.punkty_zycia - (myhero.punkty_ataku/enemy.punkty_obrony)
                    tekst4 = (f"Trafiłeś, przeciwnikowi pozostało {(round(enemy.punkty_zycia))} zdrowia.\n")
                    for character in tekst4:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

                    if enemy.punkty_zycia > 0:
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)
                        GameOver(myhero, score)

                    else:
                        if enemy.imie == "Szkielet":
                            enemy.punkty_zycia = 18
                            enemy.punkty_ataku = 3
                            enemy.punkty_obrony = 1.5
                            score=score+14
                            if myhero==Egzorcysta:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 7
                            elif myhero==Swiety_Strzelec:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 5
                            elif myhero==Kaplanka_Swiatla:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 12
                            elif myhero==Dobry_Diabel:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 10
                        elif enemy.imie == "Demon":
                            enemy.punkty_zycia = 22
                            enemy.punkty_ataku = 4
                            enemy.punkty_obrony = 2
                            score=score+17
                            if myhero==Egzorcysta:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 7
                            elif myhero==Swiety_Strzelec:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 5
                            elif myhero==Kaplanka_Swiatla:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 12
                            elif myhero==Dobry_Diabel:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 10


                        os.system('cls')
                        win1 = (f"Wygrałeś! {str(enemy.imie)} został pokonany!\n")
                        for character in win1:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        win2 = ("Wygląda na to że coś upuścił!\n")
                        for character in win2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        lootDrop = loot()
                        win3 = (f"Zdobyty przedmiot: {lootDrop}!\n")
                        for character in win3:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)

                        lootEffect(lootDrop, myhero)
                        print(f"Wynik: {score}")
                        time.sleep(1.2)
                        os.system('cls')
                        battlestate(score)
                        return score
                elif hitchance>7:
                    enemy.punkty_zycia = enemy.punkty_zycia - myhero.punkty_ataku
                    tekst4 = (f"Trafiłeś krytycznie, przeciwnikowi pozostało {(round(enemy.punkty_zycia))} zdrowia.\n")
                    for character in tekst4:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

                    if enemy.punkty_zycia > 0:
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)
                        GameOver(myhero, score)

                    else:
                        if enemy.imie == "Szkielet":
                            enemy.punkty_zycia = 18
                            enemy.punkty_ataku = 3
                            enemy.punkty_obrony = 1.5
                            score = score + 14
                            if myhero==Egzorcysta:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 7
                            elif myhero==Swiety_Strzelec:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 5
                            elif myhero==Kaplanka_Swiatla:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 12
                            elif myhero==Dobry_Diabel:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 10
                        elif enemy.imie == "Demon":
                            enemy.punkty_zycia = 22
                            enemy.punkty_ataku = 4
                            enemy.punkty_obrony = 2
                            score = score + 17
                            if myhero==Egzorcysta:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 7
                            elif myhero==Swiety_Strzelec:
                                myhero.punkty_ataku = 8
                                myhero.punkty_obrony = 5
                            elif myhero==Kaplanka_Swiatla:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 12
                            elif myhero==Dobry_Diabel:
                                myhero.punkty_ataku = 7
                                myhero.punkty_obrony = 10

                        os.system('cls')
                        win1 = (f"Wygrałeś! {str(enemy.imie)} został pokonany!\n")
                        for character in win1:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        win2 = ("Wygląda na to że coś upuścił!\n")
                        for character in win2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        lootDrop = loot()
                        win3 = (f"Zdobyty przedmiot: {lootDrop}!\n")
                        for character in win3:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)

                        lootEffect(lootDrop, myhero)
                        print(f"Wynik: {score}")
                        time.sleep(1.2)
                        os.system('cls')
                        battlestate(score)
                        return score
                else:
                    tekst6 = (f"Potknąłeś się o kamień, ratując równowagę chybiłeś cios :(\n")
                    for character in tekst6:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    tekst7 = (f"{str(enemy.imie)} trafia Cię krytycznie!\n")
                    for character in tekst7:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    myhero.punkty_zycia = myhero.punkty_zycia - enemy.punkty_ataku
                    tekst8 = (f"Zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst8:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    GameOver(myhero, score)
            elif choice=="u":
                myhero.uciekaj(Bohater)
                runchance = random.randint(1, 10)
                if runchance > 4:
                    uciek3 = "Udało Ci się uciec bez zadrapania.\n"
                    for character in uciek3:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.8)
                    os.system('cls')
                    battlestate(score)
                else:
                    uciek4="Próbujesz uciec, ale łapie Cię kolka i tak średnio to wychodzi.\n"
                    for character in uciek4:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.8)
                    uciek5=f"{enemy.imie} dogania Cię i trafia krytycznie!\n"
                    for character in uciek5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.8)
                    myhero.punkty_zycia = myhero.punkty_zycia - enemy.punkty_ataku
                    uciek6 = (f"Zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in uciek6:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    GameOver(myhero, score)
            elif choice=='r':
                myhero.rozmawiaj(Bohater)
            elif choice=='s':
                os.system('cls')
                print(f"{myhero.imie}: ")
                prosba=f'"Pradawna Mocy Światła, ja {myhero.imie} wzywam Cię do pomocy!"\n'
                for character in prosba:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)

                if myhero==Egzorcysta:
                    specialChance = random.randint(0, 4)
                    if specialChance==0:
                        myhero.Charyzma(Egzorcysta)
                    elif specialChance==1:
                        myhero.SwietaTarcza(Egzorcysta)
                    else:
                        tekscik="Nie udało się wezwać Mocy Światła :(\n"
                        for character in tekscik:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)

                elif myhero==Swiety_Strzelec:
                    specialChance = random.randint(0, 4)
                    if specialChance == 0:
                        myhero.SuperDamage(Swiety_Strzelec)
                    elif specialChance == 1:
                        myhero.SuperObrona(Swiety_Strzelec)
                    else:
                        tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                        for character in tekscik:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)

                elif myhero == Kaplanka_Swiatla:
                    specialChance = random.randint(0, 4)
                    if specialChance == 0:
                        myhero.Szczescie(Kaplanka_Swiatla)
                    elif specialChance == 1:
                        myhero.RestartHP(Kaplanka_Swiatla)
                    else:
                        tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                        for character in tekscik:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)

                elif myhero == Dobry_Diabel:
                    specialChance = random.randint(0, 4)
                    if specialChance == 0:
                        myhero.NoMercy(Dobry_Diabel)
                    elif specialChance == 1:
                        myhero.FunBegins(Dobry_Diabel)
                    else:
                        tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                        for character in tekscik:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.5)
                        myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                        tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                        for character in tekst5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(0.5)
            else:
                os.system('cls')
                print("Wybrano nieprawidłową wartość.")
    else:
        bossfight(score)
def bossfight(score):
    global enemy
    enemy=Sam_Diabel_Wcielony
    tekst1=(f"W powietrzu idzie wyczuć potężny odór siarki.\n")
    tekst2=("Zdecydowanie zbliża się coś bardzo złego...\n")
    tekst21=(" To... \n")
    tekst3=(f"{str(enemy.imie)}!!!\n")
    tekst4 = ("Co robisz?\n")
    for character in tekst1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    for character in tekst2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in tekst21:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    for character in tekst3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.8)
    for character in tekst4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.5)
    while enemy.punkty_zycia>0:
        choice = input("Atak(a) - 70% szans/ Rozmowa(r)/\nUcieczka(u) - 60% szans/ Ruch specjalny(s) - 40% szans: ").lower()
        if choice=="a":
            os.system('cls')
            myhero.atakujBossa(Bohater)
            tekst3 = (f"Wymierzasz cios, {str(enemy.imie)} czeka...\n")
            for character in tekst3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
            hitchance = random.randint(1, 10)
            if hitchance > 3 and hitchance<=7:
                enemy.punkty_zycia = enemy.punkty_zycia - (myhero.punkty_ataku/enemy.punkty_obrony)
                tekst4 = (f"Trafiłeś, przeciwnikowi pozostało {(round(enemy.punkty_zycia))} zdrowia.\n")
                for character in tekst4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.03)
                time.sleep(0.5)

                if enemy.punkty_zycia > 0:
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)
                    GameOver(myhero, score)

                else:
                    if enemy.imie == "Sam Diabeł Wcielony":
                        enemy.punkty_zycia = 35
                        score=score+50
                        if myhero == Egzorcysta:
                            myhero.punkty_ataku = 8
                            myhero.punkty_obrony = 7
                        elif myhero==Swiety_Strzelec:
                            myhero.punkty_ataku = 8
                            myhero.punkty_obrony = 5
                        elif myhero == Kaplanka_Swiatla:
                            myhero.punkty_ataku = 7
                            myhero.punkty_obrony = 12
                        elif myhero == Dobry_Diabel:
                            myhero.punkty_ataku = 7
                            myhero.punkty_obrony = 10


                    os.system('cls')
                    print(f"{enemy.imie}: ")
                    win1 = (f'"Może i udało Ci się mnie pokonać, jednak zabijając mnie nie pozbędziesz się Diabła..."\n')
                    for character in win1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    print(f"{enemy.imie}: ")
                    win2 = ('"Diabeł powstaje w sercach ludzi. Tak długo jak ludzie będą czynić zło, tak długo Diabeł będzie się odradzał..."\n')
                    for character in win2:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(1)
                    print(f"{enemy.imie}: ")
                    win3 = (f'"Bleeeh!..."\n')
                    for character in win3:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    time.sleep(1)
                    print(f"{enemy.imie}: ")
                    win3 = (f'"Do... widzenia... "\n')
                    for character in win3:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    time.sleep(1.8)
                    os.system('cls')
                    end1=f"Udało Ci się! {enemy.imie} został pokonany i chwilowo zagrożenie dla ludzi minęło.\n"
                    for character in end1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    end2 = f"Imię {myhero.imie} będzię sławione w całym świecie!\n"
                    for character in end2:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    end1 = f"Dziękujemy za grę. Świetnie sobie poradziłeś, a Grzechu stworzył super grę!\n"
                    for character in end1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.8)
                    print(f"Wynik: {score}")
                    time.sleep(1.5)
                    print("T H E   E N D")
                    time.sleep(5)
                    os.system('cls')
                    return score
                    exit(0)

            elif hitchance > 7:
                enemy.punkty_zycia = enemy.punkty_zycia - myhero.punkty_ataku
                tekst4 = (f"Trafiłeś krytycznie, przeciwnikowi pozostało {(round(enemy.punkty_zycia))} zdrowia.\n")
                for character in tekst4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.03)
                time.sleep(0.5)

                if enemy.punkty_zycia > 0:
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)
                    GameOver(myhero, score)


                else:
                    if enemy.imie == "Sam Diabeł Wcielony":
                        enemy.punkty_zycia = 35
                        score = score + 50
                        if myhero == Egzorcysta:
                            myhero.punkty_ataku = 8
                            myhero.punkty_obrony = 7
                        elif myhero == Swiety_Strzelec:
                            myhero.punkty_ataku = 8
                            myhero.punkty_obrony = 5
                        elif myhero == Kaplanka_Swiatla:
                            myhero.punkty_ataku = 7
                            myhero.punkty_obrony = 12
                        elif myhero == Dobry_Diabel:
                            myhero.punkty_ataku = 7
                            myhero.punkty_obrony = 10

                    os.system('cls')
                    print(f"{enemy.imie}: ")
                    win1 = (f'"Może i udało Ci się mnie pokonać, jednak zabijając mnie nie pozbędziesz się Diabła..."\n')
                    for character in win1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    print(f"{enemy.imie}: ")
                    win2 = ('"Diabeł powstaje w sercach ludzi. Tak długo jak ludzie będą czynić zło, tak długo Diabeł będzie się odradzał..."\n')
                    for character in win2:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(1)
                    print(f"{enemy.imie}: ")
                    win3 = (f'"Bleeeh!..."\n')
                    for character in win3:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    time.sleep(1)
                    print(f"{enemy.imie}: ")
                    win3 = (f'"Do... widzenia... "\n')
                    for character in win3:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    time.sleep(1.8)
                    os.system('cls')
                    end1 = f"Udało Ci się! {enemy.imie} został pokonany i chwilowo zagrożenie dla ludzi minęło.\n"
                    for character in end1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    end2 = f"Imię {myhero.imie} będzię sławione w całym świecie!\n"
                    for character in end2:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    end1 = f"Dziękujemy za grę. Świetnie sobie poradziłeś, a Grzechu stworzył super grę!\n"
                    for character in end1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.8)
                    print(f"Wynik: {score}")
                    time.sleep(1.5)
                    print("T H E   E N D")
                    time.sleep(5)
                    os.system('cls')
                    return score
                    exit(0)


            else:
                tekst6 = (f"Potknąłeś się o kamień, ratując równowagę chybiłeś cios :(\n")
                for character in tekst6:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)
                tekst7 = (f"{str(enemy.imie)} trafia Cię krytycznie!\n")
                for character in tekst7:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)
                myhero.punkty_zycia = myhero.punkty_zycia - enemy.punkty_ataku
                tekst8 = (f"Zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                for character in tekst8:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.5)
                GameOver(myhero, score)
        elif choice=="u":
            os.system('cls')
            tresc=f"Za późno na uciekanie. Z resztą, {enemy.imie} i tak Ci nie pozwoli.\n"
            for character in tresc:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)
        elif choice=='r':
            myhero.rozmawiajzBossem(Bohater)
        elif choice=='s':
            os.system('cls')
            print(f"{myhero.imie}: ")
            prosba = f'"Pradawna Mocy Światła, ja {myhero.imie} wzywam Cię do pomocy!"\n'
            for character in prosba:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.5)

            if myhero == Egzorcysta:
                specialChance = random.randint(0, 4)
                if specialChance == 0:
                    myhero.Charyzma(Egzorcysta)
                elif specialChance == 1:
                    myhero.SwietaTarcza(Egzorcysta)
                else:
                    tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                    for character in tekscik:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

            elif myhero == Swiety_Strzelec:
                specialChance = random.randint(0, 4)
                if specialChance == 0:
                    myhero.SuperDamage(Swiety_Strzelec)
                elif specialChance == 1:
                    myhero.SuperObrona(Swiety_Strzelec)
                else:
                    tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                    for character in tekscik:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

            elif myhero == Kaplanka_Swiatla:
                specialChance = random.randint(0, 4)
                if specialChance == 0:
                    myhero.Szczescie(Kaplanka_Swiatla)
                elif specialChance == 1:
                    myhero.RestartHP(Kaplanka_Swiatla)
                else:
                    tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                    for character in tekscik:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

            elif myhero == Dobry_Diabel:
                specialChance = random.randint(0, 4)
                if specialChance == 0:
                    myhero.NoMercy(Dobry_Diabel)
                elif specialChance == 1:
                    myhero.FunBegins(Dobry_Diabel)
                else:
                    tekscik = "Nie udało się wezwać Mocy Światła :(\n"
                    for character in tekscik:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.5)
                    myhero.punkty_zycia = myhero.punkty_zycia - (enemy.punkty_ataku / myhero.punkty_obrony)
                    tekst5 = (f"{str(enemy.imie)} trafia Cię, zostaje Ci {round(myhero.punkty_zycia)} zdrowia.\n")
                    for character in tekst5:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    time.sleep(0.5)

        else:
            os.system('cls')
            print("Wybrano nieprawidłową wartość.")

score=0
home()
