 # EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br
import random
def carregar_cenarios():
    cenarios = {
        "saguao": {
            "titulo": "Saguao do per1go!",
            "descricao": "Voce esta no saguao de entrada do insper.",
            "opcoes": {
                "sala do professor": "Tomar o elevador para a sala do professor.",
                "biblioteca": "Ir para a biblioteca.",
                "fab lab" : "Ir para o fab lab de escada."
            }
        },
        "biblioteca": {
            "titulo": "Andar Sagrado",
            "descricao": "Voce chegou na biblioteca. Shhhhhh!!!",
            "opcoes": {
                "saguao": "Tomar o elevador para o saguao de entrada.",
                "armario": "Você tem a chance de ganhar o jogo!"
            }
        },
        "fab lab": {
            "titulo": "O monstro te aguarda",
            "descricao": "Você chegou ao fab lab"
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {
                    "saguao": "Tomar o elevador para o saguao de entrada",
            }
        },
        "armario": {
            "titulo": " Você chegou ao corredor dos armários",
            "descricao": "Para adiar o EP você deve acertar esse enigma. "
                         "Qual a resposta para a vida, o universo e tudo mais??? "
                         "Se não souber a resposta volte à biblioteca e continue a sua jornada.",
            "opcoes": {
                "biblioteca": "Voltar para a biblioteca",
            }
        },
        "sala do professor": {
            "titulo": "Você chegou na sala do Rei Toshi. Ajoelhe-se!",
            "descricao": "Rei Toshi: Para adiar o EP é necessário que me prove o seu valor! Me diga a senha que te ajudarei a concluir o seu obj3tivo!"
                         " Só assim você mudará a data de entrega do EP!",
            "opcoes": {
                "saguao": "Ir para o saguao de entrada",
            }
        }
    }
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual


def main():
    lista_inventario=[]
    ataque_homem=5
    ataque_monstro=10
    hp_monstro=120
    hp_homem=100
    cont=0

    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o pr0fessor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        
        cenario_atual = cenarios[nome_cenario_atual]
        print (cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print (cenario_atual['descricao'])
        print ()

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
                print(cenarios['biblioteca']['titulo'])
                print('-'*len(cenarios['biblioteca']['titulo']))
                print(cenarios['biblioteca']['descricao'])

                #escolha = input ("Digite a sua opção: ")
                print('Aqui se encontra um teleporte que te levara aos armários, você têm duas opções:')
                print('1°) A primeira é você participar de um jogo em que será sorteado um número de 0 a 10, e você deve acerta-lo com apenas uma chance. Caso você não acerte, você será guiado a outra opção obrigatoriamente.')
                print('2°) A segunda opção é você achar a chave secreta em algum local do Insper, essa chave chega abrirá o elevador. ')

                sorteio = input('Pois então, vamos de sorteio ou prefere desistir da tentativa ? (Sim/Não): ')
                print ( 'Se você recusar essa chance, você será teleportado para o saguão!!!')
                while True:
                    if sorteio == 'Sim':
                        numero_sorteio = random.randint(0, 10)
                        numero_chute = int(input('Eai??? Qual o seu chute ?: '))

                        if numero_chute == numero_sorteio:
                            print ('Você ganhou e foi teleportado para a sala dos armarios')
                            print ()
                            cenario_atual="armario"
                            break
                        else:
                            print('''Você errou o número sorteado, e voltou para o saguão inicial''')
                            break
                    elif sorteio== 'Não':
                        print('Que pena, você desistiu do sorteio. Mas agora você têm uma nova missão para adiar seu EP, sem mais enrolações, agora ache a chave do elevador. Boa Sorte!!!')
                        break
                    else:
                        print('Não existe essa opção!')
                        sorteio=input('Você aceita particiar do sorteio? (Sim/Não)')
            while escolha not in opcoes:
                if escolha!= opcoes:
                    escolha=input('Não existe essa opção. Escreva uma nova: ')

            if cenario_atual=='armario':
                print(cenarios['armario']['titulo'])
                print('-' * len(cenarios['armario']['titulo']))
                print(cenarios['armario']['descricao'])
                resp=input('Qual a sua resposta: ')
                print()

                if resp=='42':
                    game_over=True
                else:
                    print ('Você não acertou, e morreu. Volte para o saguão inicial e reinicie a sua jornada')
                    print ()

            if escolha=='sala do professor':
                print(cenarios['sala do professor']['titulo'])
                print('-'*len(cenarios['sala do professor']['titulo']))
                print(cenarios['sala do professor']['descricao'])
                print()
                print('Rei Toshi: Para adiar o EP é necessário que me prove o seu valor! Me diga a senha que te ajudarei para concluir o seu objetivo!')
                senha=input('Qual a senha? Obs: A senha está espalhada ao longo do diálogo do jogo!!!: ')

                if senha == '103':
                    print('Parabéns, você acertou a senha. Agora foi adicionada a chave ao seu inverntário.')
                    print('Sua recompença além da chave é uma arma a qual você pode escolher.')
                    arma=input('Escolha uma dessas armas: [Lâmina do infinito] | [Excalibur ] | [Katana]')
                    lista_inventario.append(arma)
                    ataque_homem=15
                else:
                    print('Que pena você errou a senha.')
                    print('Procure a senha nas salas!!!')
                    escolha = 'saguao'
            if escolha == 'fab lab':
                print(cenarios['fab lab']['titulo'])
                print('-'*len(cenarios['fab lab']['titulo']))
                print(cenarios['fab lab']['descricao'])
                print()

                if cont==0:
                    print('Você agora terá que lutar contra o monstro do fab lab, ele é temido por suas armas de acrílico, feitas na cortadora a laser')
                    acao=input('O monstro corre em direção a você, o que você faz?  [correr do monstro] | [bater no monstro ]')

                    if acao == 'correr do monstro':
                        print('Você fugiu para o saguão!')
                        escolha = 'saguao'
                    elif acao == 'bater no monstro':
                        while hp_monstro!=0:
                            hp_monstro-=ataque_homem
                            hp_homem-=ataque_monstro
                        if hp_homem<=0:
                            print('Você morreu!!!')
                            print('Tente aumentar o seu dano ou/e sua vida! ')
                            for item in lista_inventario:
                                del lista_inventario[item]
                            escolha = 'saguao'
                            break
                        else:
                            print('PARABÉNSSS, você acabou de vencer o monstro do fab lab!!!')
                            print()
                                
                            cont+=1
                    else:
                        print('essa opcao nao existe')
                        acao = input('O monstro corre em direção a você, o que você faz?  [Correr do monstro] | [Bater no monstro com a espada]')
                if cont > 0:
                    print('Você acabou de lutar com o monstro e obteve a chave do elevador, vá até lá, senão não conseguirá adiar seu EP, ')
                    print('Você foi teleportado de volta ao saguão.')
                    escolha = 'saguao'
                                                 
                            
                    

                 
    print("Você ganhou!")

# Programa principal.
if __name__ == "__main__":
    main()