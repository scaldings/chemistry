import misc
import prompt
import database
import gui


def informacie_o_prvku(vlastnost):
    for x in database.information_to_list():
        if vlastnost in x:
            return x


def vzorec_do_listu(vzorec: str):
    temp_list, final_list, zvysok_molekuly = list(vzorec), [], ''
    if temp_list[0] in misc.cisla():
        final_list.append(temp_list[0])
        zvysok_molekuly = vzorec[1:]
    else:
        final_list.append('1')
        zvysok_molekuly = vzorec

    if zvysok_molekuly[len(zvysok_molekuly) - 1] not in misc.cisla():
        zvysok_molekuly += '-'

    for x in range(0, len(zvysok_molekuly) - 1):
        zvysok_molekuly_list = list(zvysok_molekuly)
        if zvysok_molekuly_list[x] in misc.velke_pismena():
            if zvysok_molekuly_list[x + 1] in misc.male_pismena():
                if zvysok_molekuly_list[x + 2] in misc.cisla():
                    to_append = zvysok_molekuly_list[x] + zvysok_molekuly_list[x + 1] + zvysok_molekuly_list[x + 2]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
                else:
                    to_append = zvysok_molekuly_list[x] + zvysok_molekuly_list[x + 1]
                    final_list.append(to_append)
                    zvysok_molekuly.replace(to_append, '')
            else:
                if zvysok_molekuly_list[x + 1] in misc.cisla():
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
            if x in misc.male_pismena():
                if x in misc.cisla():
                    pocet_atomov = int(x[2:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * float(informacie_o_prvku(x[:2])[4])
            else:
                if x in misc.cisla():
                    pocet_atomov = int(x[1:])
                else:
                    pocet_atomov = 1
                hmotnost += float(pocet_atomov) * float(informacie_o_prvku(x[:1])[4])
        i += 1
    return hmotnost * float(pocet_molekul)


def latkove_mnozstvo(hmotnost_vzorky: float, molarna_hmotnost: float):
    return hmotnost_vzorky / molarna_hmotnost


def latkove_mnozstvo2(celkovy_pocet_castic: float):
    return celkovy_pocet_castic / misc.avogadrova_konstanta()


def latkova_koncentracia(latkove_mnoz: float, objem: float):
    return latkove_mnoz / objem


if __name__ == '__main__':
    database.init_db()
    # prompt.main()
    gui.main()
