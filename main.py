from os import system; from time import sleep; from defs import *
saída = 'n'
while saída not in 'Ss':
    sleep(1.5)
    system('cls')
    print(f'Bem Vindo ao programa de Química')
    print('''- Informações sobre o programa:
1º Vamos receber a quantidade de elétrons que o átomo possui;
2º Vamos retornar as informações possíveis sobre esse átomo;
3º O número quântico spin será considerado "-1/2" quando a seta estiver para cima (↑),
   e "1/2" quando a seta estiver para baixo (↓).\n''')
    sleep(2)
# Receber a informação de quantos elétrons o átomo possui
    elé = nint('Informe a quantidade de elétrons do átomo [somente números inteiros]: ')
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
    print(f'Subnível mais energético: \t{sub}')
    print(f'Número quântico principal (n): \t{sub[0]}')
    print(f'Número quântico secundário (l): {qsec.index(sub[1])}')
    print(f'Número quântico magnético (ml): {ml}')
    print(f'Número quântico spin (ms): \t{ms}')
    print('Distribuição Eletrônica: \t', end='')
    for c in deletronica:
        print(f'{c} ', end='')
    print(f'{sub}\n')

    saída = autenticar_saida()
