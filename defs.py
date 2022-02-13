def autenticar_sn(txt):
    r = str(input(txt)).strip()[0]
    while r not in 'SsNn':
        print(f'Erro: digite somente sim ou não.')
        r = str(input(txt)).strip()[0]
    return r


def nint(txt):
    while True:
        try:
            x = str(input(f'{txt}'))
            x = int(x)
            if 0 < x < 119:
                pass
            else:
                t = int(str(''))
        except:
            print(f'Erro: digite um número inteiro válido!')
        else:
            break
    return x


def convert(num):
    cation = autenticar_sn('Esse elemento é um cátion? Ou seja, ele perdeu elétrons, se tornando um elemento carregado positivamente? ')
    if cation in 'Ss':
        n = nint('Quantos elétrons o elemento perdeu? ')
        n = num + n
    else:
        n = nint('Então quantos elétrons o elemento recebeu? ')
        n = num - n
    return n


def elemqui(ele):
    lista_elementos = ['Hidrogênio - H', 'Hélio - He', 'Lítio - Li', 'Berílio - Be', 'Boro - B', 'Carbono - C',
    'Nitrogênio - N', 'Oxigênio - O', 'Flúor - F', 'Neônio - Ne', 'Sódio - Na', 'Magnésio - Mg', 'Alumínio - Al',
    'Silício - Si', 'Fósforo - P', 'Enxofre - S', 'Cloro - Cl', 'Argônio - Ar', 'Potássio - K', 'Cálcio - Ca',
    'Escândio - Sc', 'Titânio - Ti', 'Vanádio - V', 'Cromo - Cr', 'Manganês - Mn', 'Ferro - Fe', 'Cobalto - Co',
    'Níquel - Ni', 'Cobre - Cu', 'Zinco - Zn', 'Gálio - Ga', 'Germânio - Ge', 'Arsênio - As', 'Selênio - Se',
    'Bromo - Br', 'Criptônio - Kr', 'Rubídio - Rb', 'Estrôncio - Sr', 'Ítrio - Y', 'Zircônio - Zr', 'Nióbio - Nb',
    'Molibdênio - Mo', 'Tecnécio - Tc', 'Rutênio - Ru', 'Ródio - Rh', 'Paládio - Pd', 'Prata - Ag', 'Cádmio - Cd'
    'Índio - In', 'Estanho - Sn', 'Antimônio - Sb', 'Telúrio - Te', 'Iodo - I', 'Xenônio - Xe', 'Césio - Cs',
    'Bário - Ba', 'Lantânio - La', 'Cério - Ce', 'Praseodímio - Pr', 'Neodímio - Nd', 'Promécio - Pm',
    'Samário - Sm', 'Európio - Eu', 'Gadolínio - Gd', 'Térbio - Tb', 'Disprósio - Dy', 'Hôlmio - Ho', 'Érbio - Er'
    'Túlio - Tm', 'Itérbio - Yb', 'Lutécio - Lu', 'Háfnio - Hf', 'Tântalo - Ta', 'Tungstênio - W', 'Rênio - Re',
    'Ósmio - Os', 'Irídio - Ir', 'Platina - Pt', 'Ouro - Au', 'Mercúrio - Hg', 'Tálio - Tl', 'Chumbo - Pb',
    'Bismuto - Bi', 'Polômio - Po', 'Astato - At', 'Radônio - Rn', 'Frâncio - Fr', 'Rádio - Ra', 'Actínio - Ac',
    'Tório - Th', 'Protactínio - Pa', 'Urânio - U', 'Neptúnio - Np', 'Plutônio - Pu', 'Amerício - Am', 'Cúrio - Cm',
    'Berquélio - Bk', 'Califórnio - Cf', 'Einstênio - Es', 'Férmio - Fm', 'Mendelévio - Md', 'Nobélio - No',
    'Laurêncio - Lr', 'Rutherfórdio - Rf', 'Dúbnio - Db', 'Seabórgio - Sg', 'Bóhrio - Bh', 'Hássio - Hs',
    'Meitnério - Mt', 'Darmstádtio - Ds', 'Roentgênio - Rg', 'Copernício - Cn', 'Nihônio - Nh', 'Fleróvio - Fl',
    'Moscóvio - Mc', 'Livermório - Lv', 'Tenesso - Ts', 'Oganessônio - Og']
    elem = lista_elementos[ele-1]
    return elem


def subnivel(n):
    if n <= 2:
        subn = f'1s{n}'
        completo = '1s2'
    elif n <= 4:
        subn = f'2s{n - 2}'
        completo = '2s2'
    elif n <= 10:
        subn = f'2p{n - 4}'
        completo = '2p6'
    elif n <= 12:
        subn = f'3s{n - 10}'
        completo = '3s2'
    elif n <= 18:
        subn = f'3p{n - 12}'
        completo = '3p6'
    elif n <= 20:
        subn = f'4s{n - 18}'
        completo = '4s2'
    elif n <= 30:
        subn = f'3d{n - 20}'
        completo = '3d10'
    elif n <= 36:
        subn = f'4p{n - 30}'
        completo = '4p6'
    elif n <= 38:
        subn = f'5s{n - 36}'
        completo = '5s2'
    elif n <= 48:
        subn = f'4d{n - 38}'
        completo = '4d10'
    elif n <= 54:
        subn = f'5p{n - 48}'
        completo = '5p6'
    elif n <= 56:
        subn = f'6s{n - 54}'
        completo = '6s2'
    elif n <= 70:
        subn = f'4f{n - 56}'
        completo = '4f14'
    elif n <= 80:
        subn = f'5d{n - 70}'
        completo = '5d10'
    elif n <= 86:
        subn = f'6p{n - 80}'
        completo = '6p6'
    elif n <= 88:
        subn = f'7s{n - 86}'
        completo = '7s2'
    elif n <= 102:
        subn = f'5f{n - 88}'
        completo = '5f14'
    elif n <= 112:
        subn = f'6d{n - 102}'
        completo = '6d10'
    elif n <= 118:
        subn = f'7p{n - 112}'
        completo = '7p6'
    return subn, completo


def distribuição(sub):
    dist_list = ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2',
    '4f14', '5d10', '6p6', '7s2', '5f14', '6d10', '7p6']
    pos = dist_list.index(sub)
    ordem = dist_list[0:pos]

    return ordem


def magnético(sub):
    isub = int(sub[2:])
    if sub[1] == 's':
        ml = 0
        if isub == 2:
            spin = '1/2 ↓'
        else:
            spin = '-1/2 ↑'
    elif sub[1] == 'p':
        p = [1, 2, 3]
        try:
            ml = p.index(isub) - 1
        except:
            ml = p.index(isub - 3) - 1
            spin = '1/2 ↓'
        else:
            spin = '-1/2 ↑'
    elif sub[1] == 'd':
        d = [1, 2, 3, 4, 5]
        try:
            ml = d.index(isub) - 2
        except:
            ml = d.index(isub - 5) - 2
            spin = '1/2 ↓'
        else:
            spin = '-1/2 ↑'
    elif sub[1] == 'f':
        f = [1, 2, 3, 4, 5, 6, 7]
        try:
            ml = f.index(isub) - 3
        except:
            ml = f.index(isub - 7) - 3
            spin = '1/2 ↓'
        else:
            spin = '-1/2 ↑' 
    return ml, spin
