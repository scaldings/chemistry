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
