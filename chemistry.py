import string


def avogadrova_konstanta():
    return 6.022 * pow(10, 23)


def cisla():
    return '0123456789'


def male_pismena():
    return string.ascii_lowercase


def velke_pismena():
    return string.ascii_uppercase


def zaokruhelnie(cislo: float, miesta: int):
    cislo_string = str(cislo)
    desatinne_miesta = cislo_string.split('.')[1]
    cislo_zaokruhlene = f'{cislo_string.split(".")[0]}.{desatinne_miesta[:miesta]}'
    return cislo_zaokruhlene


def informacie_o_prvku(prvok: str):
    file = open('prvky.txt', 'r', encoding='utf-8')
    prvky = file.read().split('\n')
    for x in prvky:
        if str(prvok + ':') in x:
            return x
    return None


def vzorec_do_listu(vzorec: str):
    temp_list, final_list, zvysok_molekuly = list(vzorec), [], ''
    if temp_list[0] in cisla():
        final_list.append(temp_list[0])
        zvysok_molekuly = vzorec[1:]
    else:
        final_list.append('1')
        zvysok_molekuly = vzorec

    for x in range(0, len(zvysok_molekuly) - 1):
        zvysok_molekuly_list = list(zvysok_molekuly)
        if zvysok_molekuly_list[x] in velke_pismena():
            if zvysok_molekuly_list[x + 1] in male_pismena():
                if zvysok_molekuly_list[x + 2] in cisla():
                    to_append = zvysok_molekuly_list[x] + zvysok_molekuly_list[x + 1] + zvysok_molekuly_list[x + 2]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
                else:
                    to_append = zvysok_molekuly_list[x] + zvysok_molekuly_list[x + 1]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
            else:
                if zvysok_molekuly_list[x + 1] in cisla():
                    to_append = zvysok_molekuly_list[x] + zvysok_molekuly_list[x + 1]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
                else:
                    to_append = zvysok_molekuly_list[x]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
    return final_list


def hmotnost_molekuly(molekula: list):
    pocet_molekul = molekula[0]
    hmotnost, i = 0, 0
    for x in molekula:
        if i != 0:
            if x in male_pismena():
                if x in cisla():
                    pocet_atomov = int(x[2:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * float(informacie_o_prvku(x[:2]).split(':')[4])
            else:
                if x in cisla():
                    pocet_atomov = int(x[1:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * float(informacie_o_prvku(x[:1]).split(':')[4])
        i += 1
    return hmotnost * float(pocet_molekul)


def latkove_mnozstvo(hmotnost_vzorky: float, molarna_hmotnost: float):
    return hmotnost_vzorky / molarna_hmotnost


def latkove_mnozstvo2(celkovy_pocet_castic: float):
    return celkovy_pocet_castic / avogadrova_konstanta()


def latkova_koncentracia(latkove_mnoz: float, objem: float):
    return latkove_mnoz / objem


def main():
    vzorec = str(input('Zadaj vzorec zlúčeniny: '))
    print(zaokruhelnie(hmotnost_molekuly(vzorec_do_listu(vzorec)), 2))
    main()


if __name__ == '__main__':
    main()
