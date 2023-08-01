comprador = 10
compras_feitas = []
def titulo():
    print()
    print('''\033[1;31m                     Simulador de supermercado pobre 1.0\033[m''')
    print()
def produtos():
    print()
    print('''\033[1;30m                    Temos os seguintes produtos disponiveis:

                    \033[1;34mCoca-cola 2l    > 7RS     (1)
                    Guaravita 150ml > 1RS     (2)
                    Caderno grande  > 3RS     (3)
                    Caneta bic azul > 1RS     (4)

                    OU APERTE \033[1;31m(8)\033[1;34m PARA SAIR DO MERCADO E ENCERRA O PROGRAMA.
                    OU APERTE \033[1;31m(9)\033[1;34m PARA PEDIR EMPRESTIMO AO BANCO NOXE.
                    
                    \033[1;32mEm breve mais produtos serão adicionados!\033[m''')
    print()
def total():
    global compras
    print()
    try:
        compras = int(input('\033[1;36mEscolha o produto: \033[m'))
        saldo()
    except ValueError:
        print('Ops! Opção invalida! Tente novamente.')
        total()
def saldo():
    global comprador
    global compras
    from  time import sleep
    print()
    print('\033[1;30mNoticia do dia:\033[m')
    noticias()
    sleep(2)
    if compras == 1:
        print()
        dialogococa_cola()
        sleep(2)
        print()
        print('\033[1;32mOk, você comprou a COCA-COLA 2L! Foi retirado 7 reais do seu saldo!')
        comprador -= 7
        print('\033[1;35mSaldo: \033[m', comprador)
        produtos()
        compras_feitas.append('Coca-cola 2L')

    elif compras == 4:
        print('\033[1;32mOk, você comprou a canaeta bic azul! Foi retirado 1 real do seu saldo!')
        comprador -= 1
        print('\033[1;35mSaldo: \033[m', comprador)
        produtos()
        compras_feitas.append('Caneta bic azul')

    elif compras == 2:
        print()
        dialogoguaravita_()
        sleep(2)
        print()
        print('\033[1;32mOk, você comprou o Guaravita 150ml! Foi retirado 1 real do seu saldo!')
        comprador -= 1
        print('\033[1;35mSaldo: \033[m', comprador)
        produtos()
        compras_feitas.append('Guaravita 150ml')

    elif compras == 9:
       emprestimo_banco()

    elif compras == 3:
        print('\033[1;32mOk, você comprou o Caderno grande! Foi retirado 3 reais do seu saldo!')
        print('\033[1;35mSaldo: \033[m', comprador)
        comprador -= 3
        produtos()
        compras_feitas.append('Caderno grande')
    elif compras == 8:
        mercado_sem_nada()

        print('\033[1;32mSaindo do mercado...')
        print('\033[1;35mSaldo: \033[m', comprador)
        print('\033[1;30mCompras feitas:')
        print('\033[1;33m')
        for compra in compras_feitas:
            print('>{}<'.format(compra))
        exit()
    return False
def controle_financeiro():
    global comprador
    if comprador == 0:
        print('''\033[1;32mOpa, aqui é o banco NOXE, vimos que você comprou um produto e ficou com saldo negativo
    infelizmente não podemos aprovar a sua compra! END GAME!\033[m''')
        print('\033[1;32mCompras feitas: ')
        for compras in compras_feitas:
            print('>{}<'.format(compras))
        exit()
    elif comprador < -1:
        print('''\033[1;32mOpa, você não tem saldo! E está devendo ao banco agora! END GAME''')
        print()
        print('\033[1;30Compras feitas: ')
        for compras in compras_feitas:
            print('>{}<'.format(compras))
        exit()
    elif comprador == 8:
        print('\033[1;30mUau! Você está movimentando a conta :O Tome 2 reais extras!\033[m')
        comprador += 2
def emprestimo_banco():
    from time import sleep
    from random import randint
    global comprador
    print()
    print('\033[1;36m*'*50)
    comprasz = int(input('\033[1;33mAperte 5 para iniciar o banco'))
    print('\033[1;36m*\033[m' * 50)
    while comprasz != 5:
        print('Aperte 5! Aperte 5!')
        return emprestimo_banco()
    if comprasz == 5:
        print()
        print('''\033[1;30mAtendente: O que você deseja?''')

        print('''\033[1;31mUsuario: De um emprestimo.''')

        print('''\033[1;30mAtendente: Qual é o valor de emprestimo?''')
        print()
    try:
        empre = int(input(                                  '''\033[1;34mEscolha o valor do emprestimo:
(1) 10R$
(2) 20R$
(3) Volta para o menu principal e cancelar o emprestimo\033[m'''))

        if empre == 1:
              print()
              print('Atendente: Ok, vamos tentar solicitar seu emprestimo')
              print('Atendente: Primeiro vamos olha seu saldo bancario atual')
              if   comprador >= 7:
                  print()
                  aleatorio = randint(0,6)
                  if aleatorio == 4:
                     print('O gerente disse que o seu saldo é alto. Negado!')
                     produtos()
                     return total()
                  else:
                      print('Mesmo seu saldo sendo alto o gerente liberou!')
                      comprador+= 10
                      produtos()
                      return total()
              elif comprador < 3:
                  print('O gerente liberou o emprestimo')
                  comprador += 10
                  produtos()
                  return total()

        elif empre == 2:
            print('Atendente: O valor que você está pedido é elevado')
            print('Atendente: Vamos ter uma reunião com o atendente pra decidir')
            print()
            print('Aguarde 10s')
            sleep(10)
            aleatorio2 = randint(0,10)
            if aleatorio2 ==  5:
                print('Seu emprestimo foi aprovado!')
                print()
                comprador+= 20
                produtos()
                return total()
            else:
                print('Emprestimo negado!')
                print()
                produtos()
                return total()
        elif empre == 3:
            print()
            print('Voltando para loja')
            produtos()
            return total()
        else:
            print('Opção invalida! Voltando para loja')
            produtos()
            return total()
    except ValueError:
        print('Opção invalida! Volte para o menu!')
        return total()
#Dialogos dos atendentes
def dialogococa_cola():
    import random
    atendente = [
'\033[1;35mAtendente: Coca-cola? Boa pedida!',
'\033[1;35mAtendente: Coca-cola? É sempre bom kk',
'\033[1;35mAtendente: Cara, coca-cola é vida!',
'\033[1;35mAtendente: Não sou muito de beber coca-cola']
    atendenteone = random.choice(atendente)
    print(atendenteone)
def dialogoguaravita_():
    import random
    guara = ['Atendente: Guaravita? Ok, você tem bom gosto!',
             'Atendente: Guaravita é uma boa hein!',
             'Atendente: Guaravita nesse calor é divino',
             'Atendente: Guaravita não é minha praia']
    vita = random.choice(guara)
    print('\033[1;34m' + vita)
#Dialogo ao sair do mercado?
def mercado_sem_nada():
    from time import sleep
    print()
    if comprador >= 10:
        print()
        print('\033[1;31mFuncionario: Olá senhor! Porque você não faz mais compras?')
        volta = int(input('\033[1;32mAperte (1) PARA VOLTA OU (2) PARA SAIR DE VEZ!'))
        if volta == 1:
            print()
            print()
            print('\033[1;30mUsuario: Ok, vou da uma olhada em tudo novamente!')
            print('\033[1;34mFuncionario: Boas compras!')
            sleep(3)
            titulo()
            sleep(1)
            produtos()
            total()
        elif volta == 2:
            print()
            print()
            print('\033[1;31mUsuario: Obrigado, Mas estou com pressa!')
            sleep(2)
            print('\033[1;30mFuncionario: Ok.\033[m')
            sleep(2)
            exit()
#Noticias_Sobre_produtos
def noticias():

    from random import choice
    produtos_noticias = ['*Coca-cola é a nova sensação do momento',
                         '*Coca-cola sofre queda no mês atual',
                         '*Coca-cola agora tem novo visual',
                         '*Guaravita agora está disponivel em mais lojas',
                         '*Guaravita é a sensação do momento',
                         '*Banco noxe em crise!',
                         '*Banco noxe passa por um momento dificil',
                         '*Banco noxe nas alturas',
                         '*Gerente do banco noxe diz: Está tudo certo!',
                         '*Gerente do banco noxe diz: Estamos subindo ainda mais',
                         '*Banco noxe está fazendo emprestimo!']
    bank = choice(produtos_noticias)
    print('\033[1;30m' + bank + '*')
noticias()
titulo()
produtos()
while True:
    total()
    controle_financeiro()
