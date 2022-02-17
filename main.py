from os import system; from time import sleep; from defs import *
saída = 'n'
while saída not in 'Ss':
    system('cls')
    print(f'Bem Vindo ao programa de Química')
    print('''- Informações sobre o programa:
1º Vamos receber a quantidade de elétrons que o átomo, ou íon, possui ou o nome do elemento químico;
2º Vamos retornar as informações possíveis sobre esse átomo/íon;
3º O número quântico spin será considerado "-1/2" quando a seta estiver para cima (↑),
   e "1/2" quando a seta estiver para baixo (↓).\n''')
    # Receber a informação crucial sobre o átomo/íon
    info = str(input('Dê alguma informação sobre o átomo/íon [nome ou quantidade de elétrons]: ')).strip().capitalize()
    # primeira validação de informação
    if info.isnumeric() or info.isalpha():
        pass
    else:
        print('\nERRO: digite uma informação válida!')
        sleep(2)
        continue
    # Processo através da quantidade de elétrons
    if info.isnumeric():
        elé = int(info)
        # Segunda validação de informação
        if elé > 118:
            print('\nERRO: digite uma quantidade de elétrons válida!')
            sleep(2)
            continue
        ion = autenticar_sn('Esse átomo é um íon? ')
        if ion in 'Ss':
            elé = convert(elé)
        # Descobrir o elemento químico
        elemento = elemqui(elé)
        # Descobrir o grupo, a família e o nome específico do elemento
        group, family, name = familia(elemento)
    # Processo através do nome do elemento químico
    elif info.isalpha():
        erro = False
        cont = 0
        arq = open('elementos.txt', 'r', encoding='utf-8')
        linhas = arq.readlines()
        for l in linhas:
            cont += 1
            if info in l:
                elemento = l
                break
            elif cont == 118:
                erro = True
                break
        arq.close()
        if erro:
            print('ERRO: digite um elemento válido! [NÃO se esqueça de assentos, caso o elemento possua]')
            sleep(3)
            continue
        # Descobrir o grupo, a família e o nome específico do elemento
        group, family, name = familia(elemento)
        elé = cont
    # Descobrir a camada de valência
    sub, full = subnivel(elé)
    # Fazer a distribuição eletrônica
    deletronica = distribuição(full)
    # Criar lista de número quântico secundário
    qsec = ['s', 'p', 'd', 'f']
    # Obter o número quântico magnético e spin
    ml, ms = magnético(sub)
    # Exibir as informações coletadas
    print('\nRecebendo informações...\n')
    sleep(1)
    print(f'Quantidade de elétrons: \t{elé}')
    print(f'Elemento químico: \t\t{elemento}')
    print(f'Grupo do elemento: \t\t{group}')
    print(f'Família do elemento: \t\t{family}')
    print(f'Nome específico da família: \t{name}')
    print(f'Subnível mais energético: \t{sub}')
    print(f'Número quântico principal (n): \t{sub[0]}')
    print(f'Número quântico secundário (l): {qsec.index(sub[1])}')
    print(f'Número quântico magnético (ml): {ml}')
    print(f'Número quântico spin (ms): \t{ms}')
    print('Distribuição Eletrônica: \t', end='')
    for c in deletronica:
        print(f'{c} ', end='')
    print(f'{sub}\n')
    saída = autenticar_sn('Deseja finalizar o programa? ')
