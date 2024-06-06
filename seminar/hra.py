import time
import random

# počáteční hodnoty
xp = 0
hp = 100
level = 1

# funkce
def zabití_nepřítele():
    global xp
    xp_za_zabití = random.randint(164, 821)
    xp += xp_za_zabití
    return xp_za_zabití

def zkontroluj_uroven():
    global level
    while xp >= level * 250:
        level += 1
        print(f"Výborně, dosáhl jsi nové úrovně {level} mezi špínou v Praze!")

def generuj_nepritele():
    nepritel = random.choice(["Feťák", "Zloděj", "Bezdomovec"])
    if nepritel == "Feťák":
        print("Potkal jsi Feťáka. Co uděláš?")
        print("1) Bojovat 2) Utéct")
        akce = input("Vyber možnost (1, 2): ").strip()
        if akce == "1":
            xp_za_zabití = zabití_nepřítele()
            print(f"Výborně! Získal jsi {xp_za_zabití} XP za zabití Feťáka.")
            print(f"Nyní máš celkem {xp} XP.")
            zkontroluj_uroven()
        elif akce == "2":
            print("Utekl jsi, ale Feťák tě možná najde později.")
        else:
            print("Neplatná volba, Feťák tě napadl a ztratil jsi 10 HP.")
            hp -= 10
            if hp <= 0:
                print("Bohužel, byl jsi poražen.")
                exit()
    elif nepritel == "Zloděj":
        print("Potkal jsi Zloděje. Co uděláš?")
        print("1) Bojovat 2) Pokusit se vyjednávat 3) Utéct")
        akce = input("Vyber možnost (1, 2, 3): ").strip()
        if akce == "1":
            xp_za_zabití = zabití_nepřítele()
            print(f"Výborně! Získal jsi {xp_za_zabití} XP za zabití Zloděje.")
            print(f"Nyní máš celkem {xp} XP.")
            zkontroluj_uroven()
        elif akce == "2":
            uspech = random.choice([True, False])
            if uspech:
                print("Vyjednal jsi se Zlodějem a získal jsi zpět své věci.")
                xp += 200
                print(f"Získal jsi 200 XP za úspěšné vyjednávání. Nyní máš {xp} XP.")
                zkontroluj_uroven()
            else:
                print("Vyjednávání selhalo, Zloděj tě okradl a ztratil jsi 20 HP.")
                hp -= 20
                if hp <= 0:
                    print("Bohužel, byl jsi poražen.")
                    exit()
        elif akce == "3":
            print("Utekl jsi, ale Zloděj tě možná najde později.")
        else:
            print("Neplatná volba, Zloděj tě okradl a ztratil jsi 20 HP.")
            hp -= 20
            if hp <= 0:
                print("Bohužel, byl jsi poražen.")
                exit()
    elif nepritel == "Bezdomovec":
        print("Potkal jsi Bezdomovce. Co uděláš?")
        print("1) Pomoci mu 2) Ignorovat ho 3) Utéct")
        akce = input("Vyber možnost (1, 2, 3): ").strip()
        if akce == "1":
            uspech = random.choice([True, False])
            if uspech:
                print("Pomohl jsi Bezdomovci a on ti dal kouzelný lektvar.")
                hp += 20
                xp += 300
                print(f"Získal jsi 300 XP a tvá aktuální životní síla je {hp} HP.")
                zkontroluj_uroven()
            else:
                print("Bezdomovec tě napadl a ztratil jsi 15 HP.")
                hp -= 15
                if hp <= 0:
                    print("Bohužel, byl jsi poražen.")
                    exit()
        elif akce == "2":
            print("Ignoroval jsi Bezdomovce a pokračoval dál.")
        elif akce == "3":
            print("Utekl jsi, ale Bezdomovec tě možná najde později.")
        else:
            print("Neplatná volba, Bezdomovec tě napadl a ztratil jsi 15 HP.")
            hp -= 15
            if hp <= 0:
                print("Bohužel, byl jsi poražen.")
                exit()

print("Vítej v The Power of Money")
time.sleep(2)

program = True
while program:
    odpoved1 = input("Jsi připravený na dobrodružství? Ano/Ne: ").strip().lower()
    if odpoved1 == "ano":
        print("Dobrá, pojďme na to!")
        break
    elif odpoved1 == "ne":
        print("Věděl jsem, že na to nemáš, losere.")
        program = False
        break
    else:
        print("Odpověz Ano/Ne, nebo si tě najdu!")

dotaznajmeno = True
while dotaznajmeno:
    otazkajmeno = "Jak se chcete jmenovat?"
    print(otazkajmeno)
    jmeno = input("Odpověď: ")
    if jmeno:
        time.sleep(1)
        print(f"Budiž, od teď jsi {jmeno}.")
        print(f"Vítej {jmeno} v Praze, v místě, kde budeš muset bojovat o každou korunu a hlavně o každý gram pika, který uvidíš.")
time.sleep(2)
print("V Praze je velmi zvláštní místo, kde budeš potkávat mnoho nebezpečných lidí, se kterými se budeš muset rvát.")
time.sleep(2)
print("Tvým cílem bude dosáhnout 5 úrovní, abys mohl opustit Prahu.")

time.sleep(3)

print("Ale ne, napadl tě feťák. Co uděláš?")
print("1) Dáš mu chce 2) Budeš bojovat 3) Pokusíš se utéct")
time.sleep(2)

fetak = True
while fetak:
    akce = input("Vyber možnost (1, 2, 3): ").strip()
    if akce == "1":
        print("Udělal jsi chybu, feťák o tobě bude vědět, že jsi slabá močka, a bude tě ponižovat vždy, když tě uvidí.")
        program = False
        break
    elif akce == "2":
        xp_za_zabití = zabití_nepřítele()
        print(f"Výborně! Správně jsi odhadl, že feťák je slabý, a proto jsi věděl, že ho dokážeš porazit.")
        time.sleep(2)
        print(f"A získal jsi {xp_za_zabití} XP za zabití.")
        print(f"Nyní máš celkem {xp} XP.")
        zkontroluj_uroven()
        time.sleep(3)
        break
    elif akce == "3":
        print("Ale né! Feťák na tebe zavolal své kámoše a společně tě dohnali. Skončil jsi.")
        program = False
        break
    else:
        print("Neplatná volba, zkus to znovu.")

generuj_nepritele()  

print("Ty máš ale štěstí na trable. Právě za tebou míří král bezdomovců. Měl bys se rozhodnout, co budeš dělat.")
time.sleep(2)
print("1) Budeš si s ním povídat 2) Budeš bojovat 3) Pokusíš se utéct ")
time.sleep(2)

kral_bezdaku = True
while kral_bezdaku:
    akce = input("Vyber možnost (1, 2, 3): ").strip()

    if akce == "1":
        print("Tybrďo, jak jsi věděl, že ti neublíží a že chce jen pomoct?")
        print("Král bezdomovců můžeš pomoci najít jeho ztraceného psa, který mu byl ukradený.")
        time.sleep(2)
        print("Chceš mu pomoci najít jeho ztraceného psa? Ano/Ne")

        pomoc_krali = input("Odpověz (Ano/Ne): ").strip().lower()
        if pomoc_krali == "ano":
            print("Výborně! Král je šťastný a sdělil ti, že ti dá kouzelný nápoj, pokud uspěješ!")
            print("Najít psa bezdomovce bude velmi těžké. Doufám, že svých rozhodnutí nelituješ. Není cesty zpět!")
            print("Najít psa bude trvat 70 sekund.")
            for i in range(70, -1, -1):
                print(i)
                time.sleep(1)
            print("Našel jsi psa!")
            time.sleep(2)
            print("Vrátil jsi se ke králi, který ti, jak slíbil, dal lektvar.")
            hp += 20
            print(f"Tvá aktuální životní síla je {hp} HP.")
            xp += 1600 
            print(f"Za získání lektvaru jsi získal 1600 XP. Celkem máš nyní {xp} XP.")
            time.sleep(2)
            break
        elif pomoc_krali == "ne":
            print("Král se rozhodl, že na tebe pošle svoje poskoky.")
            program = False
            break
    elif akce == "2":
        print("Sis myslel, že porazíš krále? Jsi hodně naivní a asi už bereš až moc toho pika.")
        program = False
        break
    elif akce == "3":
        print("Dobrá volba, utekl jsi, jelikož král měl berle.")
        break
    else:
        print("Vyber si z toho, co máš")

generuj_nepritele()  

print("Skvěle jsi si poradil s králem. To ti musím uznat. Mimochodem, za každý splněný úkol dostáváš XP a šance na HP, abys proazil silnější protivníky. Tak bojuj dál.")
time.sleep(3)
print("Ale ne, našel tě feťák, kterého si zmlátil, a má posily.")
time.sleep(2)
print("Co budeš dělat?")
time.sleep(2)
print("1) Pokusíš se s ním vyjednávat 2) Budeš utíkat 3) Půjdeš 1v20 jako šel Humi ")

fetak2 = True
while fetak2:
    akce = input("Vyber možnost (1, 2, 3): ").strip()

    if akce == "1":
        print("Js jsi se zbláznil? Vymlátili z tebe duši!")
        program = False
        break
    if akce == "2":
        print("Během tvého běhu tě viděl král bezdomovců a rozhodl se ti jít na pomoc se svými chlapy")
        time.sleep(4)
        print("Po dlouhém boji jste vyhráli a feťák se rozbrečel a utekl pryč jeho posily skončili v bezvědomí.")
        time.sleep(2)

        for _ in range(5):
            nahodne_xp = random.randint(164, 827)
            xp += nahodne_xp
            print(f"Získal jsi {nahodne_xp} XP. Celkem máš nyní {xp} XP.")
            zkontroluj_uroven()  
            if level == 5:
                print("Pánové! Dosáhl jsi správné úrovně, abys mohl opustit Prahu.")
                time.sleep(3)
                print("Opustil jsi Prahu a vyhrál jsi hru.")
                break
            elif level < 5:
                print("Selhal jsi, zkuz to znovu.")
                fetak2 = False
                break
    elif akce == "3":
        print("Utekl jsi, ale feťák a jeho posily tě možná najdou později.")
        break
    else:
        print("Vyber si z možností 1, 2 nebo 3.")
