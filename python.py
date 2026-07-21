

#------------------------------------------

# Autora: Maria Maura S. do Reis

# Data: 05/12/2022

# Python 3.10.5  64-bit 

#------------------------------------------

#FUNC PARA VALIDAR OS INT'S

def n_int(n):

    while True:

        try:

            x = int(n)

            return x

        except:

            print("ERRO! Por favor informe apenas numero")

            return n_int(input())

benvindo='\033[1;30;40mSELEÇAO DE CANDIDATO\033[m' # cor vermelha 

print("\033[31m*\033[m" * len(benvindo))

print(benvindo)

print("\033[31m*\033[m" * len(benvindo))

#DEFINIÇAO DAS VARIAVEIS 

candidato = dict()

galera = list()

eng = list()

ban = list()

a_proj = list()

some_p = 0          # ACUMULADOR DA PONTUAÇAO

start = 'S'  # BREAK DO WHILE PRINCIPAL

# PARTE 1

# PROGRAMA PRINCIPAL 

while start == 'S':             

    candidato.clear()    # LIMPA DICT ANTES DE UM NOVO CADRASTRO

    # INFORMAÇOES BASICAS

    while True:

        candidato['nome'] = str(input('\ninforme seu nome '))

        if candidato['nome'].isalpha():                         #USANDO ISALPHA PARA VALIDAÇAO DAS STR

            break

        else:

            print("ERRO! por favor informe seu nome")

    while True:

        candidato['idade'] = n_int(input('\ninforme sua idade '))

        if candidato['idade'] <= 17 or candidato['idade'] >=100:

            print('Por favor! Informe a sua idade correta')

        else:

            break

    while True:             # ADD AS AREAS  PRETENDIDAS  EM DIFERENTES LISTAS

        candidato['area_pretendida'] = str(input('\narea pretendida: [Engenharia de Software/Bancos de Dados/ Analise e Projeto de Algoritmos ] ')) .upper()[0]

        if candidato['area_pretendida'] in 'e/Engenharia e Software':

            eng.append('Engenharia de Software')

        if candidato['area_pretendida'] in 'b/Banco de Dados':

            ban.append('Banco de Dados')

        if candidato['area_pretendida'] in 'a/Analise e Projeto de Algoritmos':

            a_proj.append('Analise e Projeto de Algoritmos')

        if candidato['area_pretendida'] in 'e/Engenharia de Software/ b/Bancos de Dados/ a/Analise e Projeto de Algoritmos':

            break

        else:

            print('\nERRO! Por favor, digite apenas Engenharia de Software, Bancos de Dados ou Analise e Projeto de Algoritmos ')

# PARTE 2

    while True:

        perg = str(input('\nvoce ja fez algum curso?[S/N]\n '))

        if perg.isalpha():

            if perg in 'Ss/Nn':

                break

        else:

            print('\nERRO! Por favor, digite apenas [S/N] ')

    if perg in 'Ss':

        perg_1 = n_int(input('\nquantos? '))

        for some in range(perg_1): 

            ch = n_int(input('\ninforme a carga horaria: ')) #  CH ABREV DE CARGA HORARIA

            if ch <= 10:

                some_p += 1                      #  1 PONTO

            elif ch >= 11 and ch <= 40:

                some_p += 2                     # 2 PTS

            else:

                some_p += 3                          # 3 PTS 

# PARTE 3

    while True:

        aa = str(input('\nvoce ja fez algum outro curso afins?[S/N]\n '))

        if aa.isalpha():

            if aa in 'Ss/Nn':

                break

        print('\nERRO! Por favor, digite apenas [S/N] ')

    if aa in 'Ss':

        qts_aa = n_int(input('\nquantos? '))

        pts_aa = qts_aa * 2             # 2 PTS POR CURSOS AFINS

        some_p += pts_aa

    while True:

        ling_est = str(input('\nvoce ja fez algum curso de lingua estrangeira?[S/N]\n '))

        if ling_est.isalpha():

            if ling_est in 'Ss/Nn':

                break

        print('\nERRO! Por favor, digite apenas [S/N] ')

    if ling_est in 'Ss':

        qts_ling_est = n_int(input('\nquantos? '))

        pts_ling = qts_ling_est * 2             # 2 PTS POR CURSOS LING. ESTRANGEIRA

        some_p += pts_ling

# PARTE 4

    while True:                 # ACUMULARA 1 PONTO POR RESP == SIM

        exper = str(input('\nvoce pesquisa ou trabalha na área pretendida há mais de 3 anos?[S/N]\n '))

        if exper.isalpha():

            if exper in 'Ss/Nn':

                break

        print('\nERRO! Por favor, digite apenas [S/N] ')

        if exper in 'Ss':

            some_p += 1

    while True:

        certf = str(input('\nvoce possui certificações nacionais ou internacionais?[S/N]\n '))

        if certf.isalpha():

            if certf in 'Ss/Nn':

                break

        print('\nERRO! Por favor, digite apenas [S/N] ')

        if certf in 'Ss':

            some_p += 1

    while True:

        desenv = str(input('\nvoce já participou de alguma equipe de desenvolvimento de software para o governo?[S/N]\n '))

        if desenv.isalpha():

            if desenv in 'Ss/Nn':

                break

        print('\nERRO! Por favor, digite apenas [S/N] ')

        if desenv in 'Ss':

            some_p += 1    

    start = str(input('quer continuar? [S/N]\n ')).upper() [0] # BREAK PARA O WHILE PRINCINPAL        

    candidato['pontuaçao'] = some_p         # ADD ACUMULADOR NO DICT DE PONTUAÇAO

    galera.append(candidato.copy())         # COPIA DO DICT ANTES DE LIMPA-LO

# PARTE 5

print('=+=' * 20)

#print(galera)

print(f'\nO total de candidatos inseridos:\n\n\033[1;31;42mForam de >> {len(galera)} pessoa/as<<\033[m')# cor verde

print(f'O total de candidatos a cada uma das áreas:\n\n',len(eng),"\033[1;31;46mem Engenharia\033[m\n")  # cor azul

print(    len(ban)  ,  "\033[1;31;43mem Banco de Dados\033[m\n\n",len(a_proj),"\033[4;31;44mem Analise e Projeto de Algoritmos\033[m\n")      #ban= cor amarela  e  a_proj= cor lilais

print('-='*35)

print('posiçao', end=' ' )

for i in candidato.keys(): # PECORRER AS CHAVES DE CANDIDATOS 

    print(f'{i :<15}', end=' ')

print() 

print('-='*35)



for k, v in enumerate(galera): # CHAVES E VALORES EM GALERA QUE E A COPIA DE CANDIDATO 

        print (f' {k :>3} ', end='  ')

        for g in v.values():

                print (f'{str( g ) :<15} ', end='  ')   

        print()
