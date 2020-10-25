import string


def atomova_hmotnost_prvku(prvok: str):
    file = open('prvky.txt', 'r')
    prvky, hmotnost = file.read().split('\n'), 0
    for x in prvky:
        if str(prvok + ':') in x:
            hmotnost = float(x.split(':')[1])
    return hmotnost


def cisla():
    return '0123456789'


def male_pismena():
    return string.ascii_lowercase


def velke_pismena():
    return string.ascii_uppercase


def vzorec_do_listu(vzorec: str):
    temp_list, final_list, zvysok_zluceniny = list(vzorec), [], ''
    if temp_list[0] in cisla():
        final_list.append(temp_list[0])
        zvysok_zluceniny = vzorec[1:]
    else:
        final_list.append('1')
        zvysok_zluceniny = vzorec

    for x in range(0, len(zvysok_zluceniny) - 1):
        zvysok_zluceniny_list = list(zvysok_zluceniny)
        if zvysok_zluceniny_list[x] in velke_pismena():
            if zvysok_zluceniny_list[x + 1] in male_pismena():
                if zvysok_zluceniny_list[x + 2] in cisla():
                    to_append = zvysok_zluceniny_list[x] + zvysok_zluceniny_list[x + 1] + zvysok_zluceniny_list[x + 2]
                    final_list.append(to_append)
                    zvysok_zluceniny.replace(to_append, '')
                else:
                    to_append = zvysok_zluceniny_list[x] + zvysok_zluceniny_list[x + 1]
                    final_list.append(to_append)
                    zvysok_zluceniny.replace(to_append, '')
            else:
                if zvysok_zluceniny_list[x + 1] in cisla():
                    to_append = zvysok_zluceniny_list[x] + zvysok_zluceniny_list[x + 1]
                    final_list.append(to_append)
                    zvysok_zluceniny.replace(to_append, '')
                else:
                    to_append = zvysok_zluceniny_list[x]
                    final_list.append(to_append)
                    zvysok_zluceniny.replace(to_append, '')
    return final_list


def hmotnost_zluceniny(zlucenina: list):
    pocet_zlucenin = zlucenina[0]
    hmotnost, i = 0, 0
    for x in zlucenina:
        if i != 0:
            if x in male_pismena():
                if x in cisla():
                    pocet_atomov = int(x[2:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * atomova_hmotnost_prvku(x[:2])
            else:
                if x in cisla():
                    pocet_atomov = int(x[1:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * atomova_hmotnost_prvku(x[:1])
        i += 1
    return hmotnost * float(pocet_zlucenin)


def zaokruhelnie(cislo: float, miesta: int):
    cislo_string = str(cislo)
    desatinne_miesta = cislo_string.split('.')[1]
    cislo_zaokruhlene = f'{cislo_string.split(".")[0]}.{desatinne_miesta[:miesta]}'
    return cislo_zaokruhlene


def main():
    vzorec = str(input('Zadaj vzorec zlúčeniny: '))
    print(zaokruhelnie(hmotnost_zluceniny(vzorec_do_listu(vzorec)), 2))
    main()

if __name__ == '__main__':
    main()
