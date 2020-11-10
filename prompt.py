import chemistry as ch
import misc


def main():
    print('1. Vlastnosti prvku')
    print('2. Vlastnosti zlúčeniny')
    print('3. Koniec')
    vyber = int(input('Vyber si funkciu: '))

    if vyber == 1:
        vlastnosti_prvku()
    elif vyber == 2:
        vlastnosti_zluceniny()
    elif vyber == 3:
        exit()
    else:
        print('Neplatná funkcia!')
    main()


def vlastnosti_zluceniny():
    vzorec = str(input('Zadaj vzorec zlúčeniny: '))
    hmotnost_vzorky, celkovy_pocet_castic, objem_roztoku = 0, 0, 0

    pozna_objem_roztoku = input('Poznáš objem látky / roztoku? (A/N) ')
    pozna_hmotnost_vzorky = input('Poznáš hmotnosť vzorky? (A/N) ')
    pozna_celkovy_pocet_castic = input('Poznáš celkový počet častíc? (A/N) ')

    if pozna_hmotnost_vzorky == 'A':
        hmotnost_vzorky = float(input('Zadaj hmotnosť vzorky: '))

        if pozna_celkovy_pocet_castic == 'A':
            celkovy_pocet_castic = float(input('Zadaj celkový počet častíc: '))

            if pozna_objem_roztoku == 'A':
                objem_roztoku = float(input('Zadaj objem látky / roztoku: '))
            elif pozna_objem_roztoku == 'N':
                pass
            else:
                print('Neplatný príkaz!')
                main()

        elif pozna_celkovy_pocet_castic == 'N':

            if pozna_objem_roztoku == 'A':
                objem_roztoku = float(input('Zadaj objem látky / roztoku: '))
            elif pozna_objem_roztoku == 'N':
                pass
            else:
                print('Neplatný príkaz!')
                main()

            pass
        else:
            print('Neplatný príkaz!')
            main()

    elif pozna_hmotnost_vzorky == 'N':

        if pozna_celkovy_pocet_castic == 'A':
            celkovy_pocet_castic = float(input('Zadaj celkový počet častíc: '))

            if pozna_objem_roztoku == 'A':
                objem_roztoku = float(input('Zadaj objem látky / roztoku: '))
            elif pozna_objem_roztoku == 'N':
                pass
            else:
                print('Neplatný príkaz!')
                main()

        elif pozna_celkovy_pocet_castic == 'N':

            if pozna_objem_roztoku == 'A':
                objem_roztoku = float(input('Zadaj objem látky / roztoku: '))
            elif pozna_objem_roztoku == 'N':
                print(f'\nM({vzorec}) = {misc.zaokruhelnie(ch.hmotnost_molekuly(ch.vzorec_do_listu(vzorec)), 2)}')
                print('Nedá sa poskytnúť viac informácií.\n')
                main()
            else:
                print('Neplatný príkaz!')
                main()
        else:
            print('Neplatný príkaz!')
            main()

    else:
        print('Neplatný príkaz!')
        main()

    print(f'\nM({vzorec}) = {misc.zaokruhelnie(ch.hmotnost_molekuly(ch.vzorec_do_listu(vzorec)), 2)}')
    if hmotnost_vzorky != 0:
        print(f'm({vzorec}) = {hmotnost_vzorky}')
        if celkovy_pocet_castic == 0:
            latkove_mnozstvo = ch.latkove_mnozstvo(hmotnost_vzorky, ch.hmotnost_molekuly(ch.vzorec_do_listu(vzorec)))
            zaokruhlene_latkove_mnozstvo = float(misc.zaokruhelnie(latkove_mnozstvo, 3))
            print(f'n({vzorec}) = {zaokruhlene_latkove_mnozstvo}')
            if objem_roztoku != 0:
                koncentracia = ch.latkova_koncentracia(zaokruhlene_latkove_mnozstvo, objem_roztoku)
                zaokruhlena_koncentracia = float(misc.zaokruhelnie(koncentracia, 3))
                print(f'c({vzorec}) = {zaokruhlena_koncentracia}')
    if celkovy_pocet_castic != 0:
        print(f'N({vzorec}) = {celkovy_pocet_castic}')
        if hmotnost_vzorky == 0:
            latkove_mnozstvo = ch.latkove_mnozstvo2(celkovy_pocet_castic)
            zaokruhlene_latkove_mnozstvo = float(misc.zaokruhelnie(latkove_mnozstvo, 3))
            print(f'n({vzorec}) = {zaokruhlene_latkove_mnozstvo}')
            if objem_roztoku != 0:
                koncentracia = ch.latkova_koncentracia(zaokruhlene_latkove_mnozstvo, objem_roztoku)
                zaokruhlena_koncentracia = float(misc.zaokruhelnie(koncentracia, 3))
                print(f'c({vzorec}) = {zaokruhlena_koncentracia}')


def vlastnosti_prvku():
    print('Vlastnosti prvku sú: Latinský alebo slovenský názov, značka, protónové číslo alebo atómová hmotnosť.')
    vlastnost, informacie = input('Zadaj vlastnosť prvku: '), []
    if misc.cisla() in vlastnost:
        if '.' in vlastnost:
            vlastnost = float(vlastnost)
        else:
            vlastnost = int(vlastnost)

    if ch.informacie_o_prvku(vlastnost) is not None:
        informacie = ch.informacie_o_prvku(vlastnost)
        informacie = ch.informacie_o_prvku(vlastnost)
    elif ch.informacie_o_prvku(vlastnost) is None:
        print('Neplatny prvok!\n')
        main()

    
