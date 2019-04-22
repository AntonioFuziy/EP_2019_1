 # EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Ramon Menegatto Gonzalez, ramonmg@al.insper.edu.br
# - aluno B: Antonio Vieira Fuziy, antoniovf@al.insper.edu.br
# - aluno C: Victor Vergara Arcoverde de Albuquerque Cavalacanti, victorvaac@al.insper.edu.br

import pygame
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('Musica.mp3')
pygame.mixer.music.play(1)

import random
from time import sleep
def carregar_cenarios():

 #   with open('cenario_jogo.py','r') as arquivo:

 #       conteudo = arquivo.read()
#
   # cenarios = json.loads(conteudo)

    cenarios = {
        "Saguão": {
            "titulo": "Saguão do per1go! ",
            "descricao": "Voce esta no saguão de entrada do Insper. ",
            "opcoes": {
                "sala do professor": "Tomar o elevador para a sala do professor. ",
                "biblioteca": "Ir para a biblioteca. ",
                "fab lab" : "Ir para o fab lab de escada. "
            }
        },
        "biblioteca": {
            "titulo": "Andar Sagrado ",
            "descricao": "Voce chegou na biblioteca. Shhhhhh!!! ",
            "opcoes": {
            
            }
        },
        "fab lab": {
            "titulo": "O monstro te aguarda ",
            "descricao": "Você chegou ao fab lab "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma. ",
            "opcoes": {
                   
            }
        },
        "armário": {
            "titulo": " Você chegou ao corredor dos armários ",
            "descricao": "Para adiar o EP você deve acertar esse enigma. "
                         "Qual a resposta para a vida, o universo e tudo mais??? "
                         "Se não souber a resposta volte à biblioteca e continue a sua jornada.",
            "opcoes": {
                
            }
        },
        "sala do professor": {
            "titulo": "Você chegou na sala do Rei Toshi. Ajoelhe-se! ",
            "descricao": "Rei Toshi: Para adiar o EP é necessário que me prove o seu valor! Me diga a senha que te ajudarei a concluir o seu obj3tivo! "
                         " Só assim você mudará a data de entrega do EP! ",
            "opcoes": {
                
            }
        }
    }

    nome_cenario_atual="Saguão"

    return cenarios, nome_cenario_atual

def linha():
    print('-'*25)
def main():
    lista_inventario=[]
    ataque_homem=5
    ataque_monstro=10
    hp_monstro=120
    hp_homem=100
    cont=0
    i=0
    
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        def titulo1(nome_cenario_atual):
            cenario_atual = cenarios[nome_cenario_atual]
            print (cenario_atual['titulo'])
            print('-'*len(cenario_atual['titulo']))
            print (cenario_atual['descricao'])

        print (titulo1(nome_cenario_atual))

        opcoes = cenario_atual['opcoes']

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print ('As opções disponiveis são: ')
            print ()
            for k,v in opcoes.items():
                print ('-{0}: {1}'.format(k,v))
            escolha =input("Digite a sua opção: ")
           
            if escolha == 'biblioteca':
                nome_cenario_atual='biblioteca'
                titulo1(nome_cenario_atual)

                #escolha = input ("Digite a sua opção: ")
                print('Aqui se encontra um teleporte que te lev4rá aos armários, você têm duas opções:')
                print('1°) A primeira é você participar de um jogo em que será sorteado um número de 0 a 10, e você deve acerta-lo com apenas uma chance. Caso você não acerte, você será guiado ao saguão')
                print()
                print('2°) A segunda opção é um elevador porém esse só será liberado se houver uma chave. ')
                opc = input('Qual das opções deseja seguir? 1 representa a primeira, 2 representa a segunda: ')
                if opc == '2':
                    if 'chave' in lista_inventario:
                        print('O elevador abre, você entra. Ele te leva até o céu dos programadores! Chegando lá você encontra Rei Toshi!')
                        print()
                        print('Rei Toshi: "Você provou seu valor! Você é um programador de verdade! Não há necessidade de fazer o EP!')
                        print()
                        print('Bem vindo ao mundo superior!')
                        game_over=True
                    else:
                        print('Você não contém a chave para o elevador! Procure a chave pelas salas.')
                        nome_cenario_atual='Saguão'
                elif opc == '1':
                    print ( 'Se você recusar essa chance, você será perderá seus iten e voltará para o ínicio!!!')
                    sorteio = input('Você deseja iniciar o sorteio? (Sim/Não): ')
                    while True:
                        if sorteio == 'Sim':
                            numero_sorteio = random.randint(0, 10)
                            linha()
                            numero_chute = int(input('Eai??? Qual o seu chute ?: '))

                            if numero_chute == numero_sorteio:
                                print ('Você ganhou e está sendo teleportado para a sala dos armários')
                                print ('loading...')
                                sleep(5)
                                linha()
                                cenario_atual="armário"
                                break
                            else:
                                print('Você errou o número sorteado, e voltou para o saguão inicial')
                                print ()
                                nome_cenario_atual='Saguão'
                                del lista_inventario[:]
                                break
                        elif sorteio == 'Não':
                            print('Que pena, você desistiu do sorteio. Mas agora você têm uma nova missão para adiar seu EP, sem mais enrolações, agora ache a chave do elevador. Boa Sorte!!!')
                            break
                        else:
                            print('Não existe essa opção!')
                            linha()
                            sorteio=input('Você aceita particiar do sorteio? (Sim/Não)')
                else:
                    print('Não existe essa opção!')
                    linha()
                    opc = input('Qual das opções deseja seguir? 1 representa a primeira, 2 representa a segunda: ')
            while escolha not in opcoes:
                if escolha!= opcoes:
                    escolha=input('Não existe essa opção. Escreva uma nova: ')

            if cenario_atual=='armário':
                print(cenarios['armário']['titulo'])
                print('-' * len(cenarios['armário']['titulo']))
                print(cenarios['armário']['descricao'])
                resp=input('Qual a sua resposta: ')
                print()

                if resp=='42':
                    game_over=True
                else:
                    print ('Você não acertou, e morreu. Volte para o saguão inicial e reinicie a sua jornada')
                    print ()

            if escolha=='sala do professor':
                if i==0:
                    nome_cenario_atual='sala do professor'
                    print (titulo1(nome_cenario_atual))
                    print()
                    print ('A senha está espalhada ao longo do diálogo')
                    print ('Se você negar a tentativa de senha, voltará ao saguão')
                    a=input('Você deseja tentar a senha??? Se você errar, perderá TUDO!!! Responda com Sim ou Não: ')
                    if a=='Sim':
                        senha=input('Qual a senha?: ')
                        print ()
                        if senha == '143' or senha=='341' or senha=='413' or senha=='431' or senha=='134' or senha=='314':
                            print('Parabéns, você acertou a senha. Agora foi adicionada a chave ao seu inverntário.')
                            print('Sua recompença além da chave é uma arma a qual você pode escolher.')
                            print('Após a escolha da arma você voltará para o saguão.')
                            arma=input('Escolha uma dessas armas: Espada laser, Espada de madeira, Cajado: ')
                            lista_inventario.append(arma)
                            print ('Agora você possui um/uma {}'.format(arma))
                            sleep(4)
                            i+=1
                            nome_cenario_atual='Saguão'
                        else:
                            print('Que pena você errou a senha.')
                            print('Procure a senha nas salas!!!'/n)
                            print ('Teleportando')
                            sleep(3)
                            nome_cenario_atual = 'Saguão'
                            del lista_inventario[:]
                                                
                    elif a=='Não':
                        print('Você será teleportado para o saguão em alguns segundos.')
                        print('Teleportando...')
                        sleep(5)
                        nome_cenario_atual='Saguão'
                    
                    else:
                        print('Não existe essa opção, tente digitar novamente')
                        a=input('Qual a sua escolha?: ')
                else:
                    print('Você já conseguiu a espada de sua escolha, agora vá procurar a chave pelo Insper para conseguir adiar seu EP.')
                    print('Teleportando de volta ao saguão...')
                    sleep(3)
                    
            if escolha == 'fab lab':
                nome_cenario_atual='fab lab'
                print (titulo1(nome_cenario_atual))

                if cont==0:
                    print('Você agora terá que lutar contra o monstro dos retalhos')
                    print ('Este monstro é famoso por sua velocidade. Cuidado!!!')
                    print ('O monstro corre em direção a você, o que você faz?')
                    acao=input('Correr do monstro / Bater no monstro: ')
                    
                    print ()
                    if acao == 'Correr do monstro':
                        print('Você está fugindo para o saguão!\n')
                        sleep(3)
                        print('Despistando o monstro...\n')
                        sleep(3)
                        print('Ufa, você conseguiu despistar o monstro, mas parece que há algo escondido no fab lab que você precisa muito para adiar o EP')
                        nome_cenario_atual = 'Saguão'
                    elif acao == 'Bater no monstro':
                        while hp_monstro!=0 or hp_homem==0:
                            if len(lista_inventario)==0:
                                print ('Você não aguentou os terriveis cortes dos retalhos.')
                                print ()
                                print ('Quem sabe da próxima vez.(~__~)')
                                sleep(3)
                                nome_cenario_atual = "Saguão"
                                break
                            elif arma in lista_inventario:
                                if arma=='Espada laser':
                                    ataque_homem=15
                                    hp_homem-=ataque_monstro
                                    hp_monstro-=ataque_homem
                                elif arma=='Espada de madeira':
                                    ataque_homem=10
                                    hp_homem-=ataque_monstro
                                    hp_monstro-=ataque_homem
                                elif arma=='Cajado':
                                    ataque_homem=10
                                    hp_homem-=ataque_monstro
                                    hp_monstro-=ataque_homem
                                    hp_homem+=5
                            else:
                                ataque_homem=5
                                hp_homem-=ataque_monstro
                                hp_monstro-=ataque_homem
                        try:
                            if arma=='Cajado' and hp_monstro<=0:
                                print ('Por você ser digno a passiva do Cajado foi ativada e você a cada ataque recuperou sua vida.')
                                print ('Você ganhou com {} de vida'.format(hp_homem))
                                print ('Você será teleportado para o saguão em segundos')
                                print ()
                                lista_inventario.append('chave')
                                cont+=1
                                sleep(5)
                                nome_cenario_atual='Saguão'
                            elif arma=='Espada de madeira' and hp_monstro>=0:
                                print ('Sua espada não foi efetiva contra o monstro. Você morreu e perdeu seus itens.')
                                print()
                                print ('Sinto muito. O Saguão te espera')
                                sleep(3)
                                del lista_inventario[:]
                                nome_cenario_atual='Saguão'
                            elif arma=='Espada laser' and hp_monstro<=0:
                                print ('Você escolheu a arma mais efetiva e derrotou o monstro. Aceite essa chave.')
                                print ()
                                lista_inventario.append('chave')
                                cont+=1
                                sleep(5)
                                nome_cenario_atual='Saguão'
                        except UnboundLocalError:
                            print()

                            
                    else:
                        print('Essa opcao nao existe')
                        acao = input('O monstro corre em direção a você, o que você faz?  [Correr do monstro] | [Bater no monstro com a espada]')
                elif cont > 0:
                    print('Você já obteve a chave, volte para o saguão.')
                    sleep(5)
                    nome_cenario_atual = 'Saguão'
                                                 
                            
                    

                 
    print("Você ganhou!")

# Programa principal.
if __name__ == "__main__":
    main()