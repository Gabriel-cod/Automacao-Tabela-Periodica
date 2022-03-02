def autenticar_sn(txt):
    r = str(input(txt)).strip()[0]
    while r not in 'SsNn':
        print(f'Erro: digite somente sim ou não.')
        r = str(input(txt)).strip()[0]
    return r


def nint(txt):
    while True:
        x = str(input(f'{txt}'))
        if x.isnumeric():
            x = int(x)
            if 0 < x < 119:
                ok = True
            else:
                ok = False
        else:
            ok = False
            print(f'Erro: digite um número inteiro válido!')
        if ok:
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
    elem = ''
    cont = 0
    arq = open('elementos.txt', 'r', encoding='utf-8')
    linhas = arq.readlines()
    for l in linhas:
        el = l.replace('\n', '')
        cont += 1
        if cont == ele:
            elem = el
            break
    arq.close()     
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


def familiaA(e):
    cont = 0
    nome_e = fam = gp = ''
    f = open('famíliasA.txt', 'r', encoding='utf-8')
    lin = f.readlines()
    e = e.split(' ')
    for l in lin:
        itens = l.split(' ')
        cont += 1
        for i in itens:
            simbolo = i.replace('\n', '')
            if e[2] == simbolo:
                fam = f'{cont}A'
                if cont == 1:
                    gp = '1'
                    nome_e = 'Metais alcalinos'
                elif cont == 2:
                    gp = '2'
                    nome_e = 'Metais alcalinos-terrosos'
                elif cont == 3:
                    gp = '13'
                    nome_e = 'Família do Boro'
                elif cont == 4:
                    gp = '14'
                    nome_e = 'Família do Carbono'
                elif cont == 5:
                    gp = '15'
                    nome_e = 'Família do Nitrogênio'
                elif cont == 6:
                    gp = '16'
                    nome_e = 'Calcogênios'
                elif cont == 7:
                    gp = '17'
                    nome_e = 'Halogênios'
                elif cont == 8:
                    gp = '18'
                    nome_e = 'Gases Nobres'
            elif e[2] in 'H':
                fam = 'O Hidrogênio não possui uma família definida, apesar de alguns autores o enquadrarem na família 1A'
                gp = 'Alguns autores enquadram o Hidrogênio no grupo 1, outros dizem que ele não possui grupo'
                nome_e = '--'
    if fam == '8A':
        fam = '0'
    f.close()
    return gp, fam, nome_e


def familiaB(e):
    cont = 0
    nome_e = fam = gp = ''
    f = open('famíliasB.txt', 'r', encoding='utf-8')
    lin = f.readlines()
    e = e.split(' ')
    for l in lin:
        itens = l.split(' ')
        cont += 1
        for i in itens:
            simbolo = i.replace('\n', '')
            if e[2] == simbolo:
                if cont == 1:
                    gp = '3'
                    fam = '3B'
                    nome_e = 'Não encontrado :/'
                elif cont == 2:
                    gp = '4'
                    fam = '4B'
                    nome_e = 'Grupo do Titânio'
                elif cont == 3:
                    gp = '5'
                    fam = '5B'
                    nome_e = 'Grupo do Vanádio'
                elif cont == 4:
                    gp = '6'
                    fam = '6B'
                    nome_e = 'Grupo do Crômio'
                elif cont == 5:
                    gp = '7'
                    fam = '7B'
                    nome_e = 'Grupo do Manganês'
                elif cont in range(6, 9):
                    fam = '8B'
                    nome_e = 'Não encontrado :/'
                    if cont == 6:
                        gp = '8'
                    elif cont == 7:
                        gp = '9'
                    elif cont == 8:
                        gp = '10'
                elif cont == 9:
                    gp = '11'
                    fam = '1B'
                    nome_e = 'Grupo do Cobre'
                elif cont == 10:
                    gp = '12'
                    fam = '2B'
                    nome_e = 'Grupo do Zinco'
    f.close()
    return gp, fam, nome_e
